# `min_max` — Min–max normalization

## Description

Apply min–max normalization to a numeric column in a pandas DataFrame, either across all rows or separately within groups. This is the Python counterpart of the original R package's `min_max` function.

For a value \(x\), the transformation is:

\[
\frac{x - x_{\min}}{x_{\max} - x_{\min}}
\]

## Usage

```python
from denguedatahub import min_max

result = min_max(data, variable_to_minmax, local=False, group_var=None)
```

## Parameters

| Parameter | Type | Description |
|---|---|---|
| `data` | `pandas.DataFrame` | Input DataFrame containing the values to normalize. |
| `variable_to_minmax` | `str` | Name of the numeric column to normalize. |
| `local` | `bool`, default `False` | If `False`, normalize the whole column. If `True`, normalize separately within groups. |
| `group_var` | `str` or `None`, default `None` | Column identifying groups when `local=True`. |

## Returns

A **new `pandas.DataFrame`** containing the original columns and the following additional columns:

| Mode | Added columns | Meaning |
|---|---|---|
| Global (`local=False`) | `min.cases`, `max.cases`, `minmax.cases` | Overall minimum, overall maximum, and normalized value. |
| Group-wise (`local=True`) | `min.group`, `max.group`, `minmax.group` | Group minimum, group maximum, and normalized value. |

The original DataFrame is not modified.

## Examples

### Global normalization

```python
import pandas as pd
from denguedatahub import min_max

data = pd.DataFrame({"cases": [10, 20, 30]})
result = min_max(data, "cases")
print(result)
```

Expected `minmax.cases` values: `0.0`, `0.5`, `1.0`.

### Group-wise normalization

```python
import pandas as pd
from denguedatahub import min_max

data = pd.DataFrame({
    "district": ["A", "A", "A", "B", "B", "B"],
    "cases": [10, 20, 30, 100, 150, 200],
})

result = min_max(data, "cases", local=True, group_var="district")
print(result[["district", "cases", "minmax.group"]])
```

Expected `minmax.group` values: `0.0`, `0.5`, `1.0` for each district.

## Notes

- Missing numeric values remain missing in the normalized result; pandas calculates minima and maxima while skipping missing values by default.
- When the minimum and maximum are equal, the denominator is zero. The current implementation does not handle this case explicitly, so normalized values may be `NaN`.
- Use a valid grouping column when `local=True`; the function does not perform explicit input validation.
- The added output column names are fixed, even if the input column is not named `cases`.

## Original R reference

The original R documentation is `man/min_max.Rd` in [thiyangt/denguedatahub](https://github.com/thiyangt/denguedatahub). The R function uses arguments `variable.to.minmax`, `local`, and `group.var`; the Python version uses `variable_to_minmax`, `local`, and `group_var`.
