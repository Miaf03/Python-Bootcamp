
import requests
import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = os.getenv("OWM_API_KEY")
ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE = os.getenv("TWILIO_PHONE")
MY_PHONE = os.getenv("MY_PHONE")

weather_params = {
    "lat": 18.9186,
    "lon": -99.2340,
    "appid": API_KEY,
    "cnt": 4,
}

response = requests.get(OWM_ENDPOINT, params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = any(int(hour["weather"][0]["id"]) < 700 for hour in weather_data["list"])

if will_rain:
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages.create(
        body="☔️ It will rain in the next few hours. Don’t forget your umbrella!",
        from_=TWILIO_PHONE,
        to=MY_PHONE
    )
    print(f"Message sent with status: {message.status}")
else:
    print("No rain expected in the next few hours")
    