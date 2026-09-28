from pathlib import Path
from urllib.parse import urlparse

import requests

from .get_pdflinks_srilanka import get_pdflinks_srilanka


def download_pdfwer_srilanka(
    folder_name,
    volume_number,
    url="https://epid.gov.lk/epid/public/index.php/weekly-epidemiological-report/weekly-epidemiological-report"
):
    """
    Download Sri Lankan Weekly Epidemiological Report PDFs
    for a specified volume.

    Parameters
    ----------
    folder_name : str
        Folder where the downloaded PDF files will be saved.

    volume_number : str
        Volume identifier used to select the reports.

    url : str, optional
        URL of the Weekly Epidemiological Report webpage.

    Returns
    -------
    None
    """

    folder = Path(folder_name)
    folder.mkdir(parents=True, exist_ok=True)

    pdf_links = get_pdflinks_srilanka(
        volume_number=volume_number,
        url=url
    )

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    for link in pdf_links:
        pdf_name = Path(urlparse(link).path).name
        destination = folder / pdf_name

        response = requests.get(link, headers=headers)
        response.raise_for_status()

        destination.write_bytes(response.content)

        print(f"Downloaded: {pdf_name}")