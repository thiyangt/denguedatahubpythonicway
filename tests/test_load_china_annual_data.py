
import pandas as pd

from denguedatahub import load_china_annual_data


def test_load_china_annual_data():
    df = load_china_annual_data()

    # Check DataFrame structure
    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    assert df.shape == (16, 5)

    # Check expected columns
    expected_columns = [
        "year",
        "dengue.cases.indigenous",
        "dengue.cases.imported",
        "counties.with.dengue.fever.indigenous",
        "counties.with.dengue.fever.imported",
    ]

    assert df.columns.tolist() == expected_columns

    # Check year values and data type
    assert pd.api.types.is_integer_dtype(df["year"])
    assert df["year"].tolist() == list(range(2005, 2021))

    # Check numeric columns
    for column in expected_columns[1:]:
        assert pd.api.types.is_numeric_dtype(df[column])

    # Check missing values
    assert df.isna().sum().sum() == 0

    # Check specific values against original R dataset
    data_2014 = df.loc[df["year"] == 2014].iloc[0]
    assert data_2014["dengue.cases.indigenous"] == 46034

    data_2019 = df.loc[df["year"] == 2019].iloc[0]
    assert data_2019["dengue.cases.indigenous"] == 15378

    # Check total dengue cases for selected year
    data_2020 = df.loc[df["year"] == 2020].iloc[0]
    assert data_2020["dengue.cases.indigenous"] == 616
    assert data_2020["dengue.cases.imported"] == 158
