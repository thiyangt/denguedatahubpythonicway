
from pathlib import Path

import pandas as pd


def load_srilanka_weekly_data():
    """
    Load Sri Lankan weekly dengue case data.

    Returns
    -------
    pandas.DataFrame
        Weekly dengue cases by district, with columns:
        year, week, start.date, end.date, district, cases.
    """
    data_path = Path(__file__).resolve().parent / "data" / "srilanka_weekly_data.csv"

    return pd.read_csv(data_path)
