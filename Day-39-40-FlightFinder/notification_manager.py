from twilio.rest import Client
from dotenv import load_dotenv
load_dotenv()
import os

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(os.environ["TWILIO_SID"], os.environ["TWILIO_TOKEN"])
        
    def send_sms(self, message_str):
        message = self.client.messages.create(
            from_ = os.environ["TWILIO_PHONE"],
            body = message_str,
            to = os.environ["MY_PHONE"]
        )
        print(message.sid)
        