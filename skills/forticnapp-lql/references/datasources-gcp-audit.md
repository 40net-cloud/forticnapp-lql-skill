<!-- Generated from FortiCNAPP 26.2 LQL Reference Guide (fetched 2026-10-28). Source:
     https://docs.fortinet.com/document/forticnapp/latest/lql-reference/771173/datasource-metadata -->

# Datasource Metadata

## Google Cloud Audit Log Activity

### LW_ACT_GCP_ACTIVITY

The `LW_ACT_GCP_ACTIVITY` datasource contains events for the Pub/Sub-based audit log integration.

- `INSERT_ID` (Number) — Unique ID for each entry
- `INSERT_TIME` (Timestamp) — Time the data was inserted into the table
- `EVENT_TIME` (Timestamp) — Time the event occurred
- `EVENT` (JSON) — JSON description of the event
- `ORGANIZATION_ID` (String) — Organization identifier
- `PROJECT_ID` (String) — Project identifier
- `EVENT_SOURCE` (String) — API that generated the event
- `EVENT_NAME` (String) — Method on the API invoked for this event
- `ERROR_CODE` (String) — Error code returned for this event
