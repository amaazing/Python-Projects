'''
MAAZ ALI
Excercise Tracking Using Nutritionix API
JUNE 06 2024
'''

import requests
import os
from dotenv import load_dotenv
from datetime import datetime
load_dotenv()

NUTRITIONIX_KEY = os.getenv("NUTRITIONIX_KEY")
NUTRITIONIX_APP_ID = os.getenv("NUTRITIONIX_APP_ID")
NUTRITIONX_ENDPOINT = 'https://trackapi.nutritionix.com/v2/natural/exercise'
SHEETY_ENDPOINT = os.getenv("SHEETY_ENDPOINT")
SHEETY_TOKEN = os.getenv("SHEETY_TOKEN")

authentication_header = {
    "Content-Type": "application/json",
    "x-app-id" : NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_KEY
}

authentication_parameters = {
    "query": input("What exercise did you do today?")
}
r = requests.post(NUTRITIONX_ENDPOINT, headers=authentication_header, json=authentication_parameters)
result = r.json()

today = (datetime.now()).strftime("%d/%m/%Y")
time = datetime.now().strftime("%X")

#Posting to Google Sheets
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

sheety_authentication = {
    "Authorization": f"Bearer {SHEETY_TOKEN}"
}
for exercise in result["exercises"]:
    sheet_inputs = {
        "sheet1": {
            "date": today_date,
            "time": now_time,
            "exercise": (exercise["name"]).title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(SHEETY_ENDPOINT, json=sheet_inputs, headers=sheety_authentication)

    print(sheet_response.text)