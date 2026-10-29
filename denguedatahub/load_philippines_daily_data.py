from pathlib import Path
import pandas as pd


def load_philippines_daily_data():
    """
    Load dengue infection and death records for the Philippines.

    The dataset contains 32,701 records with location,
    infection counts, death counts, dates, and regions.

    Returns
    -------
    pandas.DataFrame
        Philippines dengue data with columns:
        location, affected_and_infected, affected_and_killed,
        date, region.

        All non-missing values are preserved as strings.
        Missing values are represented as NaN.
    """

    data_path = Path(__file__).parent / "data" / "philippines_daily_data.csv"

    df = pd.read_csv(
        data_path,
        dtype=str,
        keep_default_na=False,
        na_values=[""],
        encoding="utf-8"
    )

    return df
