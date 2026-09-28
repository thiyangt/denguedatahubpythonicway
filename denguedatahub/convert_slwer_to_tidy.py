from io import BytesIO

import pandas as pd
import pdfplumber
import requests

VALID_DISTRICTS = [
    "Colombo",
    "Gampaha",
    "Kalutara",
    "Kandy",
    "Matale",
    "NuwaraEliya",
    "Galle",
    "Hambantota",
    "Matara",
    "Jaffna",
    "Kilinochchi",
    "Mannar",
    "Vavuniya",
    "Mullaitivu",
    "Batticaloa",
    "Ampara",
    "Trincomalee",
    "Kurunegala",
    "Puttalam",
    "Anuradhapur",
    "Anuradhapura",
    "Polonnaruwa",
    "Badulla",
    "Monaragala",
    "Ratnapura",
    "Kegalle",
    "Kalmune",
]

def _extract_table_from_pdf(pdf_url):
    """
    Download a WER PDF and extract the table from page 3.

    Parameters
    ----------
    pdf_url : str
        URL of the Weekly Epidemiological Report PDF.

    Returns
    -------
    pandas.DataFrame
        Table extracted from page 3 of the PDF.
    """

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(pdf_url, headers=headers)
    response.raise_for_status()

    with pdfplumber.open(BytesIO(response.content)) as pdf:
        page = pdf.pages[2]
        table = page.extract_table()

    return pd.DataFrame(table)

def _clean_wer_table(table, year):
    """
    Clean an extracted WER dengue table.

    Parameters
    ----------
    table : pandas.DataFrame
        Raw table extracted from page 3 of a WER PDF.

    year : int
        Year of the report.

    Returns
    -------
    pandas.DataFrame
        Cleaned table containing district and cases.
    """

    if year == 2020:
        data = table.iloc[3:29].copy()
    else:
        data = table.iloc[1:27].copy()

    first_value = str(data.iloc[0, 0]).strip()

    if first_value == "Colombo":
        cleaned = pd.DataFrame({
            "district": data.iloc[:, 0],
            "cases": data.iloc[:, 1]
        })

        cleaned["district"] = (
            cleaned["district"]
            .astype(str)
            .str.strip()
        )

        cleaned["cases"] = pd.to_numeric(
            cleaned["cases"],
            errors="coerce"
        )

        cleaned["district"] = cleaned["district"].replace({
            "Nuwara": "NuwaraEliya",
            "Nuwara Eliya": "NuwaraEliya",
            "Kalmunai": "Kalmune",
        })

        return cleaned.reset_index(drop=True)

    else:
        combined = data.iloc[:, 0].astype(str).str.strip()

        split_data = combined.str.split(
            n=2,
            expand=True
        )

        cleaned = pd.DataFrame({
            "district": split_data[0],
            "cases": split_data[1]
        })

        nuwara_mask = cleaned["district"] == "Nuwara"

        cleaned.loc[nuwara_mask, "district"] = "NuwaraEliya"
        cleaned.loc[nuwara_mask, "cases"] = split_data.loc[
            nuwara_mask, 2
        ]

        cleaned["district"] = cleaned["district"].replace({
            "Kalmunai": "Kalmune"
        })

        cleaned["cases"] = pd.to_numeric(
            cleaned["cases"],
            errors="coerce"
        )

        return cleaned.reset_index(drop=True)


def convert_slwer_to_tidy(
    year,
    reports_url,
    start_date_first,
    end_date_first,
    start_date_last,
    end_date_last,
    week_no,
):
    """
    Convert Sri Lankan Weekly Epidemiological Report data
    into a tidy pandas DataFrame.

    Parameters
    ----------
    year : int
        Year of the reports.

    reports_url : list
        List of WER PDF URLs.

    start_date_first : str
        Start date of the first report.

    end_date_first : str
        End date of the first report.

    start_date_last : str
        Start date of the last report.

    end_date_last : str
        End date of the last report.

    week_no : iterable
        Week numbers corresponding to the reports.

    Returns
    -------
    pandas.DataFrame
        Tidy dengue data by year, week, dates, district, and cases.
    """
    weekly_tables = []

    for url in reports_url:
        raw_table = _extract_table_from_pdf(url)
        cleaned_table = _clean_wer_table(raw_table, year)

        weekly_tables.append(cleaned_table)

    start_dates = pd.date_range(
        start=start_date_first,
        end=start_date_last,
        freq="7D"
    )

    end_dates = pd.date_range(
        start=end_date_first,
        end=end_date_last,
        freq="7D"
    )

    dated_tables = []

    for i, table in enumerate(weekly_tables):
        table = table.copy()

        table["year"] = year
        table["week"] = week_no[i]
        table["start.date"] = start_dates[i]
        table["end.date"] = end_dates[i]

        dated_tables.append(table)

    dated_tables = []

    for i, table in enumerate(weekly_tables):
        table = table.copy()

        table["year"] = year
        table["week"] = week_no[i]
        table["start.date"] = start_dates[i]
        table["end.date"] = end_dates[i]

        dated_tables.append(table)

    result = pd.concat(
        dated_tables,
        ignore_index=True
    )

    result = result[
        result["district"].isin(VALID_DISTRICTS)
    ].copy()

    result["district"] = result["district"].replace({
        "Anuradhapur": "Anuradhapura",
        "Kurunagala": "Kurunegala",
    })

    result = result[
        [
            "year",
            "week",
            "start.date",
            "end.date",
            "district",
            "cases",
        ]
    ]

    return result.reset_index(drop=True)