# `download_pdfwer_srilanka`

## Description

Download Weekly Epidemiological Report (WER) PDF files for a specified volume from the Epidemiology Unit, Ministry of Health, Sri Lanka, and save them to a local folder.

This Python function adapts the original R package function of the same name. It uses [`get_pdflinks_srilanka()`](get_pdflinks_srilanka.md) to identify matching PDF links before downloading them.

## Usage

```python
from denguedatahub import download_pdfwer_srilanka

download_pdfwer_srilanka(
    folder_name="dengue_reports",
    volume_number="Vol_52",
)
```

## Function signature

```python
download_pdfwer_srilanka(
    folder_name,
    volume_number,
    url="https://epid.gov.lk/epid/public/index.php/weekly-epidemiological-report/weekly-epidemiological-report",
)
```

## Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `folder_name` | `str` or path-like | Destination folder for downloaded PDF files. Created if it does not exist. |
| `volume_number` | `str` | Volume identifier used to select reports, such as `"Vol_52"`. |
| `url` | `str`, optional | URL of the Weekly Epidemiological Report listing page. Defaults to the address shown in the signature. |

## Returns

`None`. The function saves matching PDF files to disk rather than returning their contents or paths.

## Example: Choose a destination folder

```python
from denguedatahub import download_pdfwer_srilanka

download_pdfwer_srilanka(
    folder_name="reports/vol_52",
    volume_number="Vol_52",
)
```

The function creates the folder (including missing parent directories), requests each matching PDF, writes its response bytes to a file named after the PDF URL's path, and prints a `Downloaded:` message after each successful save.

## How it works

1. Creates the destination folder if needed.
2. Calls `get_pdflinks_srilanka(volume_number=..., url=...)` to obtain matching PDF links.
3. Requests each returned link with `requests.get()` and checks the HTTP status.
4. Saves the response bytes to the destination folder under the link's basename.

## Notes and limitations

- The function requires network access and depends on the source website's structure and availability. A successful live download is not guaranteed.
- Returned PDF links must be absolute URLs for the current downloader to request them successfully. Relative links are not resolved against the listing page URL.
- Existing files with the same name are overwritten.
- Network and HTTP errors are propagated as exceptions; the function does not retry failed downloads.
- The current implementation does not validate that the downloaded response is a valid PDF document.
- The automated test uses mocked links and HTTP responses; it verifies file creation and saved bytes, not live website access.

## Original R package reference

Adapted from `download_pdfwer_srilanka()` in the original [R `denguedatahub` package](https://github.com/thiyangt/denguedatahub), authored by **Thiyanga S. Talagala**. See `man/download_pdfwer_srilanka.Rd` and `R/download_pdfwer_srilanka.R` in the original repository.

The R version creates a folder, extracts matching PDF links from the report page, and downloads the corresponding files. The Python version delegates link extraction to `get_pdflinks_srilanka()` and uses `pathlib` and `requests` for file operations and downloads.
