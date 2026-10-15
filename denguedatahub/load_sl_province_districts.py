
from pathlib import Path
import pandas as pd


def load_sl_province_districts():
    """
    Load the Sri Lankan province-district mapping dataset.

    Returns
    -------
    pandas.DataFrame
        Province and district information for Sri Lanka.
    """

    data_path = (
        Path(__file__).parent
        / "data"
        / "sl_province_districts.csv"
    )

    return pd.read_csv(data_path)
