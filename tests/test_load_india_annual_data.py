
import os
import pandas as pd
import pytest

from pandas.testing import assert_frame_equal
from denguedatahub import load_india_annual_data


def test_load_india_annual_data():
    """Verify the India dataset structure and representative values."""

    df = load_india_annual_data()

    # Check DataFrame type and dimensions
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (432, 5)

    # Check column names and order
    assert df.columns.tolist() == [
        "area",
        "type",
        "year",
        "additional_information",
        "value"
    ]

    # Check unique values
    assert df["area"].nunique() == 36
    assert set(df["type"]) == {"cases", "deaths"}
    assert set(df["year"]) == {
        "2017", "2018", "2019",
        "2020", "2021", "2022"
    }

    # Check missing values
    assert df["value"].isna().sum() == 4
    assert df["additional_information"].isna().sum() == 360

    # Check data types
    assert df["year"].dtype == object
    assert df["value"].dtype == "float64"

    # Check representative records
    assert df.iloc[0]["area"] == "Andhra Pradesh"
    assert df.iloc[0]["value"] == 4925.0

    assert df.iloc[-1]["area"] == "Puduchery"
    assert df.iloc[-1]["value"] == 1.0


def test_india_r_python_equivalence():
    """
    Compare the complete Python dataset with the original R dataset.

    This test runs when the DENGUEDATAHUB_INDIA_RDA
    environment variable points to the original R file.
    Otherwise, it is skipped.
    """

    rda_path = os.environ.get("DENGUEDATAHUB_INDIA_RDA")

    if not rda_path or not os.path.isfile(rda_path):
        pytest.skip("Original India R dataset not available")

    # Import pyreadr only when R data is available
    pyreadr = pytest.importorskip("pyreadr")

    # Load original R dataset
    r_df = pyreadr.read_r(rda_path)["india_annual_data"]

    # Load Python dataset
    python_df = load_india_annual_data()

    # Compare all rows, columns, values, and data types
    assert_frame_equal(
        r_df.reset_index(drop=True),
        python_df.reset_index(drop=True),
        check_dtype=True,
        check_exact=True
    )
