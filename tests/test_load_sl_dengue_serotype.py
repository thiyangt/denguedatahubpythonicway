import pandas as pd

from denguedatahub.load_sl_dengue_serotype import (
    load_sl_dengue_serotype,
)


def test_load_sl_dengue_serotype():
    df = load_sl_dengue_serotype()

    # Verify dataset dimensions
    assert df.shape == (13, 2)

    # Verify column names and order
    assert list(df.columns) == [
        "reporting.year",
        "dengue.serotype",
    ]

    # Verify data types
    assert df["reporting.year"].dtype == "float64"
    assert df["dengue.serotype"].dtype == "object"

    # Verify missing values
    assert df.isna().sum().sum() == 0

    # Verify all reporting years in original order
    expected_years = [
        1965, 1968, 1978, 1980, 1990,
        1992, 1993, 1997, 2003, 2004,
        2006, 2009, 2017,
    ]
    assert df["reporting.year"].tolist() == expected_years

    # Verify all original serotype descriptions
    expected_serotypes = [
        "DENV-1, DENV-2",
        "DENV-1, DENV-2",
        "DENV-4",
        "DENV (IIIA)",
        "DENV (IIIA)",
        "DENV-4",
        "DENV (IIIB)",
        "DENV (IIIB)",
        "DENV (IIIB), DENV-4",
        "DENV-I, DENV (IIIB), DENV-4",
        "DENV-1",
        "DENV-1",
        "DENV-2",
    ]
    assert df["dengue.serotype"].tolist() == expected_serotypes
