
from pathlib import Path
import pandas as pd


def load_china_annual_data():
    """
    Load annual dengue data for China.

    Returns
    -------
    pandas.DataFrame
        Annual dengue data for China, with year
        represented as an integer.
    """

    data_path = Path(__file__).parent / "data" / "china.csv"

    # df = pd.read_csv(data_path)
    df = pd.read_csv(data_path, thousands=",")

    df["year"] = df["year"].astype(int)

    return df
