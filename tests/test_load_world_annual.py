"""Tests for the world annual dengue dataset loader."""

import pandas as pd

from denguedatahub.load_world_annual import load_world_annual


def test_load_world_annual():
    df = load_world_annual()

    # 1. Verify dimensions
    assert df.shape == (2773284, 10)

    # 2. Verify column names and order
    expected_columns = [
        "long",
        "lat",
        "group",
        "order",
        "region",
        "subregion",
        "code",
        "year",
        "incidence",
        "dengue.present",
    ]

    assert df.columns.tolist() == expected_columns

    # 3. Verify numeric data types
    for column in [
        "long", "lat", "group", "year", "incidence"
    ]:
        assert df[column].dtype == "float64"

    assert df["order"].dtype == pd.Int64Dtype()

    # 4. Verify missing values
    expected_missing = {
        "long": 900,
        "lat": 900,
        "group": 900,
        "order": 900,
        "region": 0,
        "subregion": 1783783,
        "code": 7854,
        "year": 7164,
        "incidence": 7164,
        "dengue.present": 7164,
    }

    assert df.isna().sum().to_dict() == expected_missing

    # 5. Verify first record
    assert df.iloc[0]["region"] == "Aruba"
    assert df.iloc[0]["order"] == 1
    assert pd.isna(df.iloc[0]["incidence"])

    # 6. Verify last record
    assert (
        df.iloc[-1]["region"]
        == "World Bank Upper Middle Income"
    )
    assert df.iloc[-1]["year"] == 2019
    assert df.iloc[-1]["incidence"] == 11684260
    assert df.iloc[-1]["dengue.present"] == "yes"

    # 7. Verify original whitespace is preserved
    assert (df["subregion"] == "Ko Tarutao ").any()
    assert (df["subregion"] == " British").any()
    assert (df["subregion"] == " US").any()
