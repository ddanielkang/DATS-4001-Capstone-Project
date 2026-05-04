# DATS 4001 Capstone Project (ALS Progression)

## Overview
This repository contains code, documentation, figures, reports, and presentation materials for my DATS 4001 capstone project on predicting ALS disease progression using longitudinal clinical data.

The project focuses on modeling ALSFRS-R total score over time using patient visit history. ALSFRS-R ranges from 0 to 48, where higher scores indicate better function and lower scores indicate greater impairment. The final workflow uses PRO-ACT as the main modeling dataset and Target ALS as supplementary clinical context.

## Main Research Question
Can longitudinal patient history and clinical features be used to predict future ALSFRS-R scores, and how does prediction error vary across disease severity groups?

## Repository Structure
- `code/`
  - `README.md` final code submission notes and reproduction instructions
- `data/`
  - `raw/` original source data
  - `interim/` intermediate outputs
  - `processed/` analysis-ready datasets
- `docs/`
  - `planning/` preprocessing plans and variable selection notes
  - `proposal/` project proposal
  - `weekly-updates/` weekly progress updates
- `figures/` exported plots 
- `notebooks/` notebooks reflecting workflow
- `poster/` final research poster
- `presentation/` product demonstration presentation 
- `report/` final report and individual reflection
- `reports/` generated CSV outputs
- `scripts/` reusable Python code for data loading and preprocessing
- `acknowledgements.txt` supporting resources, tools, datasets, AI-use notes
- `environment.yml` Conda environment file

## Reproducibility 

The project was developed using Python 3.11 in a Conda environment.

```bash
conda env create -f environment.yml
conda activate als-capstone
python -m ipykernel install --user --name als-capstone --display-name "ALS Capstone"