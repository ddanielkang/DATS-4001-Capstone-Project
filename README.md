# DATS 4001 Capstone Project (ALS Progression)

## Overview
This repository contains code and documentation for a capstone project focused on modeling ALS disease progression and outcomes using longitudinal clinical data.

## Repository Structure
- `data/`
  - `raw/` original source data (not committed)
  - `interim/` intermediate outputs
  - `processed/` analysis-ready datasets
- `notebooks/` exploratory and modeling notebooks
- `scripts/` reusable code (data prep, modeling, evaluation)
- `figures/` exported plots
- `docs/` proposal, weekly updates, workflow notes
- `models/` saved model artifacts (not committed by default)
- `reports/` report artifacts

## Reproducibility (Conda)
```bash
conda env create -f environment.yml
conda activate als-capstone
python -m ipykernel install --user --name als-capstone --display-name "ALS Capstone"

cat > docs/workflow/WORKFLOW.md <<'EOF'
# Workflow & Timeline

## Workflow
1. Store unmodified source files in `data/raw/` (not committed).
2. Clean and save analysis-ready datasets to `data/processed/`.
3. Use `notebooks/` for EDA and experiments (numbered notebooks).
4. Move reusable logic into `scripts/` (data prep, features, training, evaluation).
5. Save plots to `figures/` and report artifacts to `reports/`.
6. Keep proposal + weekly updates in `docs/`.

## Timeline
- Weeks 1–2: data understanding + cleaning pipeline
- Weeks 3–5: feature engineering + baseline models
- Weeks 6–8: survival/longitudinal modeling + validation
- Weeks 9–10: final analysis + report/presentation
