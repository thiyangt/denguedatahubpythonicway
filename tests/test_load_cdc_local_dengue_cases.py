
import pandas as pd

from denguedatahub import load_cdc_local_dengue_cases


def test_load_cdc_local_dengue_cases():
    df = load_cdc_local_dengue_cases()

    assert isinstance(df, pd.DataFrame)
    assert not df.empty

    assert df.shape == (14, 3)

    expected_columns = [
        "Year",
        "Travel.status",
        "Reported.cases"
    ]

    assert list(df.columns) == expected_columns

    assert pd.api.types.is_integer_dtype(df["Year"])
    assert pd.api.types.is_numeric_dtype(df["Reported.cases"])

    assert df["Year"].min() == 2010
    assert df["Year"].max() == 2023

    assert (df["Travel.status"] == "Locally acquired").all()
