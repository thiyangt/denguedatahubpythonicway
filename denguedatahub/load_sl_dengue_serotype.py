from pathlib import Path

import pandas as pd


def load_sl_dengue_serotype() -> pd.DataFrame:
    """
    Load historical Sri Lankan dengue serotype data.

    The dataset contains 13 reporting records from
    1965 to 2017.

    Returns
    -------
    pandas.DataFrame
        DataFrame containing:
        - reporting.year: float64
        - dengue.serotype: string (object dtype)

    Notes
    -----
    Preserves the original R dataset's column names,
    numerical values, serotype descriptions, and row order.
    """
    data_path = (
        Path(__file__).resolve().parent
        / "data"
        / "sl_dengue_serotype.csv"
    )

    return pd.read_csv(
        data_path,
        dtype={
            "reporting.year": "float64",
            "dengue.serotype": str,
        },
        encoding="utf-8",
    )
