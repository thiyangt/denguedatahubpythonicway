
import os

import pandas as pd
import pytest
from pandas.testing import assert_frame_equal

from denguedatahub import load_cdc_dengue_agesex


def test_load_cdc_dengue_agesex():
    df = load_cdc_dengue_agesex()

    # Verify DataFrame and dimensions
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (140, 5)

    # Verify column names and order
    assert df.columns.tolist() == [
        "Year",
        "Travel.status",
        "Age",
        "Male",
        "Female",
    ]

    # Verify original R data types
    assert df["Year"].dtype == "float64"
    assert df["Travel.status"].dtype == "object"
    assert df["Age"].dtype == "object"
    assert df["Male"].dtype == "float64"
    assert df["Female"].dtype == "float64"

    # Verify missing values
    assert df.isna().sum().sum() == 0

    # Verify year range
    assert df["Year"].min() == 2010
    assert df["Year"].max() == 2023

    # Verify important age-group labels
    assert "< 1" in df["Age"].values
    assert "70+" in df["Age"].values
    assert "Unknown" in df["Age"].values


def test_cdc_dengue_agesex_r_python_equivalence():
    """
    Compare the complete Python dataset against
    the original R dataset.
    """

    rda_path = os.environ.get(
        "DENGUEDATAHUB_CDC_DENGUE_AGESEX_RDA"
    )

    if not rda_path or not os.path.isfile(rda_path):
        pytest.skip("Original CDC age-sex RDA not available")

    pyreadr = pytest.importorskip("pyreadr")

    # Load original R dataset
    r_df = pyreadr.read_r(rda_path)["cdc_dengue_agesex"]

    # Load Python dataset
    python_df = load_cdc_dengue_agesex()

    # Compare all records, column names,
    # data types, missing values, and values
    assert_frame_equal(
        r_df.reset_index(drop=True),
        python_df.reset_index(drop=True),
        check_dtype=True,
        check_exact=True,
        check_frame_type=False,
    )
