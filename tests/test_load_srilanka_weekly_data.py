
import pandas as pd

from denguedatahub.load_srilanka_weekly_data import load_srilanka_weekly_data


def test_load_srilanka_weekly_data():
    df = load_srilanka_weekly_data()

    assert isinstance(df, pd.DataFrame)

    assert df.shape == (18772, 6)

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
