import pandas as pd
from pathlib import Path

# Repo root = one level above /scripts
REPO_ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = REPO_ROOT / "data" / "raw"

def load_proact_alsfrs():
    return pd.read_csv(RAW_DIR / "proact" / "F_PROACT_ALSFRS.csv")

def load_proact_demographics():
    return pd.read_csv(RAW_DIR / "proact" / "F_PROACT_DEMOGRAPHICS.csv")

def load_proact_als_history():
    return pd.read_csv(RAW_DIR / "proact" / "F_PROACT_ALSHISTORY.csv")

def load_proact_deathdata():
    return pd.read_csv(RAW_DIR / "proact" / "F_PROACT_DEATHDATA.csv")

def load_proact_treatment():
    return pd.read_csv(RAW_DIR / "proact" / "F_PROACT_TREATMENT.csv")

def load_targetals_agri_clinical():
    return pd.read_csv(RAW_DIR / "target_als" / "collections.natural_history_study.clinical_data.csv")