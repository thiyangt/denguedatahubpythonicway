
import pandas as pd

from denguedatahub import load_sl_annual


def test_load_sl_annual():
    df = load_sl_annual()

    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    assert "year" in df.columns

def test_sl_annual_r_python_equivalence():
    """
    Compare every record, column, value, and data type
    against the original R dataset.

    Requires the DENGUEDATAHUB_SL_ANNUAL_RDA
    environment variable.
    """
    import os
    import pytest
    from pandas.testing import assert_frame_equal

    rda_path = os.environ.get("DENGUEDATAHUB_SL_ANNUAL_RDA")

    if not rda_path or not os.path.isfile(rda_path):
        pytest.skip("Original Sri Lanka annual RDA not available")

    pyreadr = pytest.importorskip("pyreadr")

    r_df = pyreadr.read_r(rda_path)["sl_annual"]
    python_df = load_sl_annual()

    assert_frame_equal(
        r_df.reset_index(drop=True),
        python_df.reset_index(drop=True),
        check_dtype=True,
        check_exact=True,
        check_frame_type=False,
    )
