# -----------------------------------------------------------------------------
# File:    main.py
# Project: 100 Days of Python - Day 32 - Starter project
# Purpose: Send motivational quote on a Monday via smtp email message.
# -----------------------------------------------------------------------------
import smtplib
import datetime as dt

from config import (
    MY_EMAIL,
    MY_APP_PASSWORD,
    QUOTES_TXT,
    RECIPIENT_EMAIL
)
from src.data_loader import load_quotes, get_random_quote

def send_motivational_quote(quotes_file_path, recipient_email):
    """
    Loads the quote data into a list using the load_quotes function.
    Uses the datetime module to get the current day of the week. If the day of the week is Monday,
    creates a smtp_ssl connection then sends a random motivational quote from the quote list to a
    recipient specified in the config file.

    :param quotes_file_path: path to the text file to load
    :param recipient_email: email address of the recipient
    :return: none
    """

    quotes = load_quotes(quotes_file_path)
    now = dt.datetime.now()
    day_of_week = now.weekday()

    if day_of_week == 0 :

        random_quote = get_random_quote(quotes)

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
            connection.login(user=MY_EMAIL, password=MY_APP_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=recipient_email,
                msg=f"Subject:Your motivational quote for the week!\n\n{random_quote}"
            )
    else:
        print("Not Monday, skipping.")

if __name__ == "__main__":
    send_motivational_quote(QUOTES_TXT, RECIPIENT_EMAIL)