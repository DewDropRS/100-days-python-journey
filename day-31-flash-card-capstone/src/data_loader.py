# ============================================================
# data_loader.py
# Handles loading of flash card CSV data files into a pandas
# DataFrame for use by the FlashCardApp class.
# ============================================================
import pandas as pd


def load_flash_card_data(filepath):
    """
    Loads a CSV file into a pandas DataFrame.

    :param filepath: path to the CSV file to load
    :return: DataFrame containing the CSV data (pd.DataFrame)
    """

    # Load raw data as-is
    df = pd.read_csv(filepath)
    return df