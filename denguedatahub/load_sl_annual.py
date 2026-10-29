from pathlib import Path

import pandas as pd


def load_sl_annual():
    """
    Load the annual dengue dataset for Sri Lanka.

    Returns
    -------
    pandas.DataFrame
        Annual dengue data for Sri Lanka.

        Contains 35 records and 3 columns:
        year, dengue.cases, epidemic.

        All columns are float64, matching the
        original R dataset's numeric types.
    """

    data_path = Path(__file__).parent / "data" / "sl_annual.csv"

    return pd.read_csv(
        data_path,
        dtype={
            "year": "float64",
            "dengue.cases": "float64",
            "epidemic": "float64",
        },
    )
