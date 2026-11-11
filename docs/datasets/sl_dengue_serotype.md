# `sl_dengue_serotype`

## Overview

Historical records of dengue serotypes reported as circulating in Sri Lanka. The Python dataset contains 13 reporting records covering 1965–2017.

## Loading the dataset

```python
from denguedatahub.load_sl_dengue_serotype import load_sl_dengue_serotype

df = load_sl_dengue_serotype()
print(df.head())
```

The function loads the packaged `denguedatahub/data/sl_dengue_serotype.csv` file and returns a `pandas.DataFrame`.

## Dataset structure

**Dimensions:** 13 rows × 2 columns.

| Column | Type in Python | Description |
|---|---|---|
| `reporting.year` | `float64` | Year in which the serotype information was reported. |
| `dengue.serotype` | `object` (strings) | Dengue serotype designation(s) recorded for that reporting year. |

The dataset has no missing values according to the Python test assertions. Its reporting years are 1965, 1968, 1978, 1980, 1990, 1992, 1993, 1997, 2003, 2004, 2006, 2009, and 2017. These are reporting records, not a complete annual time series.

## Example analysis

```python
# Inspect all available reporting years and their serotypes
print(df[["reporting.year", "dengue.serotype"]].to_string(index=False))

# Find records mentioning DENV-4
print(df[df["dengue.serotype"].str.contains("DENV-4", regex=False)])
```

## Validation

The test `tests/test_load_sl_dengue_serotype.py` checks:

- Shape: `(13, 2)`.
- Column names and order.
- `float64` year and `object` serotype types.
- Absence of missing values.
- Exact sequence of all 13 reporting years and corresponding serotype descriptions.

The loader uses UTF-8 encoding and explicitly sets column types. The uploaded test file does not contain a direct R `.rda` comparison; the checks above describe the validations visible in that file.

## Note on the original R documentation

The original `man/sl_dengue_serotype.Rd` and `R/sl_dengue_serotype.R` text describes **35 rows and 3 variables** and mentions `year` and `dengue.cases`. Those fields do not match the uploaded Python implementation or its test, which both specify **13 rows and 2 columns** (`reporting.year` and `dengue.serotype`). This appears to be a documentation inconsistency in the R source. The Python structure is used here; an independent check against the original R dataset object would be needed to establish exact R–Python equivalence from these files alone.

## Original source

Ali, Shahid, Abdul Waheed Khan, Andrew W. Taylor-Robinson, Muhammad Adnan, Shahana Malik, and Saba Gul. “The unprecedented magnitude of the 2017 dengue outbreak in Sri Lanka provides lessons for future mosquito-borne infection control and prevention.” *Infection, Disease & Health* 23, no. 2 (2018): 114–120.
