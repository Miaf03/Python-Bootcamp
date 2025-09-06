import os
import spotipy
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth

# Load environment variables

load_dotenv()
CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")

# Ask user for the date

date = input("Which date do you want to travel to? (Format YYYY-MM-DD): ")

# Billboard Hot 100 scraping

billboard_url = f"https://www.billboard.com/charts/hot-100/{date}"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

response = requests.get(billboard_url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# Extract song titles

song_name_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_name_spans]

print(f"🎵 Found {len(song_names)} songs on the Billboard Hot 100 for {date}")

# Spotify authentication

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://127.0.0.1:8888/callback",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)

user_id = sp.current_user()["id"]
print(f"Authenticated user: {user_id}")

# Search for songs on Spotify

song_uris = []
year = date.split("-")[0]

for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track", limit=1)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} not found on Spotify (skipped)")

# Create a new private playlist on Spotify

playlist = sp.user_playlist_create(
    user=user_id,
    name=f"{date} Billboard 100",
    public=False,
    description=f"Billboard Hot 100 for {date}"
)

# Add the found songs to the playlist

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)

print(f"🎉 Playlist created: {playlist['name']} with {len(song_uris)} songs")