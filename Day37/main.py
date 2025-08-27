
import os
import requests
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

USERNAME = os.getenv("PIXELA_USER") 
TOKEN = os.getenv("PIXELA_TOKEN")
GRAPH_ID = os.getenv("GRAPH_ID")

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# Uncomment the following line ONLY if you haven't created the user on Pixela yet

# response = requests.post(pixela_endpoint, json=user_params)
# print(response.text)

# Create a graph for the habit (only the first time)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Habit Tracker",  
    "unit": "hours",
    "type": "int",
    "color": "ajisai"
}

headers = {"X-USER-TOKEN": TOKEN}

# Uncomment the following line ONLY if you haven't created the graph yet

# response = requests.post(graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# Log a new data point (daily)

today = datetime.now().strftime("%Y%m%d") # Date in YYYYMMDD format
pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"
pixel_data = {
    "date": today,
    "quantity": input("How many kilometers did you run today? ")
}

response = requests.post(pixel_endpoint, json=pixel_data, headers=headers)
print("Log:", response.text)

# Update an existing data point (if you made a mistake)

update_endpoint = f"{pixel_endpoint}/{today}"
new_quantity = input("If you want to correct it, enter a new value (or leave empty): ")
if new_quantity:
    update_data = {"quantity": new_quantity}
    response = requests.put(update_endpoint, json=update_data, headers=headers)
    print("Update:", response.text)

# Delete a data point (if you want to remove it completely)

delete = input("Do you want to delete today's data? (y/n): ")
if delete.lower() == "y":
    response = requests.delete(update_endpoint, headers=headers)
    print("Deleted:", response.text)
