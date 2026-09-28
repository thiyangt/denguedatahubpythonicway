from unittest.mock import patch, Mock
import importlib

from denguedatahub import get_pdflinks_srilanka


def test_get_pdflinks_srilanka():
    fake_html = """
    <html>
        <body>
            <a href="reports/Vol_52_no_01-english.pdf">Week 1</a>
            <a href="reports/Vol_52_no_02-english.pdf">Week 2</a>
            <a href="reports/Vol_51_no_52-english.pdf">Old volume</a>
            <a href="reports/information.html">Not a PDF</a>
        </body>
    </html>
    """

    mock_response = Mock()
    mock_response.text = fake_html
    mock_response.raise_for_status.return_value = None

    module = importlib.import_module(
        "denguedatahub.get_pdflinks_srilanka"
    )

    with patch.object(
        module.requests,
        "get",
        return_value=mock_response
    ):
        result = get_pdflinks_srilanka("Vol_52")

    assert result == [
        "reports/Vol_52_no_02-english.pdf",
        "reports/Vol_52_no_01-english.pdf"
    ]