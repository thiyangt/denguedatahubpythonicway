from pathlib import Path
import pandas as pd


def load_cdc_usa_dengue_infection():
    """
    Load and combine CDC NNDSS dengue surveillance
    data for 2019–2022.
    """

    data_folder = Path(__file__).parent / "data" / "cdc"

    base_name = (
        "NNDSS_-_TABLE_1J._Dengue_virus_infections__"
        "Dengue_to_Severe_dengue"
    )

    files = [
        f"{base_name} (3).csv",  # 2019
        f"{base_name} (2).csv",  # 2020
        f"{base_name} (1).csv",  # 2021
        f"{base_name}.csv"       # 2022
    ]

    datasets = []

    for filename in files:
        df = pd.read_csv(data_folder / filename)

        columns = {
            "Reporting Area": "area",
            "MMWR Year": "year",
            "MMWR Week": "week"
        }

        for col in df.columns:
            if "Current week" not in col or "flag" in col.lower():
                continue

            if "Dengue-like illness" in col:
                columns[col] = "dengue_like_illness"

            elif "Severe dengue" in col:
                columns[col] = "severe_dengue"

            elif ", Dengue, Current week" in col:
                columns[col] = "dengue_cases"

        required = [
            "area",
            "year",
            "week",
            "dengue_cases",
            "dengue_like_illness",
            "severe_dengue"
        ]

        df = df[list(columns.keys())].rename(columns=columns)
        df = df[required]

        datasets.append(df)

        combined = pd.concat(datasets, ignore_index=True)

    combined = combined[
        combined["area"] != "TOTAL"
    ].reset_index(drop=True)

    return combined