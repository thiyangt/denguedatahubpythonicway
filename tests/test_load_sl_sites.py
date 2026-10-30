
import pandas as pd

from denguedatahub import load_sl_sites


def test_load_sl_sites():
    df = load_sl_sites()

    assert isinstance(df, pd.DataFrame)
    assert not df.empty


def test_sl_sites_r_python_equivalence():
    """
    Verify complete equivalence with the original R dataset.

    Requires DENGUEDATAHUB_SL_SITES_RDA to point
    to the original sl_sites.rda file.
    """
    import os
    import pytest
    from pandas.testing import assert_frame_equal

    rda_path = os.environ.get("DENGUEDATAHUB_SL_SITES_RDA")

    if not rda_path or not os.path.isfile(rda_path):
        pytest.skip("Original Sri Lanka sites RDA not available")

    pyreadr = pytest.importorskip("pyreadr")

    # Load original R dataset
    r_df = pyreadr.read_r(rda_path)["sl_sites"]

    # Load converted Python dataset
    python_df = load_sl_sites()

    # Verify dimensions, column names, values,
    # data types, and original row order
    assert_frame_equal(
        r_df.reset_index(drop=True),
        python_df.reset_index(drop=True),
        check_dtype=True,
        check_exact=True,
        check_frame_type=False,
    )
