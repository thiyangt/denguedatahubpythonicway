
import pandas as pd

from denguedatahub.load_srilanka_weekly_data import load_srilanka_weekly_data


def test_load_srilanka_weekly_data():
    df = load_srilanka_weekly_data()

    assert isinstance(df, pd.DataFrame)

    assert df.shape == (26311, 6)

    assert df.columns.tolist() == [
        "year",
        "week",
        "start.date",
        "end.date",
        "district",
        "cases",
    ]

    assert df["year"].notna().all()
    assert df["week"].notna().all()
    assert df["district"].notna().all()

    assert df.iloc[0]["year"] == 2006
    assert df.iloc[0]["week"] == 52
    assert df.iloc[0]["district"] == "Colombo"
    assert df.iloc[0]["cases"] == 71


def test_srilanka_weekly_data_r_python_equivalence():
    """
    Compare the complete Python dataset with the original R dataset.

    Requires DENGUEDATAHUB_SRI_LANKA_WEEKLY_RDA
    to point to the original RDA file.
    """
    import os
    import pytest
    from pandas.testing import assert_frame_equal

    rda_path = os.environ.get(
        "DENGUEDATAHUB_SRI_LANKA_WEEKLY_RDA"
    )

    if not rda_path or not os.path.isfile(rda_path):
        pytest.skip("Original Sri Lanka weekly RDA not available")

    pyreadr = pytest.importorskip("pyreadr")

    # Load original R dataset
    r_df = pyreadr.read_r(rda_path)["srilanka_weekly_data"]

    # Load Python dataset
    python_df = load_srilanka_weekly_data()

    # Compare all 26,311 records, columns, values,
    # data types, and row ordering
    assert_frame_equal(
        r_df.reset_index(drop=True),
        python_df.reset_index(drop=True),
        check_dtype=True,
        check_exact=True,
        check_frame_type=False,
    )
