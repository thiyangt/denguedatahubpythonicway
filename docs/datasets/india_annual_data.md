# `india_annual_data`

## Description

State/Union Territory (UT)-wise annual dengue and dengue haemorrhagic fever (DHF) cases and deaths in India, covering **2017–2022**. The original R documentation describes the dataset as dengue/DHF annual cases and deaths since 2017 and notes that its source was last accessed on **30 January 2023**.

## Python usage

```python
from denguedatahub import load_india_annual_data

data = load_india_annual_data()
print(data.head())
print(data.shape)
```

### Function signature

```python
load_india_annual_data()
```

**Parameters:** None.

**Returns:** A `pandas.DataFrame` containing 432 rows and five columns. The loader reads the packaged CSV file `denguedatahub/data/india_annual_data.csv`; it does not retrieve data from the source website at runtime.

## Dataset structure

| Column | Description | Python data type |
|---|---|---|
| `area` | Name of the affected state or Union Territory | `object` |
| `type` | Indicator category: `cases` or `deaths` | `object` |
| `year` | Reporting year, 2017–2022 | `object` (string-like) |
| `additional_information` | Additional information about the reporting period | `object` |
| `value` | Reported count for the corresponding indicator | `float64` |

The dataset contains **36 distinct areas**, two indicator categories (`cases`, `deaths`), and six reporting years. The `year` values are stored as strings rather than integer values.

### Missing values

The dataset contains **4 missing values** in `value` and **360 missing values** in `additional_information`. These missing values are retained by the Python loader.

## Example: filter cases for a year

```python
from denguedatahub import load_india_annual_data

data = load_india_annual_data()

cases_2022 = data[
    (data["year"] == "2022") & (data["type"] == "cases")
]

print(cases_2022[["area", "year", "value"]].head())
```

Because `year` is a string-like column, filter using `"2022"`, not the integer `2022`.

## Verification

The Python tests check the DataFrame shape, column order, area and indicator counts, reporting years, missing-value counts, data types, and representative records. An optional equivalence test uses `pyreadr` to compare the entire Python DataFrame against the original R `india_annual_data` object, including data types and exact values. This test runs only when the environment variable `DENGUEDATAHUB_INDIA_RDA` points to the original `.rda` file; otherwise, it is skipped.

## Source and attribution

**Original data source:** National Center for Vector Borne Disease Control, Directorate General of Health Services, Ministry of Health and Family Welfare, Government of India.

**Original R dataset:** `india_annual_data` in the R `denguedatahub` package. Original R documentation describes the data as last accessed on 30 January 2023.

**Python implementation:** `denguedatahub/load_india_annual_data.py`.
