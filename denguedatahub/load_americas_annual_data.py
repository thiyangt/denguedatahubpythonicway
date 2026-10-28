
from pathlib import Path
import pandas as pd


def load_americas_annual_data():
    """
    Load and reshape annual dengue data for the Americas.

    Returns
    -------
    pandas.DataFrame
        Data containing region, country, year,
        indicator type, and cases.
    """

    data_path = Path(__file__).parent / "data" / "americas.csv"

    df = pd.read_csv(data_path)


    indicator_types = df.iloc[0, 2:].tolist()

    country_data = df.iloc[2:54].copy()

    country_data = country_data.rename(
        columns={
            df.columns[0]: "region",
            df.columns[1]: "country"
        }
    )

    value_columns = country_data.columns[2:]

    column_info = pd.DataFrame({
        "column": value_columns,
        "year": [int(col.split(".")[0]) for col in value_columns],
        "type": indicator_types
    })

    long_data = country_data.melt(
        id_vars=["region", "country"],
        value_vars=value_columns,
        var_name="column",
        value_name="cases"
    )

    long_data = long_data.merge(
        column_info,
        on="column",
        how="left",
        validate="many_to_one"
    )

    long_data = long_data[
        ["region", "country", "year", "type", "cases"]
    ]

    return long_data
