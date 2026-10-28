
import pandas as pd

from denguedatahub import load_cdc_usa_dengue_infection


def test_load_cdc_usa_dengue_infection():
    df = load_cdc_usa_dengue_infection()

    assert isinstance(df, pd.DataFrame)
    assert not df.empty

    expected_columns = [
        "area",
        "year",
        "week",
        "dengue_cases",
        "dengue_like_illness",
        "severe_dengue"
    ]

    assert list(df.columns) == expected_columns

    assert "TOTAL" not in df["area"].values

    assert set(df["year"].unique()) == {
        2019, 2020, 2021, 2022
    }

    assert pd.api.types.is_numeric_dtype(df["year"])
    assert pd.api.types.is_numeric_dtype(df["week"])

    for col in [
        "dengue_cases",
        "dengue_like_illness",
        "severe_dengue"
    ]:
        assert pd.api.types.is_numeric_dtype(df[col])
