import pandas as pd


def min_max(data, variable_to_minmax, local=False, group_var=None):
    """
    Apply min-max normalization to a column in a pandas DataFrame.

    Parameters
    ----------
    data : pandas.DataFrame
        DataFrame containing the data.

    variable_to_minmax : str
        Name of the column to normalize.

    local : bool, default=False
        If False, apply normalization to the whole column.
        If True, apply normalization separately within each group.

    group_var : str, optional
        Column used for grouping when local=True.

    Returns
    -------
    pandas.DataFrame
        DataFrame with min-max normalized values.
    """

    data = data.copy()

    if not local:
        min_value = data[variable_to_minmax].min()
        max_value = data[variable_to_minmax].max()

        data["min.cases"] = min_value
        data["max.cases"] = max_value
        data["minmax.cases"] = (
            (data[variable_to_minmax] - min_value)
            / (max_value - min_value)
        )

    else:
        data["min.group"] = data.groupby(group_var)[
            variable_to_minmax
        ].transform("min")

        data["max.group"] = data.groupby(group_var)[
            variable_to_minmax
        ].transform("max")

        data["minmax.group"] = (
            (data[variable_to_minmax] - data["min.group"])
            / (data["max.group"] - data["min.group"])
        )

    return data