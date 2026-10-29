import pandas as pd

from denguedatahub.load_level_of_risk import load_level_of_risk


def test_load_level_of_risk():
    df = load_level_of_risk()

    # Verify dimensions
    assert df.shape == (293, 4)

    # Verify column names and order
    assert list(df.columns) == [
        "country",
        "level_of_risk",
        "region",
        "last_accessed",
    ]

    # Verify missing values
    assert df.isna().sum().sum() == 0

    # Verify date type
    assert pd.api.types.is_datetime64_any_dtype(df["last_accessed"])

    # Verify dataset characteristics
    assert df["country"].nunique() == 162
    assert df["level_of_risk"].nunique() == 3
    assert df["region"].nunique() == 5
    assert df["last_accessed"].nunique() == 2

    # Verify the previously problematic encoded country name
    assert df.iloc[176]["country"] == "São Tomé and Príncipe"

    # Verify the associated record
    assert df.iloc[176]["level_of_risk"] == "Sporadic/Uncertain"
    assert df.iloc[176]["region"] == "Africa"
    assert df.iloc[176]["last_accessed"] == pd.Timestamp("2024-09-03")

    # Verify date boundaries
    assert df["last_accessed"].min() == pd.Timestamp("2023-01-16")
    assert df["last_accessed"].max() == pd.Timestamp("2024-09-03")
