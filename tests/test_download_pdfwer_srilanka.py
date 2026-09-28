from unittest.mock import patch, Mock
import importlib

from denguedatahub import download_pdfwer_srilanka


def test_download_pdfwer_srilanka(tmp_path):
    fake_links = [
        "https://example.com/Vol_52_no_01-english.pdf",
        "https://example.com/Vol_52_no_02-english.pdf",
    ]

    mock_response = Mock()
    mock_response.content = b"fake pdf content"
    mock_response.raise_for_status.return_value = None

    module = importlib.import_module(
        "denguedatahub.download_pdfwer_srilanka"
    )

    with patch.object(
        module,
        "get_pdflinks_srilanka",
        return_value=fake_links,
    ), patch.object(
        module.requests,
        "get",
        return_value=mock_response,
    ):
        download_pdfwer_srilanka(
            folder_name=tmp_path,
            volume_number="Vol_52",
        )

    file1 = tmp_path / "Vol_52_no_01-english.pdf"
    file2 = tmp_path / "Vol_52_no_02-english.pdf"

    assert file1.exists()
    assert file2.exists()

    assert file1.read_bytes() == b"fake pdf content"
    assert file2.read_bytes() == b"fake pdf content"