
from pathlib import Path
import pandas as pd


def load_cdc_dengue_countyyear():
    """
    Load the CDC dengue county-year dataset.

    Returns
    -------
    pandas.DataFrame
        CDC dengue county-year data.
    """

    data_path = (
        Path(__file__).parent
        / "data"
        / "cdc"
        / "cdc_dengue_countyyear.csv"
    )

    
    df = pd.read_csv(data_path)

    df = df.rename(
        columns={"Travel status": "Travel.status"}
    )

    return df

