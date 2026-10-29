
from pathlib import Path
import pandas as pd


def load_india_annual_data():
    """
    Load annual dengue cases and deaths data for India.

    The dataset contains state/union territory-wise dengue
    cases and deaths from 2017 to 2022.

    Returns
    -------
    pandas.DataFrame
        Annual dengue data for India with columns:
        area, type, year, additional_information, value.
    """

    data_path = Path(__file__).parent / "data" / "india_annual_data.csv"

    df = pd.read_csv(
        data_path,
        dtype={
            "area": "object",
            "type": "object",
            "year": "object",
            "additional_information": "object",
            "value": "float64"
        }
    )

    return df
