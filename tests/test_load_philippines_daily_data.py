import pandas as pd

from denguedatahub.load_philippines_daily_data import (
    load_philippines_daily_data,
)


def test_load_philippines_daily_data():
    df = load_philippines_daily_data()

    # Verify dataset dimensions
    assert df.shape == (32701, 5)

    # Verify column names and order
    assert list(df.columns) == [
        "location",
        "affected_and_infected",
        "affected_and_killed",
        "date",
        "region",
    ]

    # Verify all columns contain character data
    assert all(df[column].dtype == object for column in df.columns)

    # Verify missing values
    assert df.isna().sum().to_dict() == {
        "location": 0,
        "affected_and_infected": 0,
        "affected_and_killed": 1,
        "date": 0,
        "region": 0,
    }

    # Verify the first record
    assert df.iloc[0].to_dict() == {
        "location": "ALBAY",
        "affected_and_infected": "15",
        "affected_and_killed": "0",
        "date": "1/10/2016",
        "region": "REGION V-BICOL REGION",
    }

    # Verify the last record
    assert df.iloc[-1].to_dict() == {
        "location": "VALENZUELA CITY",
        "affected_and_infected": "0",
        "affected_and_killed": "19",
        "date": "11/1/2020",
        "region": "NATIONAL CAPITAL REGION",
    }

    # Verify the single missing value is preserved
    assert df["affected_and_killed"].isna().sum() == 1

    # Verify the dates remain strings
    assert isinstance(df.iloc[0]["date"], str)
