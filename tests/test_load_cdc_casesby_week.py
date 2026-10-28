
import pandas as pd

from denguedatahub import load_cdc_casesby_week


def test_load_cdc_casesby_week():
    df = load_cdc_casesby_week()

    assert isinstance(df, pd.DataFrame)
    assert not df.empty

    assert df.shape == (742, 4)

    expected_columns = [
        "Year",
        "Travel.status",
        "Week",
        "Reported.cases"
    ]

    assert list(df.columns) == expected_columns

    assert pd.api.types.is_integer_dtype(df["Year"])
    assert pd.api.types.is_integer_dtype(df["Week"])
    assert pd.api.types.is_numeric_dtype(df["Reported.cases"])
