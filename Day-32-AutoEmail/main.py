'''
Author: Maaz Ali
Date: May 29
A program to send out emails automatically using smtplib and datetime
'''

import smtplib
import datetime as dt
import random
import pandas

my_email = "test@gmail.com"
my_password= "test"

now = dt.datetime.now()
now_month = now.month
now_day = now.day
date_tuple = (now_month, now_day)

birthday_data = pandas.read_csv("birthdays.csv")
birthday_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in birthday_data.iterrows()}
print(birthday_dict)
if date_tuple in birthday_dict:
    person = birthday_dict[date_tuple]["name"]
    with open(f"./letter_templates/letter_{random.randint(1,3)}.txt", "r") as letter_file:
        content = letter_file.read()
        content = content.replace("[Name]", person)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthday_dict[date_tuple]["email"],
            msg=f"Subject:Happy Birthday!\n\n{content}"
            )
                                    