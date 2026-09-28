from unittest.mock import patch, Mock
import importlib


def test_extract_table_from_pdf():
    module = importlib.import_module(
        "denguedatahub.convert_slwer_to_tidy"
    )

    mock_response = Mock()
    mock_response.content = b"fake pdf content"
    mock_response.raise_for_status.return_value = None

    fake_table = [
        ["Colombo", "100"],
        ["Gampaha", "80"],
        ["Kalutara", "50"],
    ]

    mock_page = Mock()
    mock_page.extract_table.return_value = fake_table

    mock_pdf = Mock()
    mock_pdf.pages = [Mock(), Mock(), mock_page]

    mock_pdf_context = Mock()
    mock_pdf_context.__enter__ = Mock(return_value=mock_pdf)
    mock_pdf_context.__exit__ = Mock(return_value=None)

    with patch.object(
        module.requests,
        "get",
        return_value=mock_response,
    ), patch.object(
        module.pdfplumber,
        "open",
        return_value=mock_pdf_context,
    ):
        result = module._extract_table_from_pdf(
            "https://example.com/report.pdf"
        )

    assert result.shape == (3, 2)
    assert result.iloc[0, 0] == "Colombo"
    assert result.iloc[0, 1] == "100"

    mock_page.extract_table.assert_called_once()

def test_clean_wer_table_colombo_layout():
    module = importlib.import_module(
        "denguedatahub.convert_slwer_to_tidy"
    )

    raw_data = [
        ["Header", "Cases"],
        ["Colombo", "100"],
        ["Gampaha", "80"],
        ["Nuwara Eliya", "40"],
        ["Kalmunai", "30"],
    ]

    table = module.pd.DataFrame(raw_data)

    result = module._clean_wer_table(
        table,
        year=2025
    )

    assert result.iloc[0]["district"] == "Colombo"
    assert result.iloc[0]["cases"] == 100

    assert "NuwaraEliya" in result["district"].values
    assert "Kalmune" in result["district"].values

def test_clean_wer_table_combined_layout():
    module = importlib.import_module(
        "denguedatahub.convert_slwer_to_tidy"
    )

    raw_data = [
        ["Header"],
        ["Colombo 100"],
        ["Gampaha 80"],
        ["Nuwara Eliya 40"],
        ["Kalmunai 30"],
    ]

    table = module.pd.DataFrame(raw_data)

    result = module._clean_wer_table(
        table,
        year=2025
    )

    assert result.iloc[0]["district"] == "Colombo"
    assert result.iloc[0]["cases"] == 100

    assert "NuwaraEliya" in result["district"].values
    assert "Kalmune" in result["district"].values

    nuwara_cases = result.loc[
        result["district"] == "NuwaraEliya",
        "cases"
    ].iloc[0]

    assert nuwara_cases == 40

def test_convert_slwer_to_tidy():
    module = importlib.import_module(
        "denguedatahub.convert_slwer_to_tidy"
    )

    week1 = module.pd.DataFrame({
        "district": ["Colombo", "Gampaha"],
        "cases": [100, 80],
    })

    week2 = module.pd.DataFrame({
        "district": ["Colombo", "Gampaha"],
        "cases": [120, 90],
    })

    with patch.object(
        module,
        "_extract_table_from_pdf",
        side_effect=[Mock(), Mock()],
    ), patch.object(
        module,
        "_clean_wer_table",
        side_effect=[week1, week2],
    ):
        result = module.convert_slwer_to_tidy(
            year=2025,
            reports_url=[
                "https://example.com/week1.pdf",
                "https://example.com/week2.pdf",
            ],
            start_date_first="2025-01-01",
            end_date_first="2025-01-07",
            start_date_last="2025-01-08",
            end_date_last="2025-01-14",
            week_no=[1, 2],
        )

    assert list(result.columns) == [
        "year",
        "week",
        "start.date",
        "end.date",
        "district",
        "cases",
    ]

    assert len(result) == 4

    assert result.iloc[0]["year"] == 2025
    assert result.iloc[0]["week"] == 1
    assert result.iloc[0]["district"] == "Colombo"
    assert result.iloc[0]["cases"] == 100

    assert result.iloc[2]["week"] == 2
    assert result.iloc[2]["district"] == "Colombo"
    assert result.iloc[2]["cases"] == 120