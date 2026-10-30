# `china_annual_data`

## Description

Annual indigenous and imported dengue cases in mainland China from **2005 to 2020**, including the number of counties reporting indigenous and imported dengue fever cases.

This dataset is adapted from the `china_annual_data` dataset in the original R **denguedatahub** package.

## Dataset structure

The dataset contains **16 rows and 5 columns**, with one record for each year from 2005 through 2020.

| Column | Description |
| --- | --- |
| `year` | Year |
| `dengue.cases.indigenous` | Number of indigenous dengue cases |
| `dengue.cases.imported` | Number of imported dengue cases |
| `counties.with.dengue.fever.indigenous` | Number of counties with dengue fever — indigenous cases |
| `counties.with.dengue.fever.imported` | Number of counties with dengue fever — imported cases |

The Python loader returns a **pandas DataFrame**. The `year` column is converted to integer type, and the other four columns are numeric according to the accompanying tests.

## Python usage

```python
from denguedatahub import load_china_annual_data

# Load the packaged dataset
df = load_china_annual_data()

# Preview records
print(df.head())

# Inspect the dataset
print(df.shape)
print(df.dtypes)

# Select one year
print(df[df["year"] == 2014])
```

**Function signature:**

```python
load_china_annual_data()
```

**Parameters:** None.

**Returns:** `pandas.DataFrame` containing annual dengue statistics for mainland China.

## How the loader works

1. Reads the packaged CSV file at `denguedatahub/data/china.csv`.
2. Uses `pandas.read_csv(..., thousands=",")` to interpret comma-separated thousands in numeric fields.
3. Converts `year` to integer type.
4. Returns the DataFrame without changing the original five column names.

## Verification

The project's `test_load_china_annual_data.py` checks that the loaded data:

- Contains **16 rows and 5 columns**.
- Covers every year from **2005 to 2020**.
- Has an integer `year` column and numeric measurement columns.
- Contains no missing values.
- Includes selected values checked against the original R dataset, such as **46,034 indigenous cases in 2014**, **15,378 in 2019**, and **616 indigenous and 158 imported cases in 2020**.

These are the checks encoded in the test file; they are not a claim that a new full-dataset equivalence comparison was run while preparing this document.

## Original data source

The original R package identifies the following source:

[Annual dengue data for mainland China, 2005–2020 (source table)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8997546/table/ijerph-19-03910-t001/?report=objectonly)

## R package reference

- R dataset: `china_annual_data`
- Original documentation: `man/china_annual_data.Rd`
- Original R source documentation: `R/china_annual_data.R`
- Python loader: `denguedatahub/load_china_annual_data.py`
- Python test: `tests/test_load_china_annual_data.py`

**Note:** The R file documents an existing dataset rather than defining a data-loading function; the Python package exposes it through `load_china_annual_data()`.
