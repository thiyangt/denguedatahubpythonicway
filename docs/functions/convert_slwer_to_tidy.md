# `convert_slwer_to_tidy()`

## Description

Read dengue case tables from Sri Lanka's Weekly Epidemiological Reports (WERs) and combine them into a tidy pandas DataFrame, with one row per district and reporting week. This Python function adapts the original R package's `convert_slwer_to_tidy()` function.

The reports are published by the Epidemiology Unit, Ministry of Health, Sri Lanka. The function expects URLs pointing directly to report PDF files; it downloads each PDF and extracts a table from **page 3**.

## Usage

```python
from denguedatahub import convert_slwer_to_tidy

result = convert_slwer_to_tidy(
    year=2025,
    reports_url=["https://example.org/report-week-1.pdf"],  # replace with a real WER PDF URL
    start_date_first="2025-01-01",
    end_date_first="2025-01-07",
    start_date_last="2025-01-01",
    end_date_last="2025-01-07",
    week_no=[1],
)
print(result.head())
```

The example shows the required call structure; the placeholder URL is **not** a live report. Supply an accessible WER PDF URL before running it.

## Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `year` | `int` | Year of the reports. A separate row-selection rule is applied for 2020. |
| `reports_url` | iterable of `str` | Direct PDF URLs, ordered to match the supplied week numbers and date sequence. |
| `start_date_first` | date-like `str` | First reporting week's start date, e.g. `"2025-01-01"`. |
| `end_date_first` | date-like `str` | First reporting week's end date. |
| `start_date_last` | date-like `str` | Last reporting week's start date. |
| `end_date_last` | date-like `str` | Last reporting week's end date. |
| `week_no` | indexable sequence | Week numbers corresponding, in order, to the PDF URLs. |

Dates are generated in seven-day increments from the first to the last supplied date. Provide matching numbers of report URLs, week numbers, start dates, and end dates.

## Returns

A `pandas.DataFrame` containing these columns, in order:

| Column | Meaning |
| --- | --- |
| `year` | Report year |
| `week` | Reporting week number |
| `start.date` | Start of reporting week (`datetime64` in pandas) |
| `end.date` | End of reporting week (`datetime64` in pandas) |
| `district` | Cleaned district or reporting-area name |
| `cases` | Extracted dengue case count (numeric when parsing succeeds) |

The function returns the combined table; it does not save a CSV file automatically.

## Processing workflow

1. Download each PDF using `requests` and extract the first detected table on its third page using `pdfplumber`.
2. Select the relevant rows, with a special offset for reports from 2020.
3. Parse either a two-column layout (`district`, `cases`) or a combined-text layout.
4. Standardize selected names, including `Nuwara` / `Nuwara Eliya` to `NuwaraEliya` and `Kalmunai` to `Kalmune`.
5. Add the year, week number, and weekly start/end dates to each extracted table.
6. Combine the tables, retain recognized reporting areas, correct selected spelling variants, and order the output columns.

The module also defines two internal helpers: `_extract_table_from_pdf()` and `_clean_wer_table()`. They are implementation details, not separate public functions.

## Notes and limitations

- This function requires network access and PDF layouts compatible with the current extraction and cleaning logic. Not all historical or future report layouts are guaranteed to work.
- HTTP failures, invalid URLs, missing PDF pages, unrecognized table structures, and mismatched week/date inputs may raise errors.
- Case values that cannot be parsed as numbers are converted to missing values (`NaN`). Rows whose district names are not recognized are filtered out.
- The function uses the supplied report ordering when assigning weeks and dates; it does not infer these values from the PDF filenames.
- The implementation has a duplicated intermediate date-attachment block. This is redundant and does not need to be reflected in usage examples.
- Tests use mocked PDF responses and tables; they verify representative extraction, cleaning, and combined-output behavior rather than live website compatibility.

## Original R reference

Adapted from `convert_slwer_to_tidy()` in the original [`denguedatahub` R package](https://github.com/thiyangt/denguedatahub), authored by Thiyanga S. Talagala. See `man/convert_slwer_to_tidy.Rd` and `R/convert_slwer_to_tidy.R` in that repository. The R version uses `tabulapdf`, `dplyr`, and `purrr`; this Python implementation uses `pdfplumber`, `requests`, and `pandas`.
