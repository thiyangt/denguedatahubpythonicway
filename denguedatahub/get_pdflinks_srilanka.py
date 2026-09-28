import requests
from bs4 import BeautifulSoup


def get_pdflinks_srilanka(
    volume_number,
    url="https://epid.gov.lk/epid/public/index.php/weekly-epidemiological-report/weekly-epidemiological-report"
):
    """
    Get PDF links for a specified volume of Sri Lanka's
    Weekly Epidemiological Reports.

    Parameters
    ----------
    volume_number : str
        Volume identifier used to filter the PDF links.

    url : str, optional
        URL of the Weekly Epidemiological Report webpage.

    Returns
    -------
    list
        A list of PDF URLs matching the specified volume.
    """

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    links = []

    for link in soup.find_all("a", href=True):
        href = link["href"]

        if href.lower().endswith(".pdf") and volume_number in href:
            links.append(href)

    links.reverse()

    return links