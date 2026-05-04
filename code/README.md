# Code README

## Folder Structure

The executable code for this project is stored in the root level `notebooks/` and `scripts/` folders.

- `notebooks/` contains numbered Jupyter notebooks for data inspection, preprocessing, EDA, feature engineering, modeling, validation, results refinement, and demo preparation.
- `scripts/` contains reusable Python scripts for data loading and preprocessing.
- `environment.yml` in the repository root defines the Conda environment needed to reproduce the analysis.

The code was kept at the root level to preserve the relative paths used throughout the notebooks and scripts.

## Dependencies
The project was developed in Python using the following main libraries:

- pandas
- NumPy
- matplotlib
- scikit-learn
- Jupyter Notebook / Jupyter Lab

To recreate the environment:

```bash
conda env create -f environment.yml
conda activate als-capstone
python -m ipykernel install --user --name als-capstone --display-name "ALS Capstone"