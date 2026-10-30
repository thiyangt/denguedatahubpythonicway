# denguedatahub — Python documentation

`denguedatahub` is a Python adaptation of the [original R `denguedatahub` package](https://github.com/thiyangt/denguedatahub), developed as part of the `denguedatahubpythonicway` project.

## Overview

The original R package brings together dengue-related data from different countries and regions. Its stated goal is to provide researchers with a unified collection of dengue data, including exogenous variables where available, to support understanding dengue spread and reproducible research. The R package describes weekly, monthly, and yearly summaries at state, province, and country levels.

This Python project makes the converted datasets available through Python loader functions and provides Python implementations of selected R-package utilities. Dataset availability and coverage depend on the individual source; not every dataset has every temporal or geographic level.

## Objectives

- Make the converted dengue datasets accessible as pandas DataFrames.
- Provide a Python interface to the converted functions.
- Document dataset structures, original sources, and practical usage.
- Support reproducible analysis using Python tools.

## Getting started

From the Python repository root, install the package in editable mode:

```bash
python -m pip install -e .
```

Example: load a dataset and inspect its contents.

```python
from denguedatahub import load_korea_dengue

korea = load_korea_dengue()
print(korea.head())
print(korea.shape)
```

For installation requirements and available dependencies, consult the repository's `pyproject.toml`.

## Documentation

### Datasets

The initial documentation scope is the **21 datasets** corresponding to the original R package's `data/` directory. Each dataset will have its own page in [`datasets/`](datasets/) covering its description, columns, source, and Python usage. Additional Python datasets will be considered separately.

### Functions

The [`functions/`](functions/) section will document converted utilities, including normalization and Sri Lankan Weekly Epidemiological Report (WER) processing. Only functions verified in the Python package will be documented as available.

### Getting started guide

A more detailed [`getting_started.md`](getting_started.md) guide is planned, including installation and usage examples.

## Original project and attribution

The original R package, [`thiyangt/denguedatahub`](https://github.com/thiyangt/denguedatahub), is authored and maintained by **Thiyanga S. Talagala**. Its package metadata identifies the license as **GPL-3**. Refer to the original repository for its official documentation, dataset references, and license details.

This Python adaptation is developed in [`thiyangt/denguedatahubpythonicway`](https://github.com/thiyangt/denguedatahubpythonicway). This documentation uses the R package as a reference while describing the Python implementation rather than reproducing the R API.

## Scope of this documentation

Documentation is being developed incrementally. The presence of a dataset or function in the original R package does not necessarily mean that an equivalent Python implementation is available. Consult the corresponding Python documentation page and package exports for supported usage.
