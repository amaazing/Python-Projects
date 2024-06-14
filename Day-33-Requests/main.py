"""
Author: Maaz
Date: May 30 2024
A program to learn usage of requests module to track International Space Station.
"""

import requests
from datetime import datetime
import smtplib
import time

MY_EMAIL = "your email"
MY_PASS = "your password"
MY_LAT = 0 # insert your own
MY_LONG = 0 # insert your own

def pos_in_range() -> bool:
    if MY_LAT - 100 <= latitude <= MY_LAT + 100:
        if MY_LONG - 100 <= longitude <= + 100:
            return True
        
def is_night() -> bool:
    time_now = datetime.now()
    parameters = {
        "lat":MY_LAT,
        "lng":MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    if sunset <= time_now.hour <= sunrise:
        print("Its dark now")
        return True
    
    

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()

longitude = float(data["iss_position"]["longitude"])
latitude = float(data["iss_position"]["latitude"])

iss_position = (longitude, latitude)
print(iss_position)

while True:
    if pos_in_range() == True and is_night() == True:
        connection = smtplib.SMTP("Insert your own smtp connection.")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASS)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg="Subject:ISS Overhead\n\nThe ISS is above your coordinates right now.")
    time.sleep(60)