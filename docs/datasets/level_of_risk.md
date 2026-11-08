# `level_of_risk`

## Description

Country-wise dengue risk levels around the world, based on information attributed to the U.S. Centers for Disease Control and Prevention (CDC). This dataset is a historical snapshot and should not be interpreted as a live or current travel-health risk assessment.

The original R documentation describes the dataset as **“Level of Dengue risk around the world”** and cites the CDC's 2024 dengue risk information. It also mentions a last-accessed date of **18 January 2023**; the dates stored in the dataset range from **16 January 2023** to **3 September 2024**. These are distinct statements in the source material and are not reconciled here.

## Python function

```python
from denguedatahub import load_level_of_risk

df = load_level_of_risk()
print(df.head())
```

**Signature:** `load_level_of_risk()`

**Parameters:** None.

**Returns:** `pandas.DataFrame` with 293 rows and 4 columns.

## Dataset structure

| Column | Description | Python data type |
|---|---|---|
| `country` | Country name | `object` (string values) |
| `level_of_risk` | Dengue risk classification | `object` (string values) |
| `region` | Geographic region | `object` (string values) |
| `last_accessed` | Date associated with the recorded risk information | `datetime64[ns]` |

The original R documentation describes three categories: **Frequent or continuous**, **Sporadic or uncertain**, and **Varies by region**. It defines frequent/continuous risk as evidence of more than 10 dengue cases in at least three of the previous ten years, and sporadic/uncertain risk as evidence of at least one locally acquired case in the previous ten years. The actual CSV may use abbreviated punctuation or capitalization (for example, `Sporadic/Uncertain`).

## Dataset characteristics

The Python test checks the following properties:

- **293** records and **4** columns, in the order shown above.
- **162** distinct country values, **3** risk levels, **5** regions, and **2** distinct `last_accessed` dates.
- No missing values in the loaded DataFrame.
- Earliest recorded `last_accessed`: `2023-01-16`; latest: `2024-09-03`.
- Row 177 (zero-based index 176) contains `São Tomé and Príncipe`, `Sporadic/Uncertain`, `Africa`, and `2024-09-03`.

## Examples

Inspect the dataset:

```python
from denguedatahub import load_level_of_risk

df = load_level_of_risk()
print(df.shape)
print(df.dtypes)
print(df.head())
```

Filter to a particular risk level:

```python
sporadic = df[df["level_of_risk"] == "Sporadic/Uncertain"]
print(sporadic[["country", "region", "last_accessed"]].head())
```

Count records by risk category:

```python
print(df["level_of_risk"].value_counts())
```

## Implementation notes

The loader reads the packaged file `denguedatahub/data/level_of_risk.csv` with `pandas.read_csv`, specifies UTF-8 encoding, and parses the `last_accessed` column as dates. It does not retrieve current CDC data from the internet.

The Python test checks dimensions, column names, missing values, types, distinct counts, date boundaries, and the corrected UTF-8 country name. The project previously performed a full comparison with the original R dataset; the provided test file itself does **not** contain a full R–Python equivalence test.

## Source and attribution

Original R package: [`denguedatahub`](https://github.com/thiyangt/denguedatahub), dataset `level_of_risk`.

Original documentation source: [CDC — Areas with Risk of Dengue](https://www.cdc.gov/dengue/areas-with-risk/index.html).

The source page may change after the historical data was collected. For current risk guidance, consult the CDC directly.
