from pathlib import Path

import pandas as pd


def load_taiwan_dengue() -> pd.DataFrame:
    """
    Load annual dengue case data for Taiwan.

    The dataset contains 37 annual observations
    covering 1987 to 2023.

    Returns
    -------
    pandas.DataFrame
        DataFrame containing:
        - year: float64
        - indigenous.dengue: float64
        - imported.dengue: float64

    Notes
    -----
    Preserves the original R dataset's column names,
    numerical values, data types, and row order.
    """
    data_path = (
        Path(__file__).resolve().parent
        / "data"
        / "taiwan_dengue.csv"
    )

    return pd.read_csv(
        data_path,
        dtype={
            "year": "float64",
            "indigenous.dengue": "float64",
            "imported.dengue": "float64",
        },
        encoding="utf-8",
    )
