
from pathlib import Path

import pandas as pd


def load_americas_annual_data():
    """
    Load the annual dengue dataset for the Americas.

    Returns
    -------
    pandas.DataFrame
        A dataset containing 899,134 records and five columns:
        region, country, type, cases, and year.

        All columns preserve the original R character
        data types. Missing values in cases are retained.
    """

    data_path = (
        Path(__file__).resolve().parent
        / "data"
        / "americas_annual_data.csv"
    )

    return pd.read_csv(
        data_path,
        dtype=str,
        keep_default_na=False,
        na_values=[""],
    )
