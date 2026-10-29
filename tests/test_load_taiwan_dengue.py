import pandas as pd

from denguedatahub.load_taiwan_dengue import load_taiwan_dengue


def test_load_taiwan_dengue():
    df = load_taiwan_dengue()

    # Verify dimensions
    assert df.shape == (37, 3)

    # Verify column names and order
    assert list(df.columns) == [
        "year",
        "indigenous.dengue",
        "imported.dengue",
    ]

    # Verify data types
    assert df["year"].dtype == "float64"
    assert df["indigenous.dengue"].dtype == "float64"
    assert df["imported.dengue"].dtype == "float64"

    # Verify missing values
    assert df.isna().sum().sum() == 0

    # Verify complete year sequence
    assert df["year"].tolist() == list(range(1987, 2024))

    # Verify first record
    assert df.iloc[0]["year"] == 1987
    assert df.iloc[0]["indigenous.dengue"] == 527
    assert df.iloc[0]["imported.dengue"] == 0

    # Verify selected records
    row_2021 = df.loc[df["year"] == 2021].iloc[0]
    assert row_2021["indigenous.dengue"] == 0
    assert row_2021["imported.dengue"] == 12

    # Verify last record
    assert df.iloc[-1]["year"] == 2023
    assert df.iloc[-1]["indigenous.dengue"] == 26429
    assert df.iloc[-1]["imported.dengue"] == 277

    # Verify no negative case counts
    assert (df["indigenous.dengue"] >= 0).all()
    assert (df["imported.dengue"] >= 0).all()
