
import requests
import os
from twilio.rest import Client
from dotenv import load_dotenv
load_dotenv()

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
ALPHAVANTAGE_KEY = os.getenv('ALPHAVANTAGE_KEY')
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWSAPI_KEY = os.getenv("NEWSAPI_KEY")

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_KEY = os.getenv("TWILIO_KEY")
TWILIO_PHONE = os.getenv("TWILIO_PHONE")
MY_PHONE = os.getenv("MY_PHONE")

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": ALPHAVANTAGE_KEY
}
r = requests.get(STOCK_ENDPOINT, params=stock_parameters)
data = r.json()
print(data)
closing_dict = [value for (key, value) in data["Time Series (Daily)"].items()]
yesterday_closing = closing_dict[0]["4. close"]
further_closing = closing_dict[1]["4. close"]

difference = abs(float(yesterday_closing) - float(further_closing))

percentage_difference = (difference/float(yesterday_closing)) * 100
if percentage_difference > 0:
    news_parameters = {
        "apiKey": NEWSAPI_KEY,
        "q": COMPANY_NAME,
        "searchIn": "title",
        "sortBy" : "popularity"
    }
    r = requests.get(NEWS_ENDPOINT, params=news_parameters)
    news_data = r.json()["articles"][:3]
    news_list = [f"Headline: {article['title']}\n" f"Description: {article['description']}" for article in news_data]

    client = Client(TWILIO_SID, TWILIO_KEY)

    message = client.messages \
                    .create(
                        body = news_list,
                        from_ = TWILIO_PHONE,
                        to = MY_PHONE 
                    )


