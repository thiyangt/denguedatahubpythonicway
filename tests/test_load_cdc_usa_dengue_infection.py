
import os

import pandas as pd
import pytest
from pandas.testing import assert_frame_equal

from denguedatahub import load_cdc_usa_dengue_infection


def test_load_cdc_usa_dengue_infection():
    df = load_cdc_usa_dengue_infection()

    # Verify dimensions
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (9039, 6)

    # Verify column names and order
    assert df.columns.tolist() == [
        "area",
        "year",
        "week",
        "dengue_cases",
        "dengue_like_illness",
        "severe_dengue",
    ]

    # Verify data types
    expected_dtypes = {
        "area": "object",
        "year": "float64",
        "week": "float64",
        "dengue_cases": "float64",
        "dengue_like_illness": "object",
        "severe_dengue": "object",
    }

    for column, expected_dtype in expected_dtypes.items():
        assert str(df[column].dtype) == expected_dtype

    # Verify missing values
    assert df.isna().sum().to_dict() == {
        "area": 0,
        "year": 0,
        "week": 0,
        "dengue_cases": 8918,
        "dengue_like_illness": 9039,
        "severe_dengue": 9039,
    }

    # Verify years and filtering
    assert set(df["year"].unique()) == {
        2019, 2020, 2021, 2022
    }

    assert "TOTAL" not in df["area"].values

    # Verify original R row ordering
    assert df.iloc[0]["area"] == "NON-US RESIDENTS"
    assert df.iloc[0]["year"] == 2022
    assert df.iloc[0]["week"] == 2

    assert df.iloc[-1]["area"] == "MARYLAND"
    assert df.iloc[-1]["year"] == 2019
    assert df.iloc[-1]["week"] == 21


def test_cdc_usa_dengue_infection_r_python_equivalence():
    """
    Compare all records against the original R dataset.
    """

    rda_path = os.environ.get(
        "DENGUEDATAHUB_CDC_USA_DENGUE_INFECTION_RDA"
    )

    if not rda_path or not os.path.isfile(rda_path):
        pytest.skip("Original CDC USA RDA not available")

    pyreadr = pytest.importorskip("pyreadr")

    r_df = pyreadr.read_r(rda_path)[
        "cdc_usa_dengue_infection"
    ]

    python_df = load_cdc_usa_dengue_infection()

    assert_frame_equal(
        r_df.reset_index(drop=True),
        python_df.reset_index(drop=True),
        check_dtype=True,
        check_exact=True,
        check_frame_type=False,
    )
