# -----------------------------------------------------------------------------
# File:    src/data_loader.py
# Project: 100 Days of Python - Day 32 - Automated birthday wisher
# Purpose: Helper function to load a csv file containing
#          birthday information: name, email, year, month, day
#          and returns a list of dictionaries.
# -----------------------------------------------------------------------------
import csv
from pathlib import Path
from config import BIRTHDAYS_CSV

def load_birthdays_csv(filepath: Path = BIRTHDAYS_CSV) -> list[dict]:
    """
    Reads birthdays.csv and returns a list of dictionaries.
    :param filepath: Path to birthdays.csv
    :return: list of dictionaries containing name, email, year, month, day
    :rtype: list[dict]
    """
    try:
        with filepath.open("r", encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)
            return list(reader)

    except FileNotFoundError:
        print(f"Error: birthdays file not found at {filepath}")
        raise

