# Preprocessing Plan

## Key variables
- `subject_id`: patient identifier
- `alsfrs_delta`: longitudinal ordering / time variable
- `alsfrs_r_total`: primary progression target

## Planned feature structure
- One row will represent one patient visit.
- Static baseline features will later be merged from demographics and ALS history.
- Treatment and death data will be evaluated separately before inclusion.
- Target ALS AGRI clinical data will require separate alignment before integration.

## Main issues identified
- Different datasets play different roles (visit-level vs patient-level).
- Missingness varies across tables and may limit which variables are used early.
- Target ALS will need additional harmonization before merging with PRO-ACT.