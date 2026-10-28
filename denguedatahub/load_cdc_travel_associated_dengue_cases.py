
from pathlib import Path
import pandas as pd


def load_cdc_travel_associated_dengue_cases():
    """
    Load CDC travel-associated dengue cases
    by year (2010–2023).

    Returns
    -------
    pandas.DataFrame
        Annual travel-associated dengue cases
        with standardized column names.
    """

    data_path = (
        Path(__file__).parent
        / "data"
        / "cdc"
        / "Travel associated dengue cases by year, 2010 - 2023.csv"
    )

    df = pd.read_csv(data_path)

    df = df.rename(
        columns={
            "Travel status": "Travel.status",
            "Reported cases": "Reported.cases"
        }
    )

    return df
