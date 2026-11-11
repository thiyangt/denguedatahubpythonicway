# `sl_annual` — Annual reported dengue cases in Sri Lanka

## Overview

`sl_annual` provides annual reported dengue cases in Sri Lanka, together with an indicator identifying epidemic years. The original R package describes the coverage as **1989–2021** and documents **35 rows and 3 variables**. The stated date range is reproduced from the R documentation; it has not been independently checked against the CSV in this documentation review.

## Dataset structure

| Column | Description | Python data type |
| --- | --- | --- |
| `year` | Reporting year | `float64` |
| `dengue.cases` | Number of reported dengue cases | `float64` |
| `epidemic` | Epidemic-year indicator: `1` for an epidemic year, `0` otherwise | `float64` |

**Expected shape:** 35 rows × 3 columns.

## Loading the dataset in Python

```python
from denguedatahub import load_sl_annual

df = load_sl_annual()
print(df.head())
print(df.shape)
print(df.dtypes)
```

The loader reads the packaged `denguedatahub/data/sl_annual.csv` and explicitly assigns `float64` to all three columns to match the original R dataset's numeric types.

## Example: annual dengue case trend

```python
import matplotlib.pyplot as plt
from denguedatahub import load_sl_annual

df = load_sl_annual()
plt.plot(df["year"], df["dengue.cases"], marker="o")
plt.xlabel("Year")
plt.ylabel("Reported dengue cases")
plt.title("Annual reported dengue cases in Sri Lanka")
plt.show()
```

## Validation

The supplied Python tests check that the loader returns a nonempty pandas DataFrame containing a `year` column. A separate optional equivalence test compares the original R `.rda` data with the Python DataFrame using `pandas.testing.assert_frame_equal`, with exact values and data types required. This equivalence test **skips** when the environment variable `DENGUEDATAHUB_SL_ANNUAL_RDA` is not set to an accessible original `.rda` file (or when `pyreadr` is unavailable). The uploaded test source alone does not establish that the equivalence test was executed successfully in the current environment.

To run the tests from the repository root:

```powershell
pytest tests/test_load_sl_annual.py -v
```

## Original sources

1. World Health Organization. *Dengue Fact Sheet and Situation Report, Sri Lanka*, 22 July 2022. [WHO fact sheet (PDF)](https://cdn.who.int/media/docs/default-source/sri-lanka-documents/dengue-fact-sheet_7-2022-srl.pdf?sfvrsn=49021bd_1). Original R documentation notes access on 4 September 2024.
2. National Dengue Control Unit, Ministry of Health, Sri Lanka. *Weekly Dengue Updates*.

## Notes

- This is a packaged historical dataset, not a live dengue surveillance feed.
- The column name `dengue.cases` includes a period, matching the original dataset.
- The original R documentation states a 1989–2021 coverage period and 35 records; users requiring exact temporal coverage should inspect `df["year"].min()` and `df["year"].max()`.
