import pandas as pd

from denguedatahub.min_max import min_max


def test_min_max_global():
    data = pd.DataFrame({
        "cases": [10, 20, 30]
    })

    result = min_max(data, "cases")

    assert result["min.cases"].tolist() == [10, 10, 10]
    assert result["max.cases"].tolist() == [30, 30, 30]
    assert result["minmax.cases"].tolist() == [0.0, 0.5, 1.0]

def test_min_max_group():
    data = pd.DataFrame({
        "cases": [10, 20, 30, 100, 150, 200],
        "district": ["A", "A", "A", "B", "B", "B"]
    })

    result = min_max(
        data,
        "cases",
        local=True,
        group_var="district"
    )

    assert result["min.group"].tolist() == [10, 10, 10, 100, 100, 100]
    assert result["max.group"].tolist() == [30, 30, 30, 200, 200, 200]
    assert result["minmax.group"].tolist() == [0.0, 0.5, 1.0, 0.0, 0.5, 1.0]

def test_min_max_with_missing_values():
    data = pd.DataFrame({
        "cases": [10, 20, None, 30]
    })

    result = min_max(data, "cases")

    assert result["min.cases"].tolist() == [10.0, 10.0, 10.0, 10.0]
    assert result["max.cases"].tolist() == [30.0, 30.0, 30.0, 30.0]

    assert result["minmax.cases"].iloc[0] == 0.0
    assert result["minmax.cases"].iloc[1] == 0.5
    assert pd.isna(result["minmax.cases"].iloc[2])
    assert result["minmax.cases"].iloc[3] == 1.0