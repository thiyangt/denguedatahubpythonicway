# `philippines_daily_data`

## Description

Dengue infection and death records for locations and regions in the Philippines. The original R package describes this dataset as **“Daily cases of dengue in Philippines”** and names it `philippines_daily_data`.

## Dataset information

| Property | Value |
|---|---|
| Python loader | `load_philippines_daily_data()` |
| Dimensions | 32,701 rows × 5 columns |
| Format | `pandas.DataFrame` |
| Packaged data file | `denguedatahub/data/philippines_daily_data.csv` |
| Source | [Humanitarian Data Exchange — Philippine Dengue Cases and Deaths](https://data.humdata.org/dataset/philippine-dengue-cases-and-deaths?) |

## Variables

| Column | Description |
|---|---|
| `location` | Location recorded in the source dataset |
| `affected_and_infected` | Number of affected/infected dengue cases |
| `affected_and_killed` | Number of affected/killed cases (deaths) |
| `date` | Date associated with the record; retained as text |
| `region` | Region name |

The descriptions follow the original R `.Rd` documentation. The original describes `date` as the “date of the week”; the Python loader does not infer or validate reporting frequency.

## Usage

```python
from denguedatahub import load_philippines_daily_data

df = load_philippines_daily_data()
print(df.head())
print(df.shape)
```

### Working with dates and counts

The loader deliberately retains non-missing values as strings. Convert columns explicitly for numerical or date-based analysis:

```python
import pandas as pd

analysis_df = df.copy()
analysis_df["affected_and_infected"] = pd.to_numeric(
    analysis_df["affected_and_infected"], errors="coerce"
)
analysis_df["affected_and_killed"] = pd.to_numeric(
    analysis_df["affected_and_killed"], errors="coerce"
)
analysis_df["date"] = pd.to_datetime(
    analysis_df["date"], format="%m/%d/%Y", errors="coerce"
)
```

These conversions are optional analysis steps, **not** transformations performed by `load_philippines_daily_data()`.

## Loading behavior

The function reads the bundled CSV with `pandas.read_csv`, specifying `dtype=str`, UTF-8 encoding, and `keep_default_na=False` with `na_values=[""]`. Consequently, non-missing count values and dates remain strings, while empty fields become missing values (`NaN`). It returns the DataFrame without further transformation.

## Data validation

The Python test checks:

- Dataset dimensions of **32,701 × 5** and the original column order.
- Object/string column types and text-formatted dates.
- Exactly **one missing value** in `affected_and_killed`, with no missing values in the other columns.
- Representative first and last records.

The original R documentation also reports 32,701 rows and five variables. The supplied test does **not** perform a full row-by-row comparison with the original R `.rda` file, so its checks should not be described as a complete R–Python equivalence test.

## Original R reference

- R dataset name: `philippines_daily_data`
- R documentation: `man/philippines_daily_data.Rd`
- R metadata source: `R/philippines_daily_data.R`
- Source dataset: [Philippine Dengue Cases and Deaths — HDX](https://data.humdata.org/dataset/philippine-dengue-cases-and-deaths?)
