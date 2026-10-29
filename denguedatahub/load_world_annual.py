"""Load the world annual dengue dataset."""

from pathlib import Path

import pandas as pd


def load_world_annual():
    """
    Load annual worldwide dengue data with geographical information.

    Returns
    -------
    pandas.DataFrame
        Original world_annual dataset containing 2,773,284
        records and 10 columns.

    Notes
    -----
    Preserves original column names, data types, missing values,
    whitespace in text fields, and row order.
    """
    data_path = (
        Path(__file__).resolve().parent
        / "data"
        / "world_annual.csv.gz"
    )

    column_types = {
        "long": "float64",
        "lat": "float64",
        "group": "float64",
        "order": "Int64",
        "region": str,
        "subregion": str,
        "code": str,
        "year": "float64",
        "incidence": "float64",
        "dengue.present": str,
    }

    return pd.read_csv(
        data_path,
        dtype=column_types,
        keep_default_na=False,
        na_values=["NA"],
        skipinitialspace=False,
        compression="gzip",
    )
