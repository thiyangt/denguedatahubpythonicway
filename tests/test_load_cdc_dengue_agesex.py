
import pandas as pd

from denguedatahub import load_cdc_dengue_agesex


def test_load_cdc_dengue_agesex():
    df = load_cdc_dengue_agesex()

    assert isinstance(df, pd.DataFrame)
    assert not df.empty

    assert df.shape == (140, 5)

    expected_columns = [
        "Year",
        "Travel.status",
        "Age",
        "Male",
        "Female"
    ]

    assert list(df.columns) == expected_columns

    assert pd.api.types.is_numeric_dtype(df["Male"])
    assert pd.api.types.is_numeric_dtype(df["Female"])
