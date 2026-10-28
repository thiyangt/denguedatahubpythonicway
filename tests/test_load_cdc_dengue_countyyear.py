
import pandas as pd

from denguedatahub import load_cdc_dengue_countyyear


def test_load_cdc_dengue_countyyear():
    df = load_cdc_dengue_countyyear()

    assert isinstance(df, pd.DataFrame)
    assert not df.empty

    expected_columns = [
        "FullGeoName",
        "Year",
        "Travel.status",
        "County",
        "Count",
        "Legend",
        "Notes"
    ]

    assert list(df.columns) == expected_columns

    assert df.shape[1] == 7
