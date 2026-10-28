
import pandas as pd

from denguedatahub import load_cdc_data


def test_load_cdc_data():
    datasets = load_cdc_data()

    expected_names = [
        "cdc_dengue_countyyear",
        "cdc_dengue_agesex",
        "cdc_casesby_week",
        "cdc_dengue_casesbyjurisdiction",
        "cdc_local_dengue_cases",
        "cdc_travel_associated_dengue_cases"
    ]

    assert isinstance(datasets, dict)

    assert set(datasets.keys()) == set(expected_names)

    for name in expected_names:
        df = datasets[name]

        assert isinstance(df, pd.DataFrame)
        assert not df.empty

    assert datasets["cdc_dengue_agesex"].shape == (140, 5)
    assert datasets["cdc_casesby_week"].shape == (742, 4)
    assert datasets["cdc_dengue_casesbyjurisdiction"].shape == (616, 6)
    assert datasets["cdc_local_dengue_cases"].shape == (14, 3)
    assert datasets["cdc_travel_associated_dengue_cases"].shape == (14, 3)
