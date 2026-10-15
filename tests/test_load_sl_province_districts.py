
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
