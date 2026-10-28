
from pathlib import Path
import pandas as pd


def load_cdc_dengue_agesex():
    """
    Load CDC dengue data by age group and sex.

    Returns
    -------
    pandas.DataFrame
        CDC dengue age-sex dataset.
    """

    data_path = (
        Path(__file__).parent
        / "data"
        / "cdc"
        / "cdc_dengue_agesex.csv"
    )

    df = pd.read_csv(data_path)

    df = df.rename(
        columns={
            "Travel status": "Travel.status",
            "Age group": "Age"
        }
    )

    return df
