
import pandas as pd

from denguedatahub import load_sl_province_districts


def test_load_sl_province_districts():
    df = load_sl_province_districts()

    assert isinstance(df, pd.DataFrame)
    assert not df.empty

    assert len(df) == 26

    assert list(df.columns) == ["province", "district"]

    assert df["province"].nunique() == 9

    assert "Colombo" in df["district"].values
    assert "Kalmune" in df["district"].values


def test_sl_province_districts_r_python_equivalence():
    """
    Compare the complete Python dataset with the original R dataset.

    Requires DENGUEDATAHUB_SL_PROVINCE_DISTRICTS_RDA
    to point to the original RDA file.
    """
    import os
    import pytest
    from pandas.testing import assert_frame_equal

    rda_path = os.environ.get(
        "DENGUEDATAHUB_SL_PROVINCE_DISTRICTS_RDA"
    )

    if not rda_path or not os.path.isfile(rda_path):
        pytest.skip("Original province-district RDA not available")

    pyreadr = pytest.importorskip("pyreadr")

    # Read the original R dataset
    r_df = pyreadr.read_r(rda_path)["sl_province_districts"]

    # Read the Python dataset
    python_df = load_sl_province_districts()

    # Compare all records, columns, values, and data types
    assert_frame_equal(
        r_df.reset_index(drop=True),
        python_df.reset_index(drop=True),
        check_dtype=True,
        check_exact=True,
        check_frame_type=False,
    )
