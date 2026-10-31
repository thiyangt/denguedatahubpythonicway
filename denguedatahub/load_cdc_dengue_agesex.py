
from pathlib import Path

import pandas as pd


def load_cdc_dengue_agesex():
    """
    Load CDC dengue data by age group and sex.

    Returns
    -------
    pandas.DataFrame
        CDC dengue age-sex dataset with columns:
        Year, Travel.status, Age, Male, Female.

        Data types:
        - Year: float64
        - Travel.status: string
        - Age: string
        - Male: float64
        - Female: float64
    """

    data_path = (
        Path(__file__).resolve().parent
        / "data"
        / "cdc"
        / "cdc_dengue_agesex.csv"
    )

    df = pd.read_csv(
        data_path,
        dtype={
            "Year": "float64",
            "Travel status": str,
            "Age group": str,
            "Male": "float64",
            "Female": "float64",
        },
    )

    df = df.rename(
        columns={
            "Travel status": "Travel.status",
            "Age group": "Age",
        }
    )

    return df
