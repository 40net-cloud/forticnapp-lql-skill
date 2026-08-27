---
name: forticnapp-lql
description: Author Lacework FortiCNAPP LQL queries and custom policies (compliance/violation policies for AWS, Azure, Google Cloud, OCI, Kubernetes, and workload/agent data). Use when writing or reviewing LQL, choosing FortiCNAPP datasources, or turning a compliance-standard control (CIS, etc.) into a FortiCNAPP policy.
---

# FortiCNAPP LQL query and policy authoring

LQL is FortiCNAPP's SQL-like query language. A query selects records from curated **datasources**; a **policy** wraps a query with metadata (severity, remediation, alerting) and evaluates it on a schedule. Source: FortiCNAPP 26.2 LQL Reference Guide.

## Query anatomy (the compliance-policy pattern)

```yaml
---
queryId: LW_Custom_MyPolicyQuery
queryText: |-
  {
      source {
          LW_CFG_AWS_EC2_EBS_ENCRYPTION_BY_DEFAULT
      }
      filter {
          RESOURCE_CONFIG:EbsEncryptionByDefault = 'false'
      }
      return distinct {
          ACCOUNT_ALIAS,
          ACCOUNT_ID as RESOURCE_KEY,
          RESOURCE_REGION,
          RESOURCE_TYPE,
          SERVICE,
          'EbsEncryptionNotEnabledByDefault' as COMPLIANCE_FAILURE_REASON
      }
  }
```

- The query is `{ source {…} filter {…} return [distinct] {…} }`. Filter is optional; source and return are required. Max 4096 chars. Keywords case-insensitive; datasource names and field names UPPERCASE; JSON keys inside `RESOURCE_CONFIG` are case-sensitive.
- JSON access: `RESOURCE_CONFIG:key.nested.key`. Quote keys that clash with keywords or contain special chars: `rules:"properties".access`. Cast with `::String`, `::Number`, `::Timestamp` when needed.
- Strings are single-quoted (`'true'`). Comparison to JSON booleans is typically against the strings `'true'`/`'false'` for AWS config data.
- Expand JSON arrays into rows in `source`: `LW_CFG_AWS_EC2_SECURITY_GROUPS a, array_to_rows(a.RESOURCE_CONFIG:IpPermissions) as (perm), array_to_rows(perm:IpRanges) as (r)`.
- Semi-join for "resource X lacking related record Y": `filter { RESOURCE_ID in { source {…} filter {…} return distinct { RESOURCE_ID } } }` (also `not in`).

**Policy-evaluation constraints** (queries used by policies): each result row must represent one violating resource. If the query uses `array_to_rows` or a MANY-cardinality datasource connection, it MUST use `return distinct` and may only return columns from the root datasource (filtering on expanded data is always allowed). The root (first) datasource defines what the policy is "about".

## Return-clause conventions per provider

Return the resource identity fields, aliasing the unique resource identifier `as RESOURCE_KEY`:

| Provider | Typical return fields |
| --- | --- |
| AWS | `ACCOUNT_ALIAS, ACCOUNT_ID, ARN as RESOURCE_KEY, RESOURCE_REGION, RESOURCE_TYPE, SERVICE` |
| Azure | `TENANT_ID, TENANT_NAME, SUBSCRIPTION_ID, SUBSCRIPTION_NAME, URN as RESOURCE_KEY, RESOURCE_REGION, RESOURCE_TYPE` |
| Google Cloud | `ORGANIZATION_ID, PROJECT_NUMBER, PROJECT_ID, FOLDER_IDS, URN as RESOURCE_KEY, RESOURCE_REGION, RESOURCE_TYPE, SERVICE` |
| OCI | `COMPARTMENT_ID, RESOURCE_KEY, RESOURCE_REGION, RESOURCE_TYPE, SERVICE` |

Optionally add a literal `'Reason' as COMPLIANCE_FAILURE_REASON`.

## Choosing a datasource

Config datasources are named `LW_CFG_<PROVIDER>_<SERVICE>_<API>` and mirror the provider's describe/list APIs; each row is one resource with its config in the JSON `RESOURCE_CONFIG` field and common identity columns (see the per-provider reference file headers). **Do not read a whole datasource reference file — grep it for the service name**, e.g. `grep -i -A5 'cloudtrail' references/datasources-aws.md`.

| Reference file | Contents |
| --- | --- |
| `references/datasources-aws.md` | AWS config (`LW_CFG_AWS_*`) + CloudTrail activity (`CloudTrailRawEvents`) |
| `references/datasources-azure.md` | Azure Resource Graph + Azure AD (`LW_CFG_AZURE_*`) |
| `references/datasources-gcp.md` | Google Cloud config (`LW_CFG_GCP_*`) + audit log activity (`LW_ACT_GCP_ACTIVITY`) |
| `references/datasources-oci.md` | OCI config (`LW_CFG_OCI_*`) |
| `references/datasources-agent-k8s.md` | Agent/workload (`LW_HA_*` activity, `LW_HE_*` entities incl. K8s pods/containers), attack path (`LW_APA_*`), entitlements (`LW_CE_*`) — full field lists |

The guide does **not** document the JSON schema inside `RESOURCE_CONFIG`. To discover field names: consult the underlying cloud API (each datasource maps to a named API call, e.g. `acm list-certificates`), or run an explore query returning bare `RESOURCE_CONFIG` via `lacework query run -f explore.yaml`, or `lacework query show-source <DATASOURCE>` / `preview-source`.

## Workflow: compliance control → policy

1. **Pick the datasource(s)**: grep the provider reference file for the service.
2. **Discover `RESOURCE_CONFIG` fields** (see above) — never guess key names silently; verify casing against the cloud API.
3. **Write the query YAML** (`queryId` + `queryText`, as in the anatomy example) targeting *non-compliant* resources; respect the policy-evaluation constraints.
4. **Test**: `lacework query create -f q.yaml` (or `run -f` without saving), then `lacework query run <queryId>`.
5. **Wrap in a policy** and create it: `lacework policy create -f p.yaml`:

```yaml
---
title: Security Groups Should Not Allow Unrestricted Ingress to TCP Port 445
enabled: false            # true once validated
policyType: Violation
alertEnabled: false
alertProfile: LW_CFG_AWS_DEFAULT_PROFILE.CFG_AWS_Violation   # Azure: LW_CFG_AZURE_DEFAULT_PROFILE.Violation; GCP: LW_CFG_GCP_DEFAULT_PROFILE.Violation; OCI: LW_CFG_OCI_DEFAULT_PROFILE.Violation
evalFrequency: Daily      # Hourly|Daily
queryId: LW_Custom_UnrestrictedIngressToTCP445
severity: high            # critical|high|medium|low|info
description: Security groups should not allow unrestricted ingress to TCP port 445
remediation: Steps to remediate, shown in the violation
```

API equivalent: `POST /api/v2/Queries` then `POST /api/v2/Policies` (queryText as a single line inside JSON).

## Detailed references (load on demand)

- `references/syntax.md` — full grammar: data types, strings/identifiers, JSON access & casting, `source`/`filter`/`return` details, joining/connecting datasources (`with`, named paths, cardinality), `array_to_rows`, query types (single/join/semi-join), policy-eval limitations, regex syntax, all operators (`LIKE`, `RLIKE`, `IN`, `BETWEEN`, set ops, `CASE`…).
- `references/functions.md` — all LQL functions (string, timestamp, JSON/array, net: `IP_CONTAINS`, `ARRAY_TO_ROWS`, `COALESCE`, `VALUE_EXISTS`, …). Grep by name or keyword.
- `references/examples.md` — 15 worked queries (AWS compliance checks, tag checks, CloudTrail activity, K8s) with the API calls to run them.

When unsure between reading and grepping: grep first; read only the matched section.
