
from pathlib import Path

import pandas as pd


def load_cdc_dengue_casesbyjurisdiction():
    """
    Load CDC dengue cases by jurisdiction.

    Returns
    -------
    pandas.DataFrame
        CDC dengue cases by jurisdiction with columns:
        Year, Travel.status, Jurisdiction,
        Count, Legend, Notes.

        Data types:
        - Year: float64
        - Travel.status: string
        - Jurisdiction: string
        - Count: float64
        - Legend: string
        - Notes: string (with missing values)
    """

    data_path = (
        Path(__file__).resolve().parent
        / "data"
        / "cdc"
        / "cdc_dengue_casesbyjurisdiction.csv"
    )

    df = pd.read_csv(
        data_path,
        dtype={
            "Year": "float64",
            "Travel status": str,
            "Jurisdiction": str,
            "Count": "float64",
            "Legend": str,
            "Notes": str,
        },
    )

    df = df.rename(
        columns={
            "Travel status": "Travel.status",
        }
    )

    return df
