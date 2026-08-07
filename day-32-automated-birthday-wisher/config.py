# -----------------------------------------------------------------------------
# File:    src/config.py
# Project: 100 Days of Python - Day 32 - Automated birthday wisher
# Purpose: Defines project paths and file locations, and loads email
#          account credentials from environment variables via python-dotenv.
# -----------------------------------------------------------------------------
import os
from pathlib import Path
from dotenv import load_dotenv

# Paths
PROJECT_ROOT = Path(__file__).resolve().parents[0]
DATA_DIR = PROJECT_ROOT / "data"
BIRTHDAYS_CSV = DATA_DIR / "birthdays.csv"
BIRTHDAY_LETTER_TEMPLATES = DATA_DIR / "letter_templates"
BIRTHDAY_LETTER_1 = BIRTHDAY_LETTER_TEMPLATES / "letter_1.txt"
BIRTHDAY_LETTER_2 = BIRTHDAY_LETTER_TEMPLATES / "letter_2.txt"
BIRTHDAY_LETTER_3 = BIRTHDAY_LETTER_TEMPLATES / "letter_3.txt"
BIRTHDAY_LETTERS = [BIRTHDAY_LETTER_1, BIRTHDAY_LETTER_2, BIRTHDAY_LETTER_3]

# Template message placeholders
PLACEHOLDER_NAME = "[NAME]"



load_dotenv()

MY_EMAIL = os.getenv("MY_EMAIL")
MY_APP_PASSWORD = os.getenv("MY_APP_PASSWORD")
RECIPIENT_EMAIL = os.getenv("RECIPIENT_EMAIL")

