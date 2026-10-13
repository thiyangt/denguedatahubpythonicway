
from pathlib import Path

import pandas as pd


def load_sl_annual():
    """
    Load the annual dengue dataset for Sri Lanka.

    Returns
    -------
    pandas.DataFrame
        Annual dengue data for Sri Lanka.
    """

    data_path = Path(__file__).parent / "data" / "sl_annual.csv"

    return pd.read_csv(data_path)
