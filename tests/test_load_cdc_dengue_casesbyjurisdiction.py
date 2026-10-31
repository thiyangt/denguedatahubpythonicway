
import os

import pandas as pd
import pytest
from pandas.testing import assert_frame_equal

from denguedatahub import load_cdc_dengue_casesbyjurisdiction


def test_load_cdc_dengue_casesbyjurisdiction():
    df = load_cdc_dengue_casesbyjurisdiction()

    # Verify DataFrame and dimensions
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (616, 6)

    # Verify column names and order
    assert df.columns.tolist() == [
        "Year",
        "Travel.status",
        "Jurisdiction",
        "Count",
        "Legend",
        "Notes",
    ]

    # Verify original R data types
    assert df["Year"].dtype == "float64"
    assert df["Travel.status"].dtype == "object"
    assert df["Jurisdiction"].dtype == "object"
    assert df["Count"].dtype == "float64"
    assert df["Legend"].dtype == "object"
    assert df["Notes"].dtype == "object"

    # Verify missing values
    assert df["Notes"].isna().sum() == 615
    assert df.drop(columns=["Notes"]).isna().sum().sum() == 0

    # Verify year range
    assert df["Year"].min() == 2010
    assert df["Year"].max() == 2023

    # Verify the single non-missing note
    notes_df = df[df["Notes"].notna()]

    assert len(notes_df) == 1
    assert notes_df.iloc[0]["Year"] == 2023
    assert notes_df.iloc[0]["Jurisdiction"] == "TX"
    assert notes_df.iloc[0]["Count"] == 79


def test_cdc_dengue_casesbyjurisdiction_r_python_equivalence():
    """
    Compare the complete Python dataset against
    the original R dataset.
    """

    rda_path = os.environ.get(
        "DENGUEDATAHUB_CDC_CASESBYJURISDICTION_RDA"
    )

    if not rda_path or not os.path.isfile(rda_path):
        pytest.skip("Original CDC jurisdiction RDA not available")

    pyreadr = pytest.importorskip("pyreadr")

    # Load original R dataset
    r_df = pyreadr.read_r(rda_path)[
        "cdc_dengue_casesbyjurisdiction"
    ]

    # Load Python dataset
    python_df = load_cdc_dengue_casesbyjurisdiction()

    # Compare all records, columns, data types,
    # missing values, and exact values
    assert_frame_equal(
        r_df.reset_index(drop=True),
        python_df.reset_index(drop=True),
        check_dtype=True,
        check_exact=True,
        check_frame_type=False,
    )
