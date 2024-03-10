import os
import requests
from datetime import datetime


GENDER = "MALE"
WEIGHT_KG = "80"
HEIGHT_CM = "166"
AGE = "20"

APP_ID = "a074993f"
API_KEY = ""

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}
exercise_text = input("Tell me which exercises you did: ")

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

response = requests.post(url=exercise_endpoint, json=parameters, headers=headers)
result = response.json()


today_date = datetime.now().strftime("%d/%m/%Y")
time_now = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_data = {
        "workout": {
            "date": today_date,
            "time": time_now,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

google_sheets_endpoint = "https://api.sheety.co/0eb23d74081f89ff671a1fcd46e33b18/myWorkouts/workouts"

bearer_header = {
    "Authorization": ""
}
response2 = requests.post(url=google_sheets_endpoint, json=sheet_data, headers=bearer_header)

print(response2.text)
