# -----------------------------------------------------------------------------
# File:    src/data_loader.py
# Project: 100 Days of Python - Day 32 - Starter project
# Purpose: Two functions to load data to a list and to select a random quote from that list.
# -----------------------------------------------------------------------------
# Third party — installed packages
import random

import pandas as pd
from pathlib import Path

# Local — project modules
from config import (
    QUOTES_TXT
)

def load_quotes(filepath: Path = QUOTES_TXT) -> list[str]:
    """
    Reads quotes.txt and returns a list, one quote per line.
    :param filepath: Path to quotes.txt
    :return: List of quote strings; blank lines are skipped.
    :rtype: list[str]
    """
    try:
        with filepath.open("r", encoding="utf-8") as f:
            #list comprehension: Iterates over the file object line by line. Ignores blank lines.
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Error: quotes file not found at {filepath}")
        raise

def get_random_quote(quotes: list[str]) -> str:
    """
    Returns one random quote from a list.
    :param quotes:
    :return: str
    """
    try:
        return random.choice(quotes)
    except IndexError:
        print("Error: no quotes available to select from.")
        raise

if __name__=="__main__":
    quotes = load_quotes()
    print(get_random_quote(quotes))
