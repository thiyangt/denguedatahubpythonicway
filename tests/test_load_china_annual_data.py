
import pandas as pd

from denguedatahub import load_china_annual_data


def test_load_china_annual_data():
    df = load_china_annual_data()

    assert isinstance(df, pd.DataFrame)
    assert not df.empty

    assert len(df) == 16

    assert "year" in df.columns

    assert pd.api.types.is_integer_dtype(df["year"])
