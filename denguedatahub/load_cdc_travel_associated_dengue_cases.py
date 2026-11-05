
from pathlib import Path

import pandas as pd


def load_cdc_travel_associated_dengue_cases():
    """
    Load CDC travel-associated dengue cases by year
    (2010-2023).

    Returns
    -------
    pandas.DataFrame
        Annual travel-associated dengue cases with
        column names and data types matching the
        original R dataset.
    """

    data_path = (
        Path(__file__).resolve().parent
        / "data"
        / "cdc"
        / "Travel associated dengue cases by year, 2010 - 2023.csv"
    )

    df = pd.read_csv(
        data_path,
        dtype={
            "Year": "float64",
            "Travel status": str,
            "Reported cases": "float64",
        },
    )

    df = df.rename(
        columns={
            "Travel status": "Travel.status",
            "Reported cases": "Reported.cases",
        }
    )

    return df
