'''
Maaz Ali
Flight Finder
Day 39/40
A program that finds if a flight to a desired city is within your price range, and sends an SMS 
if it is.
'''

import time
from datetime import datetime,timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager
ORIGIN_CITY_IATA = "LON"

data_manager = DataManager()
sheet_data = data_manager.get_data()
flight_search = FlightSearch()
notification_manager = NotificationManager()

for row in sheet_data:
     if row["iataCode"] == "":
         row["iataCode"] = flight_search.city_search(row["city"])
         # slowing down requests to avoid rate limit
         time.sleep(2)

data_manager.city_data = sheet_data
data_manager.update_destination_codes()

tomorrow = datetime.now() + timedelta(days=1)
time_cutoff = datetime.now() + timedelta(days=(6*30))

for location in sheet_data:
    print(f"Getting flights for {location["city"]}...")
    flights = flight_search.find_flight(
        ORIGIN_CITY_IATA,
        location["iataCode"],
        tomorrow,
        time_cutoff 
    )
    cheapest_flight = FlightData.find_cheapest_flight(flights)
    print(f"{location['city']}: £{cheapest_flight.price}")
    # Slowing down requests to avoid rate limit
    if cheapest_flight.price != "N/A" and cheapest_flight.price < location["lowestPrice"]:
        notification_manager.send_sms(message_str=f"Low price found! From {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}. Heading out at {cheapest_flight.out_date} and returning at {cheapest_flight.return_date}. Only {cheapest_flight.price}!")
        
print("Done!")
