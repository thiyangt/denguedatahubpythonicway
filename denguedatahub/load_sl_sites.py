
from pathlib import Path

import pandas as pd


def load_sl_sites():
    """
    Load the Sri Lanka dengue reporting sites dataset.

    Returns
    -------
    pandas.DataFrame
        Sri Lanka dengue reporting sites data.
    """

    data_path = Path(__file__).parent / "data" / "sl_sites.csv"

    return pd.read_csv(data_path)
