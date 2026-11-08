# `korea_dengue`

## Description

Imported dengue case data associated with Korean travelers, organized by country and region for **2011–2015**. The original R package documentation states that the data were collected from the Korea Centers for Disease Control and Prevention (KCDC).

## Python function

```python
from denguedatahub import load_korea_dengue

df = load_korea_dengue()
print(df.head())
```

**Signature:** `load_korea_dengue()`

**Parameters:** None.

**Returns:** A `pandas.DataFrame` with **33 rows and 7 columns**.

## Variables

| Column | Description | Python data type |
|---|---|---|
| `Country` | Country associated with imported dengue cases | String (`object`) |
| `Region` | Geographic region | String (`object`) |
| `2011` | Reported value for 2011 | String (`object`) |
| `2012` | Reported value for 2012 | String (`object`) |
| `2013` | Reported value for 2013 | String (`object`) |
| `2014` | Reported value for 2014 | String (`object`) |
| `2015` | Reported value for 2015 | String (`object`) |

The dataset is stored in **wide format**, with one column for each year. The Python loader deliberately retains every field as a string, including year-specific values. It also preserves literal `"NA"` entries as strings, rather than interpreting them as pandas missing values. Consequently, a pandas `isna()` check does not count these literal markers as missing.

## Data loading

The loader reads the packaged CSV at `denguedatahub/data/korea_dengue.csv` using:

```python
pd.read_csv(data_path, dtype=str, keep_default_na=False)
```

The loader does not reshape the dataset or convert the annual columns to numeric types.

## Example: inspect the data

```python
from denguedatahub import load_korea_dengue

df = load_korea_dengue()

print(df.shape)
print(df.columns.tolist())
print(df.head())
```

To perform numeric calculations on a year column, explicitly convert its values and decide how to treat `"NA"`:

```python
import pandas as pd

cases_2015 = pd.to_numeric(df["2015"], errors="coerce")
print(cases_2015.sum())
```

This conversion is for analysis only; it does not alter the packaged dataset unless you assign the result back to it.

## Validation

The Python tests check:

- Dataset dimensions: **33 × 7**.
- Column names and order: `Country`, `Region`, `2011`, `2012`, `2013`, `2014`, `2015`.
- **32** distinct `Country` values and **6** distinct `Region` values.
- String values in every column and preservation of literal `"NA"` entries.
- Representative records, including the original spelling `"Unkown"`, which is retained to preserve source data.

A separate equivalence test compares the complete Python DataFrame against the original R `.rda` dataset with exact value and dtype checking **when** the `DENGUEDATAHUB_KOREA_RDA` environment variable points to that file and `pyreadr` is available. Otherwise, that test is skipped. The dataset was previously marked verified in the project checklist.

## Original R package reference

- **R dataset name:** `korea_dengue`
- **R documentation:** `man/korea_dengue.Rd`
- **R dataset format:** Tibble, 33 rows and 7 variables.
- **Original data source:** Je, Sungmo, Wonjun Bae, Jiyeon Kim, Seung Hyeok Seok, and Eung-Soo Hwang (2016). “Epidemiological characteristics and risk factors of dengue infection in Korean travelers.” *Journal of Korean Medical Science*, 31(12), 1863–1873.

This Python documentation describes the current loader and retains the dataset's original source attribution.
