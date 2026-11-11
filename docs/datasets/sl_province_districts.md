# `sl_province_districts`

## Overview

`sl_province_districts` provides a mapping of Sri Lankan districts to their provinces. The original R package describes Sri Lanka as having nine provinces and supplies a dataset containing **26 rows and 2 columns**. This documentation describes the dataset as packaged, without assuming that every row represents a unique administrative district.

## Dataset structure

| Column | Description |
| --- | --- |
| `province` | Name of the province. |
| `district` | Name of the district. |

The accompanying Python test expects **26 records**, **9 unique province names**, and the columns in the order shown above. The test also checks for the district names `Colombo` and `Kalmune` as stored in the source dataset.

## Python usage

```python
from denguedatahub import load_sl_province_districts

df = load_sl_province_districts()
print(df.head())
print(df.shape)
print(df["province"].unique())
```

The loader reads `denguedatahub/data/sl_province_districts.csv` using `pandas.read_csv()` and returns a `pandas.DataFrame`. It does not explicitly override pandas' inferred column types.

## Validation

The included test `tests/test_load_sl_province_districts.py` checks:

- That the result is a nonempty pandas DataFrame.
- The expected row count (26) and ordered column names.
- Nine distinct province names.
- The presence of representative district names.
- Exact R–Python equality of records, columns, values, and data types **when** an original R `.rda` file is supplied.

For the optional equivalence test, set the `DENGUEDATAHUB_SL_PROVINCE_DISTRICTS_RDA` environment variable to the original `.rda` file path and install `pyreadr`. If the file is unavailable, the test skips rather than confirming equivalence.

Run the dataset tests from the project root:

```powershell
pytest tests/test_load_sl_province_districts.py -v
```

## Original R source

Original dataset name: `sl_province_districts`.

Original documentation title: *Provinces and Districts of Sri Lanka*.

Source listed by the R package: [Ministry of Education, Sri Lanka — Provinces](https://moe.gov.lk/ministry-2/provinces/).

**Data note:** The original package reports 26 rows while describing the country's nine provinces and their districts. The Python implementation retains the packaged data; this page does not attempt to reconcile the row count with an external administrative listing.
