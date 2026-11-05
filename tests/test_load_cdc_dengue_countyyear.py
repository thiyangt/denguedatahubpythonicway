
import os

import pandas as pd
import pytest
from pandas.testing import assert_frame_equal

from denguedatahub import load_cdc_dengue_countyyear


def test_load_cdc_dengue_countyyear():
    df = load_cdc_dengue_countyyear()

    # Verify DataFrame and dimensions
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (3900, 7)

    # Verify original R column names and order
    assert df.columns.tolist() == [
        "FullGeoName",
        "Year",
        "Travel.status",
        "County",
        "Legend",
        "Notes",
        None,
    ]

    # Verify original R data types
    assert df["FullGeoName"].dtype == "object"
    assert df["Year"].dtype == "float64"
    assert df["Travel.status"].dtype == "object"
    assert df["County"].dtype == "object"
    assert df["Legend"].dtype == "object"
    assert df["Notes"].dtype == "object"
    assert df[None].dtype == "object"

    # Verify missing values
    assert df["FullGeoName"].isna().sum() == 6
    assert df.drop(columns=["FullGeoName"]).isna().sum().sum() == 0

    # Verify county identifiers retain leading zeros
    assert df.iloc[0]["County"] == "01003"
    assert df.iloc[1]["County"] == "01073"

    # Verify year range
    assert df["Year"].min() == 2010
    assert df["Year"].max() == 2023


def test_cdc_dengue_countyyear_r_python_equivalence():
    """
    Compare the complete Python dataset with
    the original R dataset.
    """

    rda_path = os.environ.get(
        "DENGUEDATAHUB_CDC_DENGUE_COUNTYYEAR_RDA"
    )

    if not rda_path or not os.path.isfile(rda_path):
        pytest.skip("Original CDC county-year RDA not available")

    pyreadr = pytest.importorskip("pyreadr")

    # Load original R dataset
    r_df = pyreadr.read_r(rda_path)["cdc_dengue_countyyear"]

    # Load Python dataset
    python_df = load_cdc_dengue_countyyear()

    # Compare all records, columns, data types,
    # missing values, and exact values
    assert_frame_equal(
        r_df.reset_index(drop=True),
        python_df.reset_index(drop=True),
        check_dtype=True,
        check_exact=True,
        check_frame_type=False,
    )
