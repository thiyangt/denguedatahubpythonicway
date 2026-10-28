
import pandas as pd

from denguedatahub import load_cdc_dengue_casesbyjurisdiction


def test_load_cdc_dengue_casesbyjurisdiction():
    df = load_cdc_dengue_casesbyjurisdiction()

    assert isinstance(df, pd.DataFrame)
    assert not df.empty

    assert df.shape == (616, 6)

    expected_columns = [
        "Year",
        "Travel.status",
        "Jurisdiction",
        "Count",
        "Legend",
        "Notes"
    ]

    assert list(df.columns) == expected_columns

    assert pd.api.types.is_integer_dtype(df["Year"])
    assert pd.api.types.is_numeric_dtype(df["Count"])
