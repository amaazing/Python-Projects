'''
Day 37 Habit Tracker 
Maaz
Uses Pixela API in order to track your habits.
Date: June 5 2024
'''

import requests
import os
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()

PIXELA_TOKEN = os.getenv("PIXELA_TOKEN")
PIXELA_USERNAME = os.getenv("PIXELA_USERNAME")
PIXELA_GRAPH_ID = os.getenv("PIXELA_GRAPH_ID")
URL_ENDPOINT = f"https://pixe.la/v1/users/{PIXELA_USERNAME}/graphs/{PIXELA_GRAPH_ID}"


graph_parameters = {
    "id": PIXELA_GRAPH_ID,
    "name": "Coding",
    "unit": "minutes",
    "type": "int",
    "color" : "sora",
}

graph_header = {
    "X-USER-TOKEN" : PIXELA_TOKEN
}

this_day = datetime.now()

date_parameters = {
    "date" : this_day.strftime("%Y%m%d"),
    "quantity": input("How many minutes did you code today?"),
}

r = requests.post(url=URL_ENDPOINT, json=date_parameters, headers=graph_header)
print(r.text)
