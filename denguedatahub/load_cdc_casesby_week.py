
from pathlib import Path
import pandas as pd


def load_cdc_casesby_week():
    """
    Load CDC weekly dengue case data.

    Returns
    -------
    pandas.DataFrame
        CDC weekly dengue cases with standardized
        column names.
    """

    data_path = (
        Path(__file__).parent
        / "data"
        / "cdc"
        / "cdc_casesby_week.csv"
    )

    df = pd.read_csv(data_path)

    df = df.rename(
        columns={
            "Travel status": "Travel.status",
            "Reported cases": "Reported.cases"
        }
    )

    return df
