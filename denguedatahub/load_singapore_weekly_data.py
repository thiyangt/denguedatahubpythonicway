from pathlib import Path

import pandas as pd


def load_singapore_weekly_data() -> pd.DataFrame:
    """
    Load Singapore weekly dengue case data.

    The dataset contains 272 observations from 2018 to 2023.

    Returns
    -------
    pandas.DataFrame
        DataFrame with the following columns:
        - year: float64
        - week: int64
        - cases: float64

    Notes
    -----
    Preserves the original R dataset's column order,
    numerical types, row order, and missing values.
    """
    data_path = (
        Path(__file__).resolve().parent
        / "data"
        / "singapore_weekly_data.csv"
    )

    return pd.read_csv(
        data_path,
        dtype={
            "year": "float64",
            "week": "int64",
            "cases": "float64",
        },
        encoding="utf-8",
    )
