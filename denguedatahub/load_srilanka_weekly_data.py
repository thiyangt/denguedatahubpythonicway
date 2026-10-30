
from pathlib import Path

import pandas as pd


def load_srilanka_weekly_data():
    """
    Load Sri Lankan weekly dengue case data.

    Returns
    -------
    pandas.DataFrame
        Weekly dengue cases by district.

        Columns:
        - year: float64
        - week: float64
        - start.date: string
        - end.date: string
        - district: string
        - cases: float64
    """

    data_path = (
        Path(__file__).resolve().parent
        / "data"
        / "srilanka_weekly_data.csv"
    )

    return pd.read_csv(
        data_path,
        dtype={
            "year": "float64",
            "week": "float64",
            "start.date": str,
            "end.date": str,
            "district": str,
            "cases": "float64",
        },
    )
