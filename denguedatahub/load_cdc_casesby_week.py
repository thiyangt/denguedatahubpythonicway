
from pathlib import Path

import pandas as pd


def load_cdc_casesby_week():
    """
    Load CDC weekly dengue case data.

    Returns
    -------
    pandas.DataFrame
        CDC weekly dengue cases with columns:
        Year, Travel.status, Week, Reported.cases.

        Data types:
        - Year: float64
        - Travel.status: string
        - Week: string
        - Reported.cases: float64
    """

    data_path = (
        Path(__file__).resolve().parent
        / "data"
        / "cdc"
        / "cdc_casesby_week.csv"
    )

    df = pd.read_csv(
        data_path,
        dtype={
            "Year": "float64",
            "Travel status": str,
            "Week": str,
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
