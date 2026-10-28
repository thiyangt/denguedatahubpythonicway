
import pandas as pd

from denguedatahub.load_srilanka_2020 import load_srilanka_2020


def test_load_srilanka_2020():
    df = load_srilanka_2020()

    assert isinstance(df, pd.DataFrame)
    assert df.shape == (1316, 6)

    assert df.columns.tolist() == [
        "year",
        "week",
        "start.date",
        "end.date",
        "district",
        "cases",
    ]

    assert (df["year"] == 2020).all()
    assert df["week"].between(1, 51).all()
    assert not (df["week"] == 52).any()

    assert df.iloc[0]["district"] == "Colombo"
    assert df.iloc[0]["cases"] == 535
    assert df.iloc[0]["week"] == 1
