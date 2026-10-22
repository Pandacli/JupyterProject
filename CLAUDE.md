# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project overview

Personal Python/Jupyter learning workspace for AI/ML and data science topics. This is a PyCharm project using Python 3.12 (`py312` SDK). No build system, test framework, or linter is configured.

## Repository structure

- `CN-AI-Trainer/` — Markdown knowledge base for the China AI Trainer (Level 3) national certification. 13 chapters covering ML model types, regression, statistical tests, HMM, convolutions, text annotation, class imbalance, dataset partitioning, and overfitting.
- `trainnerLevel3/` — Structured AI Trainer Level 3 coursework organized in numbered subdirectories (`1.1.1` through `4.2.5`). Contains Jupyter-notebook-derived HTML files under `htmls/`, reference `.doc` files under `document/`, and one Python utility at `3.2.5/vision/utils/box_utils_numpy.py` (bounding box operations with NumPy).
- `python_base/` — Basic Python Jupyter notebooks (functions, return values).
- `pandas/` — Pandas practice notebook.
- `numpy/` — NumPy quick-start notebook.
- `matplotlib/` — Matplotlib plotting sample notebook.
- `mongodb/` — MongoDB usage example notebook.
- `dataset_demo/` — NBA career stats dataset demo notebook.
- `data/` — Data directory (currently empty).
- `models/` — Models directory (currently empty; excluded from PyCharm indexing).

## Working with notebooks

All `.ipynb` files are Jupyter notebooks. Use `NotebookEdit` to modify cells. To run notebooks locally, start a Jupyter server with `jupyter notebook` or `jupyter lab` from the repo root. Notebooks assume dependencies like `pandas`, `numpy`, `matplotlib`, and `pymongo` are available in the `py312` environment.
