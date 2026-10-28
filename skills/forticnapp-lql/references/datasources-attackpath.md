<!-- Generated from FortiCNAPP 26.2 LQL Reference Guide (fetched 2026-10-28). Source:
     https://docs.fortinet.com/document/forticnapp/latest/lql-reference/771173/datasource-metadata -->

# Datasource Metadata

## Attack Path Analysis Datasources

Query the following datasources for information about Attack Path Analysis.

### LW_APA_ATTACK_PATHS

Details about cloud resource attack paths

- `RECORD_CREATED_TIME` (Timestamp) — Record creation time
- `PATH_ID` (String) — Path ID
- `PROVIDER_TYPE` (String) — Cloud or service domain provider
- `DOMAIN_ID` (String) — Domain identifier within the provider type
- `METRICS` (JSON) — Path metrics
| Path | JSON | Path elements |
- `TARGETS` (JSON) — Path targets

### LW_APA_EXPOSURE_PATHS

Details about cloud resource exposure paths

- `RECORD_CREATED_TIME` (Timestamp) — Record creation time
- `PATH_ID` (String) — Path ID
- `PATH_TYPE` (String) — Path type
- `PROVIDER_TYPE` (String) — Cloud or service domain provider
- `DOMAIN_ID` (String) — Domain identifier within the provider type
- `METRICS` (JSON) — Path metrics
- `TARGET_ID` (String) — Target ID
- `TARGET_TYPE` (String) — Target type
- `TARGET_TAGS` (JSON) — Target resource tags
