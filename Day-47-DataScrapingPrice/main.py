'''
Author: Maaz
Date: June 27 2024
Finds the price of the RTX 4070 and emails if it's below a certain threshold.
'''

import requests
from bs4 import BeautifulSoup

PRODUCT_URL = "https://www.amazon.ca/ASUS-DisplayPort-2-56-Slot-Axial-tech-Technology/dp/B0C4BZZWJM/ref=sr_1_2?crid=HZOFD0LMZQGF&dib=eyJ2IjoiMSJ9."
DESIRED_PRICE = 750.00

def send_email():
    import smtplib
    from dotenv import load_dotenv
    load_dotenv()
    import os
    email = os.getenv("EMAIL")
    password = os.getenv("EMAIL_PASSWORD")
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(email, password)
        connection.sendmail(msg=f"Subject: 4070 Price\n\nThe price of the 4070 is desireable!\n{PRODUCT_URL}", from_addr=email, to_addrs=email,)
    

header_params = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) Gecko/20100101 Firefox/127.0",
                 "Accept-Language": "en-CA,en-US;q=0.7,en;q=0.3"
                 }

r = requests.get(PRODUCT_URL, headers=header_params)

html_text = r.text

soup = BeautifulSoup(html_text, "lxml")

float_price = float(soup.select_one('[data-csa-c-slot-id="apex_dp_offer_display"]').get_text(strip=True).split("$")[1])

print(float_price)

if float_price < DESIRED_PRICE:
    send_email()
else:
    print("Sorry, the price is not desireable!")