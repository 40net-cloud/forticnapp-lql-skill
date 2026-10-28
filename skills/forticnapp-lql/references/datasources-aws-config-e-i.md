<!-- Generated from FortiCNAPP 26.2 LQL Reference Guide (fetched 2026-10-28). Source:
     https://docs.fortinet.com/document/forticnapp/latest/lql-reference/771173/datasource-metadata -->

# Datasource Metadata

## AWS Configuration Datasources

All AWS configuration datasources listed in this section contain these common fields:

- `BATCH_START_TIME` (Timestamp) — Beginning of time interval
- `BATCH_END_TIME` (Timestamp) — End of time interval
- `QUERY_START_TIME` (Timestamp) — Start time of query for this resource
- `QUERY_END_TIME` (Timestamp) — End time of query for this resource
- `ARN` (String) — ARN for the resource
- `API_KEY` (String) — Key describing the API used to fetch data for this resource
- `SERVICE` (String) — Service this resource belongs to
- `ACCOUNT_ID` (String) — AWS Account identifier
- `ACCOUNT_ALIAS` (String) — User friendly alias for AWS Account
- `RESOURCE_TYPE` (String) — Type of this resource
- `RESOURCE_ID` (String) — Identifier for this resource
- `RESOURCE_REGION` (String) — Region this resource belongs to
- `RESOURCE_CONFIG` (JSON) — JSON Definition of this resource
- `RESOURCE_TAGS` (JSON) — Tags associated with this resource

### Elastic Container Registry Public

- `LW_CFG_AWS_ECR_PUBLIC_GET_REGISTRY_CATALOG_DATA` — ecr-public `get-regstry-catalog-data`
- `LW_CFG_AWS_ECR_PUBLIC_GET_REPOSITORY_CATALOG_DATA` — ecrpublic `get-repository-catalog-data`
- `LW_CFG_AWS_ECR_PUBLIC_GET_REPOSITORY_POLICY` — ecr-public `get-repository-policy`
- `LW_CFG_AWS_ECR_PUBLIC_IMAGES` — ecr-public `describe-images`
- `LW_CFG_AWS_ECR_PUBLIC_IMAGE_TAGS` — ecr-public `describe-image-tags`
- `LW_CFG_AWS_ECR_PUBLIC_REGISTRIES` — ecr-public `describe-registries`
- `LW_CFG_AWS_ECR_PUBLIC_REPOSITORIES` — ecr-public `describe-repositories`

### ElastiCache

- `LW_CFG_AWS_ELASTICACHE_CACHE_CLUSTERS` — Amazon ElastiCache `describe-cache-clusters`
- `LW_CFG_AWS_ELASTICACHE_DESCRIBE_REPLICATION_GROUPS` — Amazon ElastiCache `describe-replication-groups`

### ELB

- `LW_CFG_AWS_ELB` — elb `describe-load-balancers`
- `LW_CFG_AWS_ELB_DESCRIBE_LOAD_BALANCER_ATTRIBUTES` — Elastic Load Balancing `describe-load-balancer-attributes`
- `LW_CFG_AWS_ELB_DESCRIBE_POLICIES` — elb `describe-load-balancer-policies`

### ELBv2

- `LW_CFG_AWS_ELBV2` — elbv2 `describe-load-balancers`
- `LW_CFG_AWS_ELBV2_DESCRIBE_ATTRIBUTES` — elbv2 `describe-load-balancer-attributes`
- `LW_CFG_AWS_ELBV2_DESCRIBE_LISTENERS` — elbv2 `describe-listeners`
- `LW_CFG_AWS_ELBV2_RULES` — elbv2 `describe-rules`
- `LW_CFG_AWS_ELBV2_SSL_POLICIES` — elbv2 `describe-ssl-policies`
- `LW_CFG_AWS_ELBV2_TARGET_GROUPS` — elbv2 `describe-target-groups`
- `LW_CFG_AWS_ELBV2_TARGET_HEALTH` — elbv2 `describe-target-health`

### EMR

- `LW_CFG_AWS_EMR_CLUSTERS` — emr `list-clusters`
- `LW_CFG_AWS_EMR_DESCRIBE_CLUSTER` — emr `describe-cluster`
- `LW_CFG_AWS_EMR_DESCRIBE_SECURITY_CONFIGURATION` — emr `describe-security-configuration`
- `LW_CFG_AWS_EMR_GET_BLOCK_PUBLIC_ACCESS_CONFIGURATION` — emr `get-block-public-access-configuration`
- `LW_CFG_AWS_EMR_INSTANCES` — emr `list-instances`
- `LW_CFG_AWS_EMR_INSTANCE_FLEETS` — emr `list-instance-fleets`

### ES

- `LW_CFG_AWS_ES` — es `list-domain-names`
- `LW_CFG_AWS_ES_DESCRIBE_DOMAIN` — es `describe-elasticsearch-domain`

### EventBridge

- `LW_CFG_AWS_EVENTS_API_DESTINATIONS` — Amazon EventBridge `list-api-destinations`
- `LW_CFG_AWS_EVENTS_ARCHIVES` — Amazon EventBridge `list-archives`
- `LW_CFG_AWS_EVENTS_CONNECTIONS` — Amazon EventBridge `list-connections`
- `LW_CFG_AWS_EVENTS_DESCRIBE_API_DESTINATION` — Amazon EventBridge `describe-api-destination`
- `LW_CFG_AWS_EVENTS_DESCRIBE_ARCHIVE` — Amazon EventBridge `describe-archive`
- `LW_CFG_AWS_EVENTS_DESCRIBE_CONNECTION` — Amazon EventBridge `describe-connection`
- `LW_CFG_AWS_EVENTS_DESCRIBE_EVENT_BUS` — Amazon EventBridge `describe-event-bus`
- `LW_CFG_AWS_EVENTS_DESCRIBE_EVENT_SOURCE` — Amazon EventBridge `describe-event-source`
- `LW_CFG_AWS_EVENTS_DESCRIBE_REPLAY` — Amazon EventBridge `describe-replay`
- `LW_CFG_AWS_EVENTS_DESCRIBE_RULE` — Amazon EventBridge `describe-rule`
- `LW_CFG_AWS_EVENTS_EVENT_BUSES` — Amazon EventBridge `list-event-buses`
- `LW_CFG_AWS_EVENTS_EVENT_SOURCES` — Amazon EventBridge `list-event-sources`
- `LW_CFG_AWS_EVENTS_REPLAYS` — Amazon EventBridge `list-replays`
- `LW_CFG_AWS_EVENTS_RULES` — Amazon EventBridge `list-rules`

### EventBridge Scheduler

- `LW_CFG_AWS_SCHEDULER_GET_SCHEDULE` — Results from Amazon EventBridge Scheduler 'get-schedule'
- `LW_CFG_AWS_SCHEDULER_GET_SCHEDULE_GROUP` — Results from Amazon EventBridge Scheduler 'get-schedule-group'
- `LW_CFG_AWS_SCHEDULER_SCHEDULES` — Results from Amazon EventBridge Scheduler 'list-schedules'
- `LW_CFG_AWS_SCHEDULER_SCHEDULE_GROUPS` — Results from Amazon EventBridge Scheduler 'list-schedule-groups'

### Fault Injection Service

- `LW_CFG_AWS_FIS_ACTIONS` — fis `list-actions`
- `LW_CFG_AWS_FIS_EXPERIMENTS` — fis `list-experiments`
- `LW_CFG_AWS_FIS_EXPERIMENT_RESOLVED_TARGETS` — fis `list-experiment-resolved-targets`
- `LW_CFG_AWS_FIS_EXPERIMENT_TEMPLATES` — fis `list-experiment-templates`
- `LW_CFG_AWS_FIS_GET_ACTION` — fis `get-action`
- `LW_CFG_AWS_FIS_GET_EXPERIMENT` — fis `get-experiment`
- `LW_CFG_AWS_FIS_GET_EXPERIMENT_TEMPLATE` — fis `get-experiment-template`
- `LW_CFG_AWS_FIS_TARGET_ACCOUNT_CONFIGURATIONS` — fis `list-target-account-configuration`

### Forecast Service

- `LW_CFG_AWS_FORECAST_DATASETS` — Results from Amazon Forecast Service 'list-datasets'
- `LW_CFG_AWS_FORECAST_DATASET_GROUP` — Results from Amazon Forecast Service 'describe-dataset-group'
- `LW_CFG_AWS_FORECAST_DATASET_GROUPS` — Results from Amazon Forecast Service 'list-dataset-groups'
- `LW_CFG_AWS_FORECAST_DATASET_IMPORT_JOBS` — Results from Amazon Forecast Service 'list-dataset-import-jobs'
- `LW_CFG_AWS_FORECAST_DESCRIBE_AUTO_PREDICTOR` — Results from Amazon Forecast Service 'describe-auto-predictor'
- `LW_CFG_AWS_FORECAST_DESCRIBE_DATASET` — Results from Amazon Forecast Service 'describe-dataset'
- `LW_CFG_AWS_FORECAST_DESCRIBE_DATASET_IMPORT_JOB` — Results from Amazon Forecast Service 'describe-dataset-import-job'
- `LW_CFG_AWS_FORECAST_DESCRIBE_EXPLAINABILITY` — Results from Amazon Forecast Service 'describe-explainability'
- `LW_CFG_AWS_FORECAST_DESCRIBE_EXPLAINABILITY_EXPORT` — Results from Amazon Forecast Service 'describe-explainability-export'
- `LW_CFG_AWS_FORECAST_DESCRIBE_FORECAST_EXPORT_JOB` — Results from Amazon Forecast Service 'describe-forecast-export-job'
- `LW_CFG_AWS_FORECAST_DESCRIBE_MONITOR` — Results from Amazon Forecast Service 'describe-monitor'
- `LW_CFG_AWS_FORECAST_DESCRIBE_PREDICTOR` — Results from Amazon Forecast Service 'describe-predictor'
- `LW_CFG_AWS_FORECAST_DESCRIBE_PREDICTOR_BACKTEST_EXPORT_JOB` — Results from Amazon Forecast Service 'describe-predictor-backtest-export-job'
- `LW_CFG_AWS_FORECAST_DESCRIBE_WHAT_IF_ANALYSIS` — Results from Amazon Forecast Service 'describe-what-if-analysis'
- `LW_CFG_AWS_FORECAST_DESCRIBE_WHAT_IF_FORECAST` — Results from Amazon Forecast Service 'describe-what-if-forecast'
- `LW_CFG_AWS_FORECAST_EXPLAINABILITIES` — Results from Amazon Forecast Service 'list-explainabilities'
- `LW_CFG_AWS_FORECAST_EXPLAINABILITY_EXPORTS` — Results from Amazon Forecast Service 'list-explainability-exports'
- `LW_CFG_AWS_FORECAST_FORECAST` — Results from Amazon Forecast Service 'describe-forecast'
- `LW_CFG_AWS_FORECAST_FORECASTS` — Results from Amazon Forecast Service 'list-forecasts'
- `LW_CFG_AWS_FORECAST_FORECAST_EXPORT_JOBS` — Results from Amazon Forecast Service 'list-forecast-export-jobs'
- `LW_CFG_AWS_FORECAST_GET_ACCURACY_METRICS` — Results from Amazon Forecast Service 'get-accuracy-metrics'
- `LW_CFG_AWS_FORECAST_MONITORS` — Results from Amazon Forecast Service 'list-monitors'
- `LW_CFG_AWS_FORECAST_MONITOR_EVALUATIONS` — Results from Amazon Forecast Service 'list-monitor-evaluations'
- `LW_CFG_AWS_FORECAST_PREDICTORS` — Results from Amazon Forecast Service 'list-predictors'
- `LW_CFG_AWS_FORECAST_PREDICTOR_BACKTEST_EXPORT_JOBS` — Results from Amazon Forecast Service 'list-predictor-backtest-export-jobs'
- `LW_CFG_AWS_FORECAST_WHAT_IF_ANALYSES` — Results from Amazon Forecast Service 'list-what-if-analyses'
- `LW_CFG_AWS_FORECAST_WHAT_IF_FORECASTS` — Results from Amazon Forecast Service 'list-what-if-forecasts'
- `LW_CFG_AWS_FORECAST_WHAT_IF_FORECAST_EXPORT` — Results from Amazon Forecast Service 'describe-what-if-forecast-export'
- `LW_CFG_AWS_FORECAST_WHAT_IF_FORECAST_EXPORTS` — Results from Amazon Forecast Service 'list-what-if-forecast-exports'

### Free Tier

- `LW_CFG_AWS_FREETIER_GET_FREE_TIER_USAGE` — Results from AWS Free Tier 'get-free-tier-usage'

### Glacier

- `LW_CFG_AWS_GLACIER_GET_VAULT_ACCESS_POLICY` — Amazon Glacier `get-vault-access-policy`
- `LW_CFG_AWS_GLACIER_GET_VAULT_LOCK` — Amazon Glacier `get-vault-lock`
- `LW_CFG_AWS_GLACIER_VAULTS` — Amazon Glacier `list-vaults`

### Glue

- `LW_CFG_AWS_GLUE_BATCH_GET_WORKFLOWS` — AWS Glue `batch-get-workflows`
- `LW_CFG_AWS_GLUE_WORKFLOWS` — AWS Glue `list-workflows`

### Greengrass

- `LW_CFG_AWS_GREENGRASS_BULK_DEPLOYMENTS` — Results from AWS Greengrass 'list-bulk-deployments'
- `LW_CFG_AWS_GREENGRASS_BULK_DEPLOYMENT_DETAILED_REPORTS` — Results from AWS Greengrass 'list-bulk-deployment-detailed-reports'
- `LW_CFG_AWS_GREENGRASS_CONNECTOR_DEFINITIONS` — Results from AWS Greengrass 'list-connector-definitions'
- `LW_CFG_AWS_GREENGRASS_CONNECTOR_DEFINITION_VERSIONS` — Results from AWS Greengrass 'list-connector-definition-versions'
- `LW_CFG_AWS_GREENGRASS_CORE_DEFINITIONS` — Results from AWS Greengrass 'list-core-definitions'
- `LW_CFG_AWS_GREENGRASS_CORE_DEFINITION_VERSIONS` — Results from AWS Greengrass 'list-core-definition-versions'
- `LW_CFG_AWS_GREENGRASS_DEPLOYMENTS` — Results from AWS Greengrass 'list-deployments'
- `LW_CFG_AWS_GREENGRASS_DEVICE_DEFINITIONS` — Results from AWS Greengrass 'list-device-definitions'
- `LW_CFG_AWS_GREENGRASS_DEVICE_DEFINITION_VERSIONS` — Results from AWS Greengrass 'list-device-definition-versions'
- `LW_CFG_AWS_GREENGRASS_FUNCTION_DEFINITIONS` — Results from AWS Greengrass 'list-function-definitions'
- `LW_CFG_AWS_GREENGRASS_FUNCTION_DEFINITION_VERSIONS` — Results from AWS Greengrass 'list-function-definition-versions'
- `LW_CFG_AWS_GREENGRASS_GET_ASSOCIATED_ROLE` — Results from AWS Greengrass 'get-associated-role'
- `LW_CFG_AWS_GREENGRASS_GET_BULK_DEPLOYMENT_STATUS` — Results from AWS Greengrass 'get-bulk-deployment-status'
- `LW_CFG_AWS_GREENGRASS_GET_CONNECTOR_DEFINITION_VERSION` — Results from AWS Greengrass 'get-connector-definition-version'
- `LW_CFG_AWS_GREENGRASS_GET_CORE_DEFINITION_VERSION` — Results from AWS Greengrass 'get-core-definition-version'
- `LW_CFG_AWS_GREENGRASS_GET_DEPLOYMENT_STATUS` — Results from AWS Greengrass 'get-deployment-status'
- `LW_CFG_AWS_GREENGRASS_GET_DEVICE_DEFINITION_VERSION` — Results from AWS Greengrass 'get-device-definition-version'
- `LW_CFG_AWS_GREENGRASS_GET_FUNCTION_DEFINITION_VERSION` — Results from AWS Greengrass 'get-function-definition-version'
- `LW_CFG_AWS_GREENGRASS_GET_GROUP_CERTIFICATE_CONFIGURATION` — Results from AWS Greengrass 'get-group-certificate-configuration'
- `LW_CFG_AWS_GREENGRASS_GET_GROUP_VERSION` — Results from AWS Greengrass 'get-group-version'
- `LW_CFG_AWS_GREENGRASS_GET_LOGGER_DEFINITION_VERSION` — Results from AWS Greengrass 'get-logger-definition-version'
- `LW_CFG_AWS_GREENGRASS_GET_RESOURCE_DEFINITION_VERSION` — Results from AWS Greengrass 'get-resource-definition-version'
- `LW_CFG_AWS_GREENGRASS_GET_SUBSCRIPTION_DEFINITION_VERSION` — Results from AWS Greengrass 'get-subscription-definition-version'
- `LW_CFG_AWS_GREENGRASS_GROUPS` — Results from AWS Greengrass 'list-groups'
- `LW_CFG_AWS_GREENGRASS_GROUP_VERSIONS` — Results from AWS Greengrass 'list-group-versions'
- `LW_CFG_AWS_GREENGRASS_LOGGER_DEFINITIONS` — Results from AWS Greengrass 'list-logger-definitions'
- `LW_CFG_AWS_GREENGRASS_LOGGER_DEFINITION_VERSIONS` — Results from AWS Greengrass 'list-logger-definition-versions'
- `LW_CFG_AWS_GREENGRASS_RESOURCE_DEFINITIONS` — Results from AWS Greengrass 'list-resource-definitions'
- `LW_CFG_AWS_GREENGRASS_RESOURCE_DEFINITION_VERSIONS` — Results from AWS Greengrass 'list-resource-definition-versions'
- `LW_CFG_AWS_GREENGRASS_SUBSCRIPTION_DEFINITIONS` — Results from AWS Greengrass 'list-subscription-definitions'
- `LW_CFG_AWS_GREENGRASS_SUBSCRIPTION_DEFINITION_VERSIONS` — Results from AWS Greengrass 'list-subscription-definition-versions'

### GuardDuty

- `LW_CFG_AWS_GUARDDUTY_DESCRIBE_PUBLISHING_DESTINATION` — Amazon GuardDuty `describe-publishing-destination`
- `LW_CFG_AWS_GUARDDUTY_DETECTORS` — Amazon GuardDuty `list-detectors`
- `LW_CFG_AWS_GUARDDUTY_FILTERS` — Amazon GuardDuty `list-filters`
- `LW_CFG_AWS_GUARDDUTY_FINDINGS` — Amazon GuardDuty `list-findings`
- `LW_CFG_AWS_GUARDDUTY_GET_ADMINISTRATOR_ACCOUNT` — Amazon GuardDuty `get-administrator-account`
- `LW_CFG_AWS_GUARDDUTY_GET_DETECTOR` — Amazon GuardDuty `get-detector`
- `LW_CFG_AWS_GUARDDUTY_GET_FILTER` — Amazon GuardDuty `get-filter`
- `LW_CFG_AWS_GUARDDUTY_GET_FINDINGS` — Amazon GuardDuty `get-findings`
- `LW_CFG_AWS_GUARDDUTY_GET_IP_SET` — Amazon GuardDuty `get-ip-set`
- `LW_CFG_AWS_GUARDDUTY_GET_MALWARE_SCAN_SETTINGS` — Amazon GuardDuty `get-malware-scan-settings`
- `LW_CFG_AWS_GUARDDUTY_GET_MASTER_ACCOUNT` — Amazon GuardDuty `get-master-account`
- `LW_CFG_AWS_GUARDDUTY_GET_MEMBERS` — Amazon GuardDuty `get-members`
- `LW_CFG_AWS_GUARDDUTY_GET_MEMBER_DETECTORS` — Amazon GuardDuty `get-member-detectors`
- `LW_CFG_AWS_GUARDDUTY_GET_THREAT_INTEL_SET` — Amazon GuardDuty `get-threat-intel-set`
- `LW_CFG_AWS_GUARDDUTY_INVITATIONS` — Amazon GuardDuty `list-invitations`
- `LW_CFG_AWS_GUARDDUTY_IP_SETS` — Amazon GuardDuty `list-ip-sets`
- `LW_CFG_AWS_GUARDDUTY_MEMBERS` — Amazon GuardDuty `list-members`
- `LW_CFG_AWS_GUARDDUTY_PUBLISHING_DESTINATIONS` — Amazon GuardDuty `list-publishing-destinations`
- `LW_CFG_AWS_GUARDDUTY_THREAT_INTEL_SETS` — Amazon GuardDuty `list-threat-intel-sets`

### IAM

- `LW_CFG_AWS_IAM_ACCOUNT_PASSWORD_POLICY` — iam `get-account-password-policy`
- `LW_CFG_AWS_IAM_ACCOUNT_SUMMARY` — iam `get-account-summary`
- `LW_CFG_AWS_IAM_GET_GROUP_POLICY` — iam `get-group-policy`
- `LW_CFG_AWS_IAM_GET_ROLE` — iam `get-role`
- `LW_CFG_AWS_IAM_GET_USER` — iam `get-user`
- `LW_CFG_AWS_IAM_GROUPS` — iam `list-groups`
- `LW_CFG_AWS_IAM_GROUPS_GET_GROUP` — iam `get-group`
- `LW_CFG_AWS_IAM_GROUPS_LIST_ATTACHED_POLICIES` — iam `list-attached-group-policies`
- `LW_CFG_AWS_IAM_GROUP_POLICIES` — iam `list-group-policies`
- `LW_CFG_AWS_IAM_INSTANCE_PROFILES` — iam `list-instance-profiles`
- `LW_CFG_AWS_IAM_MFA_DEVICES` — iam `list-virtual-mfa-devices`
- `LW_CFG_AWS_IAM_OPEN_ID_CONNECT_PROVIDERS` — iam `list-open-id-connect-providers`
- `LW_CFG_AWS_IAM_POLICIES` — iam `list-policies`
- `LW_CFG_AWS_IAM_POLICIES_GET_VERSION` — iam `get-policy-version`
- `LW_CFG_AWS_IAM_ROLES` — iam `list-roles`
- `LW_CFG_AWS_IAM_ROLES_GET_POLICY` — iam `get-role-policy`
- `LW_CFG_AWS_IAM_ROLES_LIST_ATTACHED_POLICIES` — iam `list-attached-role-policies`
- `LW_CFG_AWS_IAM_ROLES_LIST_POLICIES` — iam `list-role-policies`
- `LW_CFG_AWS_IAM_SAML_PROVIDERS` — iam `list-saml-providers`
- `LW_CFG_AWS_IAM_SERVER_CERTIFICATES` — iam `list-server-certificates`
- `LW_CFG_AWS_IAM_USERS` — iam `list-users`
- `LW_CFG_AWS_IAM_USERS_GET_CREDENTIAL_REPORT` — iam `get-credential-report`
- `LW_CFG_AWS_IAM_USERS_GET_POLICY` — iam `get-user-policy`
- `LW_CFG_AWS_IAM_USERS_LIST_ACCESS_KEYS` — iam `list-access-keys`
- `LW_CFG_AWS_IAM_USERS_LIST_ATTACHED_POLICIES` — iam `list-attached-user-policies`
- `LW_CFG_AWS_IAM_USERS_LIST_MFA_DEVICES` — iam `list-mfa-devices`
- `LW_CFG_AWS_IAM_USERS_LIST_POLICIES` — iam `list-user-policies`
- `LW_CFG_AWS_IAM_USERS_LIST_SSH_PUBLIC_KEYS` — iam `list-ssh-public-keys`
- `LW_CFG_AWS_IAM_GET_ACCESS_KEY_LAST_USED` — Results from AWS Identity and Access Management 'get-access-key-last-used'

### Inspector2

- `LW_CFG_AWS_INSPECTOR2_CIS_SCANS` — Results from Inspector2 'list-cis-scans'
- `LW_CFG_AWS_INSPECTOR2_CIS_SCAN_CONFIGURATIONS` — Results from Inspector2 'list-cis-scan-configurations'
- `LW_CFG_AWS_INSPECTOR2_CIS_SCAN_RESULTS_AGGREGATED_BY_CHECKS` — Results from Inspector2 'list-cis-scan-results-aggregated-by-checks'
- `LW_CFG_AWS_INSPECTOR2_CIS_SCAN_RESULTS_AGGREGATED_BY_TARGET_RESOURCE` — Results from Inspector2 'list-cis-scan-results-aggregated-by-target-resource'
- `LW_CFG_AWS_INSPECTOR2_COVERAGE` — Results from Inspector2 'list-coverage'
- `LW_CFG_AWS_INSPECTOR2_DELEGATED_ADMIN_ACCOUNTS` — Results from Inspector2 'list-delegated-admin-accounts'
- `LW_CFG_AWS_INSPECTOR2_FILTERS` — Results from Inspector2 'list-filters'
- `LW_CFG_AWS_INSPECTOR2_GET_CIS_SCAN_REPORT` — Results from Inspector2 'get-cis-scan-report'
- `LW_CFG_AWS_INSPECTOR2_GET_CIS_SCAN_RESULT_DETAILS` — Results from Inspector2 'get-cis-scan-result-details'
- `LW_CFG_AWS_INSPECTOR2_GET_FINDINGS_REPORT_STATUS` — Results from Inspector2 'get-findings-report-status'
- `LW_CFG_AWS_INSPECTOR2_MEMBERS` — Results from Inspector2 'list-members'
- `LW_CFG_AWS_INSPECTOR2_COVERAGE_STATISTICS` — Results from Inspector2 'list-coverage-statistics'

### IoT

- `LW_CFG_AWS_IOT_ACTIVE_VIOLATIONS` — Results from AWS IoT 'list-active-violations'
- `LW_CFG_AWS_IOT_ATTACHED_POLICIES` — Results from AWS IoT 'list-attached-policies'
- `LW_CFG_AWS_IOT_AUDIT_FINDINGS` — Results from AWS IoT 'list-audit-findings'
- `LW_CFG_AWS_IOT_AUTHORIZERS` — Results from AWS IoT 'list-authorizers'
- `LW_CFG_AWS_IOT_BILLING_GROUPS` — Results from AWS IoT 'list-billing-groups'
- `LW_CFG_AWS_IOT_CA_CERTIFICATES` — Results from AWS IoT 'list-ca-certificates'
- `LW_CFG_AWS_IOT_CERTIFICATES` — Results from AWS IoT 'list-certificates'
- `LW_CFG_AWS_IOT_CERTIFICATE_PROVIDERS` — Results from AWS IoT 'list-certificate-providers'
- `LW_CFG_AWS_IOT_COMMANDS` — Results from AWS IoT 'list-commands'
- `LW_CFG_AWS_IOT_CUSTOM_METRICS` — Results from AWS IoT 'list-custom-metrics'
- `LW_CFG_AWS_IOT_DESCRIBE_ACCOUNT_AUDIT_CONFIGURATION` — Results from AWS IoT 'describe-account-audit-configuration'
- `LW_CFG_AWS_IOT_DESCRIBE_AUTHORIZER` — Results from AWS IoT 'describe-authorizer'
- `LW_CFG_AWS_IOT_DESCRIBE_BILLING_GROUP` — Results from AWS IoT 'describe-billing-group'
- `LW_CFG_AWS_IOT_DESCRIBE_CA_CERTIFICATE` — Results from AWS IoT 'describe-ca-certificate'
- `LW_CFG_AWS_IOT_DESCRIBE_CERTIFICATE` — Results from AWS IoT 'describe-certificate'
- `LW_CFG_AWS_IOT_DESCRIBE_CERTIFICATE_PROVIDER` — Results from AWS IoT 'describe-certificate-provider'
- `LW_CFG_AWS_IOT_DESCRIBE_CUSTOM_METRIC` — Results from AWS IoT 'describe-custom-metric'
- `LW_CFG_AWS_IOT_DESCRIBE_DEFAULT_AUTHORIZER` — Results from AWS IoT 'describe-default-authorizer'
- `LW_CFG_AWS_IOT_DESCRIBE_DIMENSION` — Results from AWS IoT 'describe-dimension'
- `LW_CFG_AWS_IOT_DESCRIBE_DOMAIN_CONFIGURATION` — Results from AWS IoT 'describe-domain-configuration'
- `LW_CFG_AWS_IOT_DESCRIBE_ENDPOINT` — Results from AWS IoT 'describe-endpoint'
- `LW_CFG_AWS_IOT_DESCRIBE_EVENT_CONFIGURATIONS` — Results from AWS IoT 'describe-event-configurations'
- `LW_CFG_AWS_IOT_DESCRIBE_FLEET_METRIC` — Results from AWS IoT 'describe-fleet-metric'
- `LW_CFG_AWS_IOT_DESCRIBE_INDEX` — Results from AWS IoT 'describe-index'
- `LW_CFG_AWS_IOT_DESCRIBE_JOB` — Results from AWS IoT 'describe-job'
- `LW_CFG_AWS_IOT_DESCRIBE_JOB_EXECUTION` — Results from AWS IoT 'describe-job-execution'
- `LW_CFG_AWS_IOT_DESCRIBE_JOB_TEMPLATE` — Results from AWS IoT 'describe-job-template'
- `LW_CFG_AWS_IOT_DESCRIBE_MANAGED_JOB_TEMPLATE` — Results from AWS IoT 'describe-managed-job-template'
- `LW_CFG_AWS_IOT_DESCRIBE_MITIGATION_ACTION` — Results from AWS IoT 'describe-mitigation-action'
- `LW_CFG_AWS_IOT_DESCRIBE_PROVISIONING_TEMPLATE` — Results from AWS IoT 'describe-provisioning-template'
- `LW_CFG_AWS_IOT_DESCRIBE_PROVISIONING_TEMPLATE_VERSION` — Results from AWS IoT 'describe-provisioning-template-version'
- `LW_CFG_AWS_IOT_DESCRIBE_ROLE_ALIAS` — Results from AWS IoT 'describe-role-alias'
- `LW_CFG_AWS_IOT_DESCRIBE_SCHEDULED_AUDIT` — Results from AWS IoT 'describe-scheduled-audit'
- `LW_CFG_AWS_IOT_DESCRIBE_SECURITY_PROFILE` — Results from AWS IoT 'describe-security-profile'
- `LW_CFG_AWS_IOT_DESCRIBE_STREAM` — Results from AWS IoT 'describe-stream'
- `LW_CFG_AWS_IOT_DESCRIBE_THING` — Results from AWS IoT 'describe-thing'
- `LW_CFG_AWS_IOT_DESCRIBE_THING_GROUP` — Results from AWS IoT 'describe-thing-group'
- `LW_CFG_AWS_IOT_DESCRIBE_THING_REGISTRATION_TASK` — Results from AWS IoT 'describe-thing-registration-task'
- `LW_CFG_AWS_IOT_DESCRIBE_THING_TYPE` — Results from AWS IoT 'describe-thing-type'
- `LW_CFG_AWS_IOT_DIMENSIONS` — Results from AWS IoT 'list-dimensions'
- `LW_CFG_AWS_IOT_DOMAIN_CONFIGURATIONS` — Results from AWS IoT 'list-domain-configurations'
- `LW_CFG_AWS_IOT_FLEET_METRICS` — Results from AWS IoT 'list-fleet-metrics'
- `LW_CFG_AWS_IOT_GET_POLICY` — Results from AWS IoT 'get-policy'
- `LW_CFG_AWS_IOT_GET_POLICY_VERSION` — Results from AWS IoT 'get-policy-version'
- `LW_CFG_AWS_IOT_INDICES` — Results from AWS IoT 'list-indices'
- `LW_CFG_AWS_IOT_JOBS` — Results from AWS IoT 'list-jobs'
- `LW_CFG_AWS_IOT_JOB_EXECUTIONS_FOR_JOB` — Results from AWS IoT 'list-job-executions-for-job'
- `LW_CFG_AWS_IOT_JOB_EXECUTIONS_FOR_THING` — Results from AWS IoT 'list-job-executions-for-thing'
- `LW_CFG_AWS_IOT_JOB_TEMPLATES` — Results from AWS IoT 'list-job-templates'
- `LW_CFG_AWS_IOT_MANAGED_JOB_TEMPLATES` — Results from AWS IoT 'list-managed-job-templates'
- `LW_CFG_AWS_IOT_MITIGATION_ACTIONS` — Results from AWS IoT 'list-mitigation-actions'
- `LW_CFG_AWS_IOT_OTA_UPDATES` — Results from AWS IoT 'list-ota-updates'
- `LW_CFG_AWS_IOT_OUTGOING_CERTIFICATES` — Results from AWS IoT 'list-outgoing-certificates'
- `LW_CFG_AWS_IOT_PACKAGES` — Results from AWS IoT 'list-packages'
- `LW_CFG_AWS_IOT_PACKAGE_VERSIONS` — Results from AWS IoT 'list-package-versions'
- `LW_CFG_AWS_IOT_POLICIES` — Results from AWS IoT 'list-policies'
- `LW_CFG_AWS_IOT_POLICY_VERSIONS` — Results from AWS IoT 'list-policy-versions'
- `LW_CFG_AWS_IOT_PRINCIPAL_POLICIES` — Results from AWS IoT 'list-principal-policies'
- `LW_CFG_AWS_IOT_PROVISIONING_TEMPLATES` — Results from AWS IoT 'list-provisioning-templates'
- `LW_CFG_AWS_IOT_PROVISIONING_TEMPLATE_VERSIONS` — Results from AWS IoT 'list-provisioning-template-versions'
- `LW_CFG_AWS_IOT_ROLE_ALIASES` — Results from AWS IoT 'list-role-aliases'
- `LW_CFG_AWS_IOT_SBOM_VALIDATION_RESULTS` — Results from AWS IoT 'list-sbom-validation-results'
- `LW_CFG_AWS_IOT_SCHEDULED_AUDITS` — Results from AWS IoT 'list-scheduled-audits'
- `LW_CFG_AWS_IOT_SECURITY_PROFILES` — Results from AWS IoT 'list-security-profiles'
- `LW_CFG_AWS_IOT_SECURITY_PROFILES_FOR_TARGET` — Results from AWS IoT 'list-security-profiles-for-target'
- `LW_CFG_AWS_IOT_STREAMS` — Results from AWS IoT 'list-streams'
- `LW_CFG_AWS_IOT_TARGETS_FOR_POLICY` — Results from AWS IoT 'list-targets-for-policy'
- `LW_CFG_AWS_IOT_TARGETS_FOR_SECURITY_PROFILE` — Results from AWS IoT 'list-targets-for-security-profile'
- `LW_CFG_AWS_IOT_THINGS` — Results from AWS IoT 'list-things'
- `LW_CFG_AWS_IOT_THINGS_IN_BILLING_GROUP` — Results from AWS IoT 'list-things-in-billing-group'
- `LW_CFG_AWS_IOT_THING_GROUPS` — Results from AWS IoT 'list-thing-groups'
- `LW_CFG_AWS_IOT_THING_GROUPS_FOR_THING` — Results from AWS IoT 'list-thing-groups-for-thing'
- `LW_CFG_AWS_IOT_THING_PRINCIPALS_V2` — Results from AWS IoT 'list-thing-principals-v2'
- `LW_CFG_AWS_IOT_THING_REGISTRATION_TASKS` — Results from AWS IoT 'list-thing-registration-tasks'
- `LW_CFG_AWS_IOT_THING_REGISTRATION_TASK_REPORTS` — Results from AWS IoT 'list-thing-registration-task-reports'
- `LW_CFG_AWS_IOT_THING_TYPES` — Results from AWS IoT 'list-thing-types'
- `LW_CFG_AWS_IOT_TOPIC_RULES` — Results from AWS IoT 'list-topic-rules'
- `LW_CFG_AWS_IOT_TOPIC_RULE_DESTINATIONS` — Results from AWS IoT 'list-topic-rule-destinations'
