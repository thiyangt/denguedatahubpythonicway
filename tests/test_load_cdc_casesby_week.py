
import os

import pandas as pd
import pytest
from pandas.testing import assert_frame_equal

from denguedatahub import load_cdc_casesby_week


def test_load_cdc_casesby_week():
    df = load_cdc_casesby_week()

    assert isinstance(df, pd.DataFrame)

    assert df.shape == (742, 4)

    assert df.columns.tolist() == [
        "Year",
        "Travel.status",
        "Week",
        "Reported.cases",
    ]

    # Verify original R data types
    assert df["Year"].dtype == "float64"
    assert df["Travel.status"].dtype == "object"
    assert df["Week"].dtype == "object"
    assert df["Reported.cases"].dtype == "float64"

    # Verify missing values
    assert df.isna().sum().sum() == 0

    # Verify leading zeros in Week
    assert df.iloc[0]["Week"] == "01"
    assert df.iloc[1]["Week"] == "02"

    # Verify year range
    assert df["Year"].min() == 2010
    assert df["Year"].max() == 2023


def test_cdc_casesby_week_r_python_equivalence():
    """
    Compare the complete Python dataset with the original R dataset.

    Requires DENGUEDATAHUB_CDC_CASESBY_WEEK_RDA.
    """
    rda_path = os.environ.get(
        "DENGUEDATAHUB_CDC_CASESBY_WEEK_RDA"
    )

    if not rda_path or not os.path.isfile(rda_path):
        pytest.skip("Original CDC cases-by-week RDA not available")

    pyreadr = pytest.importorskip("pyreadr")

    # Load original R dataset
    r_df = pyreadr.read_r(rda_path)["cdc_casesby_week"]

    # Load Python dataset
    python_df = load_cdc_casesby_week()

    # Compare all rows, columns, values, and data types
    assert_frame_equal(
        r_df.reset_index(drop=True),
        python_df.reset_index(drop=True),
        check_dtype=True,
        check_exact=True,
        check_frame_type=False,
    )
