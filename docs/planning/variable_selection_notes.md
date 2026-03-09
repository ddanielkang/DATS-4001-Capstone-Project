# Variable Selection Notes

| Dataset | Variable | Role | Keep? | Notes |
|---|---|---|---|---|
| PRO-ACT ALSFRS | subject_id | identifier | Keep | patient key |
| PRO-ACT ALSFRS | alsfrs_delta | time | Keep | visit ordering variable |
| PRO-ACT ALSFRS | alsfrs_r_total | target | Keep | primary ALS progression outcome |
| PRO-ACT ALSFRS | alsfrs_total | alternate target | Maybe | may be useful for comparison |
| PRO-ACT Demographics | subject_id | identifier | Keep | merge key |
| PRO-ACT Demographics | age / sex fields | baseline features | Keep | static patient-level covariates |
| PRO-ACT ALS History | subject_id | identifier | Keep | merge key |
| PRO-ACT ALS History | onset/history variables | baseline clinical features | Maybe | evaluate completeness and relevance |
| PRO-ACT Treatment | subject_id | identifier | Maybe | likely repeated table |
| PRO-ACT Death Data | subject_id | follow-up outcome key | Maybe | may support later survival analysis |
| Target ALS AGRI Clinical | subject identifier | external alignment | Maybe | requires harmonization before use |