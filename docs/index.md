# denguedatahub — Python Documentation

## Introduction

`denguedatahub` is a Python adaptation of the R package [denguedatahub](https://github.com/thiyangt/denguedatahub), developed by Thiyanga S. Talagala. The original project aims to provide the research community with a unified collection of dengue-related data from around the world to support analysis of dengue spread and reproducible research.

This Python package provides access to converted datasets through Python loader functions and includes selected utilities adapted from the original R implementation.

## Objectives

- Make the original package's dengue datasets accessible in Python.
- Preserve the meaning and structure of the original datasets as closely as possible.
- Provide documented functions for loading and processing data.
- Support reproducible data analysis using Python.

## Documentation contents

### Datasets

The package includes Python loaders corresponding to the 21 datasets in the original R package's `data/` folder. Individual pages will be added under [`datasets/`](datasets/) as their documentation is reviewed.

### Functions

Documentation for converted utility functions, including normalization and Sri Lankan Weekly Epidemiological Report (WER) processing, will be added under [`functions/`](functions/).

## Basic usage

For example, load the Korea dengue dataset:

```python
from denguedatahub import load_korea_dengue

korea = load_korea_dengue()
print(korea.head())
```

## Original project and attribution

This project is based on the original [denguedatahub R package](https://github.com/thiyangt/denguedatahub). For original data descriptions, sources, and references, consult the corresponding R documentation files in its `man/` directory.

- Original package website: https://thiyangt.github.io/denguedatahubweb/
- Original R package license (per its DESCRIPTION file): GPL-3

## Documentation status

This documentation is being developed alongside the Python conversion. The presence of a loader file does not by itself establish complete functional equivalence with the original R implementation.
