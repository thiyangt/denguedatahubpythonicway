# `singapore_weekly_data`

## Overview

Weekly dengue case counts for Singapore, covering observations from 2018 through 2023. The Python package exposes the dataset as a pandas DataFrame through `load_singapore_weekly_data()`.

## Source

The original R package cites The Straits Times, *Singapore dengue cases*:

https://www.straitstimes.com/multimedia/graphics/2022/06/singapore-dengue-cases/index.html

## Dataset structure

The Python loader and its tests specify **272 rows and 3 columns**:

| Column | Python dtype | Description |
| --- | --- | --- |
| `year` | `float64` | Year of observation |
| `week` | `int64` | Week number (values from 0 to 52 in the dataset) |
| `cases` | `float64` | Reported dengue case count; some entries are missing |

The data spans **2018–2023**. The `cases` column contains **3 missing values**; `year` and `week` contain none.

## Usage

```python
from denguedatahub.load_singapore_weekly_data import load_singapore_weekly_data

df = load_singapore_weekly_data()
print(df.head())
print(df.shape)  # (272, 3)
```

The loader reads `denguedatahub/data/singapore_weekly_data.csv` using UTF-8 encoding and explicitly sets the three column dtypes. It does not impute missing case counts.

## Validation

The accompanying test, `tests/test_load_singapore_weekly_data.py`, checks:

- Dataset dimensions and column order.
- Column data types and missing-value counts.
- Minimum and maximum years (2018 and 2023).
- First record: year `2018`, week `0`, cases `54`.
- Last record: year `2023`, week `8`, cases `112`.
- Week numbers fall within `0`–`52`.

These checks describe the assertions in the supplied test file; they were **not rerun** while preparing this documentation.

## Note on the original R documentation

The original `man/singapore_weekly_data.Rd` and `R/singapore_weekly_data.R` text supplied for this dataset incorrectly describe **Sri Lanka** and state **18,772 rows and 6 variables**, while naming only `year`, `week`, and `cases`. The Python loader and test instead specify **Singapore**, **272 rows**, and **3 columns**. This documentation follows the Python implementation and records the discrepancy transparently. The supplied materials alone do not independently establish full row-by-row equivalence with the original R data object.
