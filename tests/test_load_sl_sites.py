
import pandas as pd

from denguedatahub import load_sl_sites


def test_load_sl_sites():
    df = load_sl_sites()

    assert isinstance(df, pd.DataFrame)
    assert not df.empty
