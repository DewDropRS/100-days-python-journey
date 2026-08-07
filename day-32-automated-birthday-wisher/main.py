# -----------------------------------------------------------------------------
# File:    main.py
# Project: 100 Days of Python - Day 32 - Automated birthday wisher
# Purpose: Checks birthdays.csv for matches to today's date and sends each
#          match a personalized birthday email using a randomly selected
#          letter template.
# -----------------------------------------------------------------------------
import random
import smtplib
import datetime as dt

from config import (
    BIRTHDAYS_CSV,
    BIRTHDAY_LETTERS,
    PLACEHOLDER_NAME,
    MY_EMAIL,
    MY_APP_PASSWORD
)
from src.data_loader import load_birthdays_csv

def send_birthday_wishes():
    """
    Loads birthday records from CSV, filters for matches to today's date,
    and sends a personalized birthday email to each match using a randomly
    selected letter template.

    :return: None
    """

    today = dt.datetime.now()

    # All birthdays to track
    birthdays = load_birthdays_csv(BIRTHDAYS_CSV)

    # Today's birthdays list
    todays_birthdays = [
        person for person in birthdays
        if int(person["month"]) == today.month and int(person["day"]) == today.day
    ]

    if todays_birthdays:
        for person in todays_birthdays:
            letter_template = random.choice(BIRTHDAY_LETTERS)
            with open(letter_template) as template:
                contents = template.read()
            custom_letter = contents.replace(PLACEHOLDER_NAME, person["name"])

            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
                connection.login(user=MY_EMAIL, password=MY_APP_PASSWORD)
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=person["email"],
                    msg=f"Subject:Happy Birthday!\n\n{custom_letter}"
                )

            print(f"Birthday wish email sent to {person['name']}:{person['email']}")

if __name__ == "__main__":
    send_birthday_wishes()