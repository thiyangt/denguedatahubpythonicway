
"""
Python equivalent of data-raw/cdc/cdc.R.

Loads the six CDC dengue datasets using
their individual Python loader functions.
"""

from .load_cdc_dengue_countyyear import load_cdc_dengue_countyyear
from .load_cdc_dengue_agesex import load_cdc_dengue_agesex
from .load_cdc_casesby_week import load_cdc_casesby_week
from .load_cdc_dengue_casesbyjurisdiction import load_cdc_dengue_casesbyjurisdiction
from .load_cdc_local_dengue_cases import load_cdc_local_dengue_cases
from .load_cdc_travel_associated_dengue_cases import load_cdc_travel_associated_dengue_cases


def load_cdc_data():
    """
    Load all six CDC dengue datasets.

    Returns
    -------
    dict
        Dictionary containing six pandas DataFrames.
    """

    return {
        "cdc_dengue_countyyear": load_cdc_dengue_countyyear(),
        "cdc_dengue_agesex": load_cdc_dengue_agesex(),
        "cdc_casesby_week": load_cdc_casesby_week(),
        "cdc_dengue_casesbyjurisdiction": load_cdc_dengue_casesbyjurisdiction(),
        "cdc_local_dengue_cases": load_cdc_local_dengue_cases(),
        "cdc_travel_associated_dengue_cases": load_cdc_travel_associated_dengue_cases()
    }
