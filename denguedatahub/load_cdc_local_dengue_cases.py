
from pathlib import Path

import pandas as pd


def load_cdc_local_dengue_cases():
    """
    Load locally acquired dengue cases by year
    from the CDC dataset (2010-2023).

    Returns
    -------
    pandas.DataFrame
        Annual locally acquired dengue cases with columns:
        Year, Travel.status, Reported.cases.

        Data types:
        - Year: float64
        - Travel.status: string
        - Reported.cases: float64
    """

    data_path = (
        Path(__file__).resolve().parent
        / "data"
        / "cdc"
        / "Locally acquired dengue cases by year, 2010 - 2023.csv"
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
