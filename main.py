##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import datetime as dt
import pandas as pd
import smtplib
import random

MY_EMAIL = "testwisangeom@gmail.com"
MY_PASSWORD = "eomm9409"

data = pd.read_csv("birthdays.csv")
user_record = data.to_dict(orient="records")

now = dt.datetime.now()

letters = ["letter_templates/letter_1.txt", "letter_templates/letter_2.txt", "letter_templates/letter_3.txt"]


def send_letter(to_addr, body):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(MY_EMAIL, to_addr, f"Subject:Happy birthday!\n\n{body}")


def write_letter(user):
    letter = random.choice(letters)
    with open(letter) as letter_file:
        original_letter = letter_file.read()
        new_letter = original_letter.replace("[NAME]", user["name"])
        send_letter(user["email"], new_letter)


for user_data in user_record:
    if now.month == user_data["month"] and now.day == user_data["day"]:
        write_letter(user_data)


