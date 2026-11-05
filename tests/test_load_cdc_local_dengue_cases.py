
import os

import pandas as pd
import pytest
from pandas.testing import assert_frame_equal

from denguedatahub import load_cdc_local_dengue_cases


def test_load_cdc_local_dengue_cases():
    df = load_cdc_local_dengue_cases()

    # Verify DataFrame and dimensions
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (14, 3)

    # Verify column names and order
    assert df.columns.tolist() == [
        "Year",
        "Travel.status",
        "Reported.cases",
    ]

    # Verify original R data types
    assert df["Year"].dtype == "float64"
    assert df["Travel.status"].dtype == "object"
    assert df["Reported.cases"].dtype == "float64"

    # Verify missing values
    assert df.isna().sum().sum() == 0

    # Verify year range
    assert df["Year"].min() == 2010
    assert df["Year"].max() == 2023

    # Verify travel status
    assert (df["Travel.status"] == "Locally acquired").all()

    # Verify sample records
    assert df.iloc[0]["Reported.cases"] == 10969
    assert df.iloc[-1]["Reported.cases"] == 1462


def test_cdc_local_dengue_cases_r_python_equivalence():
    """
    Compare the complete Python dataset with
    the original R dataset.
    """

    rda_path = os.environ.get(
        "DENGUEDATAHUB_CDC_LOCAL_DENGUE_CASES_RDA"
    )

    if not rda_path or not os.path.isfile(rda_path):
        pytest.skip("Original CDC local dengue RDA not available")

    pyreadr = pytest.importorskip("pyreadr")

    # Load original R dataset
    r_df = pyreadr.read_r(rda_path)["cdc_local_dengue_cases"]

    # Load Python dataset
    python_df = load_cdc_local_dengue_cases()

    # Compare all rows, columns, data types,
    # missing values, and exact values
    assert_frame_equal(
        r_df.reset_index(drop=True),
        python_df.reset_index(drop=True),
        check_dtype=True,
        check_exact=True,
        check_frame_type=False,
    )
