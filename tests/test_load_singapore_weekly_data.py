import pandas as pd

from denguedatahub.load_singapore_weekly_data import (
    load_singapore_weekly_data,
)


def test_load_singapore_weekly_data():
    df = load_singapore_weekly_data()

    # Verify dataset dimensions
    assert df.shape == (272, 3)

    # Verify column names and order
    assert list(df.columns) == ["year", "week", "cases"]

    # Verify data types
    assert df["year"].dtype == "float64"
    assert df["week"].dtype == "int64"
    assert df["cases"].dtype == "float64"

    # Verify missing values
    assert df["year"].isna().sum() == 0
    assert df["week"].isna().sum() == 0
    assert df["cases"].isna().sum() == 3

    # Verify year range
    assert df["year"].min() == 2018
    assert df["year"].max() == 2023

    # Verify first record
    assert df.iloc[0]["year"] == 2018
    assert df.iloc[0]["week"] == 0
    assert df.iloc[0]["cases"] == 54

    # Verify last record
    assert df.iloc[-1]["year"] == 2023
    assert df.iloc[-1]["week"] == 8
    assert df.iloc[-1]["cases"] == 112

    # Verify all week values are within original range
    assert df["week"].between(0, 52).all()
