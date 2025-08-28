
import os
from datetime import datetime
import requests
from dotenv import load_dotenv

load_dotenv()

GENDER = "female"
WEIGHT_KG = 62
HEIGHT_CM = 163
AGE = 22

APP_ID = os.getenv("NUTRITIONIX_APP_ID")
APP_KEY = os.getenv("NUTRITIONIX_APP_KEY")
SHEETY_ENDPOINT = os.getenv("SHEETY_ENDPOINT")
SHEETY_TOKEN = os.getenv("SHEETY_TOKEN")

exercise_text = input("Describe your workout (e.g., 'ran 5 km and swam 30 minutes'): ")

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
headers = {"x-app-id": APP_ID, "x-app-key": APP_KEY}
body = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

res = requests.post(nutritionix_endpoint, json=body, headers=headers)
res.raise_for_status()
exercises = res.json()["exercises"]

today = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%H:%M:%S")

sheety_headers = {"Authorization": f"Bearer {SHEETY_TOKEN}"}

for ex in exercises:
    sheet_body = {
        "workout": {
            "date": today,
            "time": now_time,
            "exercise": ex["name"].title(),
            "duration": ex["duration_min"],
            "calories": ex["nf_calories"]
        }
    }

    sheety_res = requests.post(SHEETY_ENDPOINT, json=sheet_body, headers=sheety_headers)
    sheety_res.raise_for_status()
    print("Saved to Google Sheet:", sheety_res.text)
    