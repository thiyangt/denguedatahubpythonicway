
from pathlib import Path
import pandas as pd


def load_korea_dengue():
    """
    Load imported dengue cases data for Korea.

    The dataset contains imported dengue cases
    categorized by country and region for 2011–2015.

    Returns
    -------
    pandas.DataFrame
        Imported dengue data with columns:
        Country, Region, 2011, 2012, 2013, 2014, 2015.

        All columns are strings, and literal "NA"
        values are preserved as in the original R dataset.
    """

    data_path = Path(__file__).parent / "data" / "korea_dengue.csv"

    df = pd.read_csv(
        data_path,
        dtype=str,
        keep_default_na=False
    )

    return df
