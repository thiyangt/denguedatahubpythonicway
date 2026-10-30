# `get_pdflinks_srilanka`

## Description

Retrieve links to PDF files for a specified volume of the **Weekly Epidemiological Reports (WER)** published by the Epidemiology Unit, Ministry of Health, Sri Lanka.

This Python function adapts the original `get_pdflinks_srilanka()` function in the R `denguedatahub` package.

## Usage

```python
from denguedatahub import get_pdflinks_srilanka

links = get_pdflinks_srilanka("Vol_52")
print(links)
```

## Signature

```python
get_pdflinks_srilanka(
    volume_number,
    url="https://epid.gov.lk/epid/public/index.php/weekly-epidemiological-report/weekly-epidemiological-report"
)
```

## Parameters

| Parameter | Type | Description |
|---|---|---|
| `volume_number` | `str` | Volume identifier used to select PDF links, such as `"Vol_52"`. |
| `url` | `str`, optional | Webpage containing links to the reports. Defaults to the Epidemiology Unit WER page shown in the signature. |

## Returns

`list[str]`: PDF link strings whose `href` values contain the requested volume identifier. Links are returned in reverse order of their appearance on the webpage. If none match, an empty list is returned.

**Note:** The returned links are the webpage's original `href` values. They may be relative paths, not complete URLs.

## Example: Custom webpage URL

```python
from denguedatahub import get_pdflinks_srilanka

links = get_pdflinks_srilanka(
    volume_number="Vol_52",
    url="https://www.epid.gov.lk/weekly-epidemiological-report/weekly-epidemiological-report"
)

for link in links:
    print(link)
```

The example requires the webpage to be accessible and to contain matching PDF links. The function does not download the PDF files.

## How it works

1. Requests the specified webpage using `requests` and checks for HTTP errors.
2. Parses the HTML using BeautifulSoup.
3. Selects anchor elements with an `href` ending in `.pdf` (case-insensitive) and containing `volume_number`.
4. Reverses the matching links and returns them as a list.

## Notes and limitations

- Requires access to the report webpage. Network or HTTP errors may interrupt execution.
- The default URL differs from the URL used in the original R package.
- The function does not convert relative paths into absolute URLs.
- The volume identifier is matched as a substring of the link, not as a separately parsed field.
- The automated test uses a mocked HTML page; it does not verify current availability of the official website.

## Original R reference

- Original package: [thiyangt/denguedatahub](https://github.com/thiyangt/denguedatahub)
- R source: `R/get_pdflinks_srilanka.R`
- R documentation: `man/get_pdflinks_srilanka.Rd`
- Original function author: Thiyanga S. Talagala
