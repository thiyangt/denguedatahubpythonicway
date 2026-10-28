
import pandas as pd

from denguedatahub import load_americas_annual_data


def test_load_americas_annual_data():
    df = load_americas_annual_data()

    assert isinstance(df, pd.DataFrame)
    assert not df.empty

    assert list(df.columns) == [
        "region", "country", "year", "type", "cases"
    ]

    assert len(df) == 52 * 220

    assert df["year"].min() == 1980
    assert df["year"].max() == 2023

    assert df["type"].nunique() == 5
