
import pandas as pd

from denguedatahub import load_sl_annual


def test_load_sl_annual():
    df = load_sl_annual()

    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    assert "year" in df.columns
