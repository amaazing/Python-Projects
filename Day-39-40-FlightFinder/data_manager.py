import requests
import os
from dotenv import load_dotenv
import pprint
load_dotenv()
SHEETY_ENDPOINT = os.getenv("SHEETY_ENDPOINT")
SHEETY__USER_INFO_ENDPOINT = os.getenv("SHEETY_USER_INFO_ENDPOINT")


class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self._authorization = {"Authorization": os.getenv("SHEETY_AUTHORIZATION")}
        self.city_data = {}
        
    def get_data(self):
        r = requests.get(url=SHEETY_ENDPOINT, headers=self._authorization)
        data = r.json()["prices"]
        return data
        
    def update_destination_codes(self):
        for city in self.city_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_ENDPOINT}/{city['id']}",
                json=new_data,
                headers=self._authorization
            )
            
    def update_user_info(self, first_name, last_name, email):
        body = {
            "user" : {
                "firstName" : first_name,
                "lastName" : last_name,
                "email" : email,
                }
        }
        r = requests.post(url=SHEETY__USER_INFO_ENDPOINT, headers=self._authorization, json=body)
        print(r.raise_for_status())
        