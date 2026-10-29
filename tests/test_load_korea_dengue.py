
import os
import pandas as pd
import pytest

from pandas.testing import assert_frame_equal
from denguedatahub import load_korea_dengue


def test_load_korea_dengue():
    """Verify the Korea dataset structure and representative values."""

    df = load_korea_dengue()

    # Check DataFrame type and dimensions
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (33, 7)

    # Check column names and order
    assert df.columns.tolist() == [
        "Country",
        "Region",
        "2011",
        "2012",
        "2013",
        "2014",
        "2015"
    ]

    # Check unique values
    assert df["Country"].nunique() == 32
    assert df["Region"].nunique() == 6

    # Check that all columns contain strings
    for col in df.columns:
        assert df[col].dtype == object
        assert df[col].map(lambda x: isinstance(x, str)).all()

    # Check missing values
    assert df.isna().sum().sum() == 0

    # Check that literal "NA" values are preserved
    assert df.iloc[0]["2014"] == "NA"
    assert df.iloc[1]["2011"] == "NA"

    # Check representative records
    assert df.iloc[0]["Country"] == "Bangladesh"
    assert df.iloc[0]["Region"] == "Asia"
    assert df.iloc[0]["2011"] == "8"

    assert df.iloc[-1]["Country"] == "Unkown"
    assert df.iloc[-1]["2013"] == "1"


def test_korea_r_python_equivalence():
    """
    Compare the complete Python dataset with the original R dataset.

    This test runs when the DENGUEDATAHUB_KOREA_RDA
    environment variable points to the original R file.
    Otherwise, it is skipped.
    """

    rda_path = os.environ.get("DENGUEDATAHUB_KOREA_RDA")

    if not rda_path or not os.path.isfile(rda_path):
        pytest.skip("Original Korea R dataset not available")

    # Import pyreadr only when the R dataset is available
    pyreadr = pytest.importorskip("pyreadr")

    # Load original R dataset
    r_df = pyreadr.read_r(rda_path)["korea_dengue"]

    # Load Python dataset
    python_df = load_korea_dengue()

    # Compare every row, column, value, and data type
    assert_frame_equal(
        r_df.reset_index(drop=True),
        python_df.reset_index(drop=True),
        check_dtype=True,
        check_exact=True
    )
