import datetime as dt
import os

import requests
from dotenv import load_dotenv

load_dotenv()

# Nutritionix (Exercise Data + Natural Language Model for user inputs)
NUTRITIONIX_ID = os.getenv("nutritionix_id")
NUTRITIONIX_API_KEY = os.getenv("nutritionix_api_key")
NUTRITIONIX_DOMAIN = "https://trackapi.nutritionix.com"
nutritionix_header = {
    "x-app-id": NUTRITIONIX_ID,
    "x-app-key": NUTRITIONIX_API_KEY,
}
# -> Natural Language
natural_language_endpoint = "/v2/natural/exercise"
nutritionix_params = {
    "query": str(input("Tell me which exercise you did: ")),
    "weight_kg": str(input("Please insert weight in kg: ")),
    "height_cm": str(input("Please insert height in cm: ")),
    "age": str(input("Please enter your age: "))
}

# Sheety (Google Sheets API)
SHEETY_TOKEN = os.getenv("sheety_token")
SHEETY_WORKOUT_SHEET = f"https://api.sheety.co/{SHEETY_TOKEN}/workoutTracker/workouts"
SHEETY_AUTH_TOKEN = os.getenv("sheety_auth_token")
sheety_header = {
    "Authorization": f"Bearer {SHEETY_AUTH_TOKEN}"
}

# Date and Time at the moment of request
now = dt.datetime.now()
date_now = now.strftime("%Y/%m/%d")
time_now = now.strftime("%H:%M:%S")

# Request and converting it into .json(), getting exercise data
nutritionix_request = requests.post(f"{NUTRITIONIX_DOMAIN}{natural_language_endpoint}",
                                    json=nutritionix_params,
                                    headers=nutritionix_header)
request_data = nutritionix_request.json()
exercises = request_data["exercises"]

# Add excercise data to spreadsheet (for every exercise in exercises list)
for exercise in exercises:
    sheety_data = {
        "workout": {
            "date": date_now,
            "time": time_now,
            "exercise": str(exercise["user_input"]).title(),
            "duration": exercise["duration_min"],
            "calories": int(exercise["nf_calories"]),
        }
    }
    sheety_post = requests.post(SHEETY_WORKOUT_SHEET,
                                json=sheety_data,
                                headers=sheety_header)
