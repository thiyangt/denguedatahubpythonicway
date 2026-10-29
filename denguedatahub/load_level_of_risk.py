from pathlib import Path
import pandas as pd


def load_level_of_risk():
    """
    Load dengue risk-level information by country and region.

    The dataset contains 293 records with country names,
    dengue risk categories, regions, and last-accessed dates.

    Returns
    -------
    pandas.DataFrame
        Dengue risk information with columns:
        country, level_of_risk, region, last_accessed.

        The last_accessed column is parsed as datetime64[ns].
    """

    data_path = Path(__file__).parent / "data" / "level_of_risk.csv"

    df = pd.read_csv(
        data_path,
        dtype={
            "country": "object",
            "level_of_risk": "object",
            "region": "object"
        },
        parse_dates=["last_accessed"],
        encoding="utf-8"
    )

    return df
