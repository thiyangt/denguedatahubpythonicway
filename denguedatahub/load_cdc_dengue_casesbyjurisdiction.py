
from pathlib import Path
import pandas as pd


def load_cdc_dengue_casesbyjurisdiction():
    """
    Load CDC dengue cases by jurisdiction.

    Returns
    -------
    pandas.DataFrame
        CDC dengue cases by jurisdiction with
        standardized column names.
    """

    data_path = (
        Path(__file__).parent
        / "data"
        / "cdc"
        / "cdc_dengue_casesbyjurisdiction.csv"
    )

    df = pd.read_csv(data_path)

    df = df.rename(
        columns={
            "Travel status": "Travel.status"
        }
    )

    return df
