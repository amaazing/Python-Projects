import os
from dotenv import load_dotenv
import requests
load_dotenv()

TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"
IATA_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
FLIGHT_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"


class FlightSearch:

    def __init__(self):
        self._api_key = os.environ["AMADEUS_API_KEY"]
        self._api_secret = os.environ["AMADEUS_SECRET"]
        # Getting a new token every time program is run. Could reuse unexpired tokens as an extension.
        self._token = self._get_new_token()

    def _get_new_token(self):
        body = {
            'grant_type': 'client_credentials',
            'client_id': self._api_key,
            'client_secret': self._api_secret
        }
        header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        response = requests.post(url=TOKEN_ENDPOINT, data=body, headers=header)
        # New bearer token. Typically expires in 1799 seconds (30min)
        return response.json()['access_token']
    
    def city_search(self, city: str):
        header = {"Authorization" : f"Bearer {self._token}"}
        query_by = {
            "keyword" : city,
            "max": 1,
            "include": "AIRPORTS",
        }
        r = requests.get(url=IATA_ENDPOINT, headers=header, params=query_by)
        try:
            iata = r.json()["data"][0]["iataCode"]
        except IndexError:
            print(f"IndexError: No airport code found for {city}.")
            return "N/A"
        except KeyError:
            print(f"KeyError: No airport code found for {city}.")
            return "Not Found"
        return iata
            
    def find_flight(self, origin, destination, start_time, end_time):
        header = {"Authorization" : f"Bearer {self._token}"}
        query = {
            "originLocationCode" : origin,
            "destinationLocationCode" : destination,
            "departureDate" : start_time.strftime("%Y-%m-%d"),
            "returnDate" : end_time.strftime("%Y-%m-%d"),
            "adults" : 1,
            "nonStop" : "true",
            "currencyCode" : "GBP",
            "max" : 10
        }
        r = requests.get(
            url=FLIGHT_ENDPOINT,
            headers=header,
            params=query
        )
        
        if r.status_code != 200:
            print(f"check_flights() response code: {r.status_code}")
            print("There was a problem with the flight search.\n"
                  "For details on status codes, check the API documentation:\n"
                  "https://developers.amadeus.com/self-service/category/flights/api-doc/flight-offers-search/api"
                  "-reference")
            print("Response body:", r.text)
            return None
        return r.json()