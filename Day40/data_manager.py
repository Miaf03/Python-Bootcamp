import os
import requests
from dotenv import load_dotenv

load_dotenv()

SHEETY_PRICES_ENDPOINT = os.environ["SHEETY_PRICES_ENDPOINT"]
SHEETY_USERS_ENDPOINT = os.environ["SHEETY_USERS_ENDPOINT"]
SHEETY_TOKEN = os.environ["SHEETY_TOKEN"]

HEADERS = {
    "Authorization": f"Bearer {SHEETY_TOKEN}"
}

class DataManager:
    def __init__(self):
        self.destination_data = {}
        self.customer_data = {}

    def get_destination_data(self):
        """Gets destination data from the prices sheet"""
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=HEADERS)
        data = response.json()
        print("DEBUG Sheety response (destinations):", data)
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        """Updates IATA codes in the prices sheet."""
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data,
                headers=HEADERS
            )
            print(response.text)
    
    def get_customer_emails(self):
        """Gets customer emails from the users sheet"""
        response = requests.get(
            url=SHEETY_USERS_ENDPOINT,
            headers={"Authorization": f"Bearer {os.environ['SHEETY_TOKEN']}"}
        )
        
        data = response.json()
        print(f"DEBUG Sheety response (customers): {data}")
        self.customer_data = data["users"]
        return self.customer_data