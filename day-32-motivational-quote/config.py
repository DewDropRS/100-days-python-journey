# -----------------------------------------------------------------------------
# File:    src/config.py
# Project: 100 Days of Python - Day 32 - Starter project
# Purpose: Defines project paths, email account credentials, and recipient settings.
# -----------------------------------------------------------------------------
import os
from pathlib import Path
from dotenv import load_dotenv

# Paths
PROJECT_ROOT = Path(__file__).resolve().parents[0]
DATA_DIR = PROJECT_ROOT / "data"
QUOTES_TXT = DATA_DIR / "quotes.txt"

load_dotenv()

MY_EMAIL = os.getenv("MY_EMAIL")
MY_APP_PASSWORD = os.getenv("MY_APP_PASSWORD")
RECIPIENT_EMAIL = os.getenv("RECIPIENT_EMAIL")