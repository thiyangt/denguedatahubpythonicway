
from pathlib import Path

import pandas as pd


def load_srilanka_2020():
    """
    Load the prepared Sri Lankan weekly dengue dataset for 2020.

    The dataset reproduces the filtering operation in
    sri_lanka_2020.R, excluding records with week == 52.

    Returns
    -------
    pandas.DataFrame
        Weekly dengue cases by district for weeks 1–51 of 2020.
    """
    data_path = (
        Path(__file__).resolve().parent
        / "data"
        / "srilanka_2020.csv"
    )

    return pd.read_csv(data_path)

