from data_manager import DataManager
import requests
import os
from dotenv import load_dotenv
import pprint
load_dotenv()

data_manager = DataManager()




print("Welcome to the flight deal tracker!")
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
user_email = input("What is your email: ")
if input("Enter your email again for confirmation: ") == user_email:
    data_manager.update_user_info(first_name,last_name,user_email)
    print("Thanks for signing up!")
else:
    print("Sorry your email doesn't match...")