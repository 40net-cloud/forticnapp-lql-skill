<!-- Generated from FortiCNAPP 26.2 LQL Reference Guide (fetched 2026-10-28). Source:
     https://docs.fortinet.com/document/forticnapp/latest/lql-reference/771173/datasource-metadata -->

# Datasource Metadata

## Cloud Entitlement Datasources

### LW_CE_ENTITLEMENTS

Details about cloud entitlements associated with identities

- `RECORD_CREATED_TIME` (Timestamp) — Record creation time
- `PRINCIPAL_ID` (String) — Identity principal ID
- `PROVIDER_TYPE` (String) — Cloud or service domain provider
- `DOMAIN_ID` (String) — Domain identifier within the provider type
- `SERVICE` (JSON) — Service name
- `RESOURCE_TYPE` (String) — Resource type
- `RESOURCE_ID` (String) — Resource identifier
- `POLICY_ID` (String) — Policy identifier
- `ACTION` (String) — Action
- `LAST_USED_TIME` (Timestamp) — Last used time

### LW_CE_IDENTITIES

Details about cloud identities

- `RECORD_CREATED_TIME` (Timestamp) — Record creation time
- `PRINCIPAL_ID` (String) — Identity principal ID
- `PROVIDER_TYPE` (String) — Cloud or service domain provider
- `DOMAIN_ID` (String) — Domain identifier within the provider type
- `NAME` (JSON) — Friendly name for the identity
- `LAST_USED_TIME` (Timestamp) — Last used time
- `CREATED_TIME` (Timestamp) — Created time
- `METRICS` (JSON) — Metrics data from computed entitlements and configuration
- `TAGS` (JSON) — Tags
- `ACCESS_KEYS` (JSON) — Access key summaries

### LW_CE_LINKED_IDENTITIES

Details about cloud linked identities

- `RECORD_CREATED_TIME` (Timestamp) — Record creation time
- `PRINCIPAL_ID` (String) — Identity principal ID
- `NAME` (JSON) — Friendly name for the identity
- `LINKED_PRINCIPAL_ID` (String) — Linked identity principal ID
- `LINKED_NAME` (JSON) — Friendly name for the linked identity
- `RELATION_TYPE` (String) — Type of linked relationship

### LW_CE_REMEDIATIONS

Details about cloud identity remediations

- `RECORD_CREATED_TIME` (Timestamp) — Record creation time
- `REMEDIATION_KEYS` (JSON) — Identity principal ID
- `REMEDIATION_TYPE` (String) — Type of remediation
- `METRICS` (JSON) — Metrics data from computed remediation effect
