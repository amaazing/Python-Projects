'''
Maaz Ali
A program that sends an SMS based on the weather using API calls.
June 3, 2024
'''

import requests
from twilio.rest import Client


def weather_message(weather_data):
    rain_check = False
    account_sid = "Your SID"
    auth_token = "YOUR AUTH"
    client = Client(account_sid,auth_token)
    for indices in range(0,4):
        if weather_data["list"][indices]["weather"][0]["main"] == "Rain":
            rain_check = True
            break
    if rain_check == True:
        send_msg = "It is going to rain, bring an umbrella to be safe."
    else:
        send_msg = "No rain, so no umbrella needed."
    message = client.messages \
                    .create(
                        body=send_msg,
                        from_="YOUR PHONE",
                        to="YOUR PHONE"
                    )
    print(message.status)
        
    
if __name__ == "__main__":
    weather_parameters = {"lat": 53.544388,
                "lon": -113.490929,
                "appid": "YOUR ID",
                "cnt": 4
                }
    

    response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=weather_parameters)
    response.raise_for_status()
    data = response.json()
    weather_message(data)
