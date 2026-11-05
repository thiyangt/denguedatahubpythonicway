
from pathlib import Path

import pandas as pd


def load_cdc_dengue_countyyear():
    """
    Load CDC dengue county-year data.

    Reproduces the original R dataset structure,
    including its unusual final column names.

    Returns
    -------
    pandas.DataFrame
        CDC dengue county-year dataset.
    """

    data_path = (
        Path(__file__).resolve().parent
        / "data"
        / "cdc"
        / "cdc_dengue_countyyear.csv"
    )

    df = pd.read_csv(
        data_path,
        dtype={
            "FullGeoName": str,
            "Year": "float64",
            "Travel status": str,
            "County": str,
            "Count": str,
            "Legend": str,
            "Notes": str,
        },
    )

    # Match the original R column names
    df.columns = [
        "FullGeoName",
        "Year",
        "Travel.status",
        "County",
        "Legend",
        "Notes",
        None,
    ]

    return df
