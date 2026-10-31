
import os

import pandas as pd
import pytest
from pandas.testing import assert_frame_equal

from denguedatahub import load_americas_annual_data


def test_load_americas_annual_data():
    df = load_americas_annual_data()

    assert isinstance(df, pd.DataFrame)

    assert df.shape == (899134, 5)

    assert df.columns.tolist() == [
        "region",
        "country",
        "type",
        "cases",
        "year",
    ]

    # All columns must contain character data
    assert all(dtype == object for dtype in df.dtypes)

    # Missing values must match the original R dataset
    assert df["cases"].isna().sum() == 2309

    for column in ["region", "country", "type", "year"]:
        assert df[column].notna().all()

    # Check original year range
    assert df["year"].astype(int).min() == 1980
    assert df["year"].astype(int).max() == 2023


def test_americas_annual_data_r_python_equivalence():
    """
    Compare all records, columns, data types, and values
    against the original R dataset.

    Requires DENGUEDATAHUB_AMERICAS_RDA.
    """
    rda_path = os.environ.get(
        "DENGUEDATAHUB_AMERICAS_RDA"
    )

    if not rda_path or not os.path.isfile(rda_path):
        pytest.skip("Original Americas annual RDA not available")

    pyreadr = pytest.importorskip("pyreadr")

    # Load original R dataset
    r_df = pyreadr.read_r(rda_path)["americas_annual_data"]

    # Load Python dataset
    python_df = load_americas_annual_data()

    # Compare every row, column, value, and data type
    assert_frame_equal(
        r_df.reset_index(drop=True),
        python_df.reset_index(drop=True),
        check_dtype=True,
        check_exact=True,
        check_frame_type=False,
    )
