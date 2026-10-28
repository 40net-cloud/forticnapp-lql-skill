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

### RDS

- `LW_CFG_AWS_RDS_CLUSTER_SNAPSHOTS` — rds `describe-db-cluster-snapshots`
- `LW_CFG_AWS_RDS_CLUSTERS` — rds `describe-db-clusters`
- `LW_CFG_AWS_RDS_DB_CLUSTER_PARAMETERS` — Amazon Relational Database Service `describe-db-cluster-parameters`
- `LW_CFG_AWS_RDS_DB_CLUSTER_PARAMETER_GROUPS` — Amazon Relational Database Service `describe-db-cluster-parameter-groups`
- `LW_CFG_AWS_RDS_DB_INSTANCES` — rds `describe-db-instances`
- `LW_CFG_AWS_RDS_DB_SNAPSHOTS` — Amazon Relational Database Service `describe-db-snapshots`
- `LW_CFG_AWS_RDS_DESCRIBE_DB_SNAPSHOT_ATTRIBUTES` — Amazon Relational Database Service `describe-db-snapshot-attributes`
- `LW_CFG_AWS_RDS_EVENT_SUBSCRIPTIONS` — rds `describe-event-subscriptions`
- `LW_CFG_AWS_RDS_DB_PARAMETERS` — Amazon Relational Database Service `describe-db-parameters`
- `LW_CFG_AWS_RDS_DB_PARAMETER_GROUPS` — Amazon Relational Database Service `describe-db-parameter-groups`
- `LW_CFG_AWS_RDS_RESERVED_DB_INSTANCES_OFFERINGS` — rds `describe-reserved-db-instances-offerings`
- `LW_CFG_AWS_RDS_DB_PROXIES` — Results from Amazon Relational Database Service 'describe-db-proxies'
- `LW_CFG_AWS_RDS_DB_PROXY_ENDPOINTS` — Results from Amazon Relational Database Service 'describe-db-proxy-endpoints'
- `LW_CFG_AWS_RDS_DB_PROXY_TARGETS` — Results from Amazon Relational Database Service 'describe-db-proxy-targets'
- `LW_CFG_AWS_RDS_DB_PROXY_TARGET_GROUPS` — Results from Amazon Relational Database Service 'describe-db-proxy-target-groups'

### Redshift

- `LW_CFG_AWS_REDSHIFT_CLUSTERS` — redshift `describe-clusters`
- `LW_CFG_AWS_REDSHIFT_CLUSTER_PARAMETERS` — Results from Amazon Redshift 'describe-cluster-parameters'
- `LW_CFG_AWS_REDSHIFT_CLUSTER_PARAMETER_GROUPS` — Results from Amazon Redshift 'describe-cluster-parameter-groups'
- `LW_CFG_AWS_REDSHIFT_DESCRIBE_LOGGING_STATUS` — Results from Amazon Redshift 'describe-logging-status'

### Resilience Hub

- `LW_CFG_AWS_RESILIENCEHUB_ALARM_RECOMMENDATIONS` — Results from AWS Resilience Hub 'list-alarm-recommendations'
- `LW_CFG_AWS_RESILIENCEHUB_APPS` — Results from AWS Resilience Hub 'list-apps'
- `LW_CFG_AWS_RESILIENCEHUB_APP_ASSESSMENTS` — Results from AWS Resilience Hub 'list-app-assessments'
- `LW_CFG_AWS_RESILIENCEHUB_APP_ASSESSMENT_COMPLIANCE_DRIFTS` — Results from AWS Resilience Hub 'list-app-assessment-compliance-drifts'
- `LW_CFG_AWS_RESILIENCEHUB_APP_ASSESSMENT_RESOURCE_DRIFTS` — Results from AWS Resilience Hub 'list-app-assessment-resource-drifts'
- `LW_CFG_AWS_RESILIENCEHUB_APP_COMPONENT_COMPLIANCES` — Results from AWS Resilience Hub 'list-app-component-compliances'
- `LW_CFG_AWS_RESILIENCEHUB_APP_COMPONENT_RECOMMENDATIONS` — Results from AWS Resilience Hub 'list-app-component-recommendations'
- `LW_CFG_AWS_RESILIENCEHUB_APP_INPUT_SOURCES` — Results from AWS Resilience Hub 'list-app-input-sources'
- `LW_CFG_AWS_RESILIENCEHUB_APP_VERSIONS` — Results from AWS Resilience Hub 'list-app-versions'
- `LW_CFG_AWS_RESILIENCEHUB_APP_VERSION_APP_COMPONENTS` — Results from AWS Resilience Hub 'list-app-version-app-components'
- `LW_CFG_AWS_RESILIENCEHUB_APP_VERSION_RESOURCES` — Results from AWS Resilience Hub 'list-app-version-resources'
- `LW_CFG_AWS_RESILIENCEHUB_APP_VERSION_RESOURCE_MAPPINGS` — Results from AWS Resilience Hub 'list-app-version-resource-mappings'
- `LW_CFG_AWS_RESILIENCEHUB_DESCRIBE_APP` — Results from AWS Resilience Hub 'describe-app'
- `LW_CFG_AWS_RESILIENCEHUB_DESCRIBE_APP_ASSESSMENT` — Results from AWS Resilience Hub 'describe-app-assessment'
- `LW_CFG_AWS_RESILIENCEHUB_DESCRIBE_APP_VERSION` — Results from AWS Resilience Hub 'describe-app-version'
- `LW_CFG_AWS_RESILIENCEHUB_DESCRIBE_APP_VERSION_RESOURCES_RESOLUTION_STATUS` — Results from AWS Resilience Hub 'describe-app-version-resources-resolution-status'
- `LW_CFG_AWS_RESILIENCEHUB_DESCRIBE_APP_VERSION_TEMPLATE` — Results from AWS Resilience Hub 'describe-app-version-template'
- `LW_CFG_AWS_RESILIENCEHUB_DESCRIBE_RESOURCE_GROUPING_RECOMMENDATION_TASK` — Results from AWS Resilience Hub 'describe-resource-grouping-recommendation-task'
- `LW_CFG_AWS_RESILIENCEHUB_DRAFT_APP_VERSION_RESOURCES_IMPORT_STATUS` — Results from AWS Resilience Hub 'describe-draft-app-version-resources-import-status'
- `LW_CFG_AWS_RESILIENCEHUB_RECOMMENDATION_TEMPLATES` — Results from AWS Resilience Hub 'list-recommendation-templates'
- `LW_CFG_AWS_RESILIENCEHUB_RESILIENCY_POLICIES` — Results from AWS Resilience Hub 'list-resiliency-policies'
- `LW_CFG_AWS_RESILIENCEHUB_RESOURCE_GROUPING_RECOMMENDATIONS` — Results from AWS Resilience Hub 'list-resource-grouping-recommendations'
- `LW_CFG_AWS_RESILIENCEHUB_SOP_RECOMMENDATIONS` — Results from AWS Resilience Hub 'list-sop-recommendations'
- `LW_CFG_AWS_RESILIENCEHUB_SUGGESTED_RESILIENCY_POLICIES` — Results from AWS Resilience Hub 'list-suggested-resiliency-policies'
- `LW_CFG_AWS_RESILIENCEHUB_TEST_RECOMMENDATIONS` — Results from AWS Resilience Hub 'list-test-recommendations'
- `LW_CFG_AWS_RESILIENCEHUB_UNSUPPORTED_APP_VERSION_RESOURCES` — Results from AWS Resilience Hub 'list-unsupported-app-version-resources'

### Resource Groups

- `LW_CFG_AWS_RESOURCE_GROUPS_GROUPS` — resource-groups `list-groups`
- `LW_CFG_AWS_RESOURCE_GROUPS_GROUP_RESOURCES` — resource-groups `list-group-resources`

### Route 53

- `LW_CFG_AWS_ROUTE53_CIDR_BLOCKS` — route53 `list-cidr-blocks`
- `LW_CFG_AWS_ROUTE53_CIDR_COLLECTIONS` — route53 `list-cidr-collections`
- `LW_CFG_AWS_ROUTE53_CIDR_LOCATIONS` — route53 `list-cidr-locations`
- `LW_CFG_AWS_ROUTE53_GEO_LOCATIONS` — route53 `list-geo-locations`
- `LW_CFG_AWS_ROUTE53_GET_CHECKER_IP_RANGES` — route53 `get-checker-ip-ranges`
- `LW_CFG_AWS_ROUTE53_GET_DNSSEC` — route53 `get-dnssec`
- `LW_CFG_AWS_ROUTE53_GET_HEALTH_CHECK_LAST_FAILURE_REASON` — route53 `get-health-check-last-failure-reason`
- `LW_CFG_AWS_ROUTE53_GET_HEALTH_CHECK_STATUS` — route53 `get-health-check-status`
- `LW_CFG_AWS_ROUTE53_GET_HOSTED_ZONE` — route53 `get-hosted-zone`
- `LW_CFG_AWS_ROUTE53_GET_HOSTED_ZONE_LIMIT` — route53 `get-hosted-zone-limit`
- `LW_CFG_AWS_ROUTE53_GET_QUERY_LOGGING_CONFIG` — route53 `get-query-logging-config`
- `LW_CFG_AWS_ROUTE53_GET_REUSABLE_DELEGATION_SET` — route53 `get-reusable-delegation-set`
- `LW_CFG_AWS_ROUTE53_GET_TRAFFIC_POLICY` — route53 `get-traffic-policy`
- `LW_CFG_AWS_ROUTE53_GET_TRAFFIC_POLICY_INSTANCE` — route53 `get-traffic-policy-instance`
- `LW_CFG_AWS_ROUTE53_HEALTH_CHECKS` — route53 `list-health-checks`
- `LW_CFG_AWS_ROUTE53_HOSTED_ZONES` — route53 `list-hosted-zones`
- `LW_CFG_AWS_ROUTE53_QUERY_LOGGING_CONFIGS` — route53 `list-query-logging-configs`
- `LW_CFG_AWS_ROUTE53_RESOURCE_RECORD_SETS` — route53 `list-resource-record-sets`
- `LW_CFG_AWS_ROUTE53_REUSABLE_DELEGATION_SETS` — route53 `list-reusable-delegation-sets`
- `LW_CFG_AWS_ROUTE53_TRAFFIC_POLICIES` — route53 `list-traffic-policies`
- `LW_CFG_AWS_ROUTE53_TRAFFIC_POLICY_INSTANCES` — route53 `list-traffic-policy-instances`
- `LW_CFG_AWS_ROUTE53_TRAFFIC_POLICY_VERSIONS` — route53 `list-traffic-policy-versions`

### Route 53 Domains

- `LW_CFG_AWS_ROUTE53DOMAINS_DOMAINS` — route53domains `list-domains`
- `LW_CFG_AWS_ROUTE53DOMAINS_GET_DOMAIN_DETAIL` — route53domains `get-domain-detail`
- `LW_CFG_AWS_ROUTE53DOMAINS_GET_OPERATION_DETAIL` — route53domains `get-operation-detail`
- `LW_CFG_AWS_ROUTE53DOMAINS_OPERATIONS` — route53domains `list-operations`

### Route 53 Resolver

- `LW_CFG_AWS_ROUTE53RESOLVER_FIREWALL_CONFIGS` — Results from Amazon Route 53 Resolver 'list-firewall-configs'
- `LW_CFG_AWS_ROUTE53RESOLVER_FIREWALL_DOMAINS` — Results from Amazon Route 53 Resolver 'list-firewall-domains'
- `LW_CFG_AWS_ROUTE53RESOLVER_FIREWALL_DOMAIN_LISTS` — Results from Amazon Route 53 Resolver 'list-firewall-domain-lists'
- `LW_CFG_AWS_ROUTE53RESOLVER_FIREWALL_RULES` — Results from Amazon Route 53 Resolver 'list-firewall-rules'
- `LW_CFG_AWS_ROUTE53RESOLVER_FIREWALL_RULE_GROUPS` — Results from Amazon Route 53 Resolver 'list-firewall-rule-groups'
- `LW_CFG_AWS_ROUTE53RESOLVER_FIREWALL_RULE_GROUP_ASSOCIATIONS` — Results from Amazon Route 53 Resolver 'list-firewall-rule-group-associations'
- `LW_CFG_AWS_ROUTE53RESOLVER_GET_FIREWALL_DOMAIN_LIST` — Results from Amazon Route 53 Resolver 'get-firewall-domain-list'
- `LW_CFG_AWS_ROUTE53RESOLVER_GET_FIREWALL_RULE_GROUP` — Results from Amazon Route 53 Resolver 'get-firewall-rule-group'
- `LW_CFG_AWS_ROUTE53RESOLVER_GET_FIREWALL_RULE_GROUP_POLICY` — Results from Amazon Route 53 Resolver 'get-firewall-rule-group-policy'
- `LW_CFG_AWS_ROUTE53RESOLVER_GET_RESOLVER_QUERY_LOG_CONFIG_POLICY` — Results from Amazon Route 53 Resolver 'get-resolver-query-log-config-policy'
- `LW_CFG_AWS_ROUTE53RESOLVER_GET_RESOLVER_RULE_POLICY` — Results from Amazon Route 53 Resolver 'get-resolver-rule-policy'
- `LW_CFG_AWS_ROUTE53RESOLVER_OUTPOST_RESOLVERS` — Results from Amazon Route 53 Resolver 'list-outpost-resolvers'
- `LW_CFG_AWS_ROUTE53RESOLVER_RESOLVER_CONFIGS` — Results from Amazon Route 53 Resolver 'list-resolver-configs'
- `LW_CFG_AWS_ROUTE53RESOLVER_RESOLVER_DNSSEC_CONFIGS` — Results from Amazon Route 53 Resolver 'list-resolver-dnssec-configs'
- `LW_CFG_AWS_ROUTE53RESOLVER_RESOLVER_ENDPOINTS` — Results from Amazon Route 53 Resolver 'list-resolver-endpoints'
- `LW_CFG_AWS_ROUTE53RESOLVER_RESOLVER_ENDPOINT_IP_ADDRESSES` — Results from Amazon Route 53 Resolver 'list-resolver-endpoint-ip-addresses'
- `LW_CFG_AWS_ROUTE53RESOLVER_RESOLVER_QUERY_LOG_CONFIGS` — Results from Amazon Route 53 Resolver 'list-resolver-query-log-configs'
- `LW_CFG_AWS_ROUTE53RESOLVER_RESOLVER_QUERY_LOG_CONFIG_ASSOCIATIONS` — Results from Amazon Route 53 Resolver 'list-resolver-query-log-config-associations'
- `LW_CFG_AWS_ROUTE53RESOLVER_RESOLVER_RULES` — Results from Amazon Route 53 Resolver 'list-resolver-rules'
- `LW_CFG_AWS_ROUTE53RESOLVER_RESOLVER_RULE_ASSOCIATIONS` — Results from Amazon Route 53 Resolver 'list-resolver-rule-associations'

### S3

- `LW_CFG_AWS_S3` — s3api `list-buckets`
- `LW_CFG_AWS_S3_GET_BUCKET_ACL` — s3api `get-bucket-acl`
- `LW_CFG_AWS_S3_GET_BUCKET_ENCRYPTION` — s3api `get-bucket-encryption`
- `LW_CFG_AWS_S3_GET_BUCKET_LOGGING` — s3api `get-bucket-logging`
- `LW_CFG_AWS_S3_GET_BUCKET_OWNERSHIP_CONTROLS` — s3api `get-bucket-ownership-controls`
- `LW_CFG_AWS_S3_GET_BUCKET_POLICY` — s3api `get-bucket-policy`
- `LW_CFG_AWS_S3_GET_BUCKET_POLICY_STATUS` — s3api `get-bucket-policy-status`
- `LW_CFG_AWS_S3_GET_BUCKET_VERSIONING` — s3api `get-bucket-versioning`
- `LW_CFG_AWS_S3_GET_PUBLIC_ACCESS_BLOCK` — s3api `get-public-access-block`
- `LW_CFG_AWS_S3_GET_BUCKET_LIFECYCLE_CONFIGURATION` — Results from Amazon Simple Storage Service 'get-bucket-lifecycle-configuration'
- `LW_CFG_AWS_S3_GET_BUCKET_NOTIFICATION_CONFIGURATION` — Results from Amazon Simple Storage Service 'get-bucket-notification-configuration'
- `LW_CFG_AWS_S3_GET_BUCKET_REPLICATION` — Results from Amazon Simple Storage Service 'get-bucket-replication'
- `LW_CFG_AWS_S3_GET_BUCKET_WEBSITE` — Results from Amazon Simple Storage Service 'get-bucket-website'
- `LW_CFG_AWS_S3_GET_OBJECT_LOCK_CONFIGURATION` — Results from Amazon Simple Storage Service 'get-object-lock-configuration'

### S3 Control

- `LW_CFG_AWS_S3CONTROL_GET_PUBLIC_ACCESS_BLOCK` — s3control `get-public-access-block`

### SageMaker

- `LW_CFG_AWS_SAGEMAKER_ACTIONS` — sagemaker `list-actions`
- `LW_CFG_AWS_SAGEMAKER_ALGORITHMS` — sagemaker `list-algorithms`
- `LW_CFG_AWS_SAGEMAKER_ALIASES` — sagemaker `list-aliases`
- `LW_CFG_AWS_SAGEMAKER_APPS` — sagemaker `list-apps`
- `LW_CFG_AWS_SAGEMAKER_APP_IMAGE_CONFIGS` — sagemaker `list-app-image-configs`
- `LW_CFG_AWS_SAGEMAKER_ARTIFACTS` — sagemaker `list-artifacts`
- `LW_CFG_AWS_SAGEMAKER_AUTO_ML_JOBS` — sagemaker `list-auto-ml-jobs`
- `LW_CFG_AWS_SAGEMAKER_CANDIDATES_FOR_AUTO_ML_JOB` — sagemaker `list-candidates-for-auto-ml-job`
- `LW_CFG_AWS_SAGEMAKER_CODE_REPOSITORIES` — sagemaker `list-code-repositories`
- `LW_CFG_AWS_SAGEMAKER_COMPILATION_JOBS` — sagemaker `list-compilation-jobs`
- `LW_CFG_AWS_SAGEMAKER_CONTEXTS` — sagemaker `list-contexts`
- `LW_CFG_AWS_SAGEMAKER_DATA_QUALITY_JOB_DEFINITIONS` — sagemaker `list-data-quality-job-definitions`
- `LW_CFG_AWS_SAGEMAKER_DESCRIBE_ACTION` — sagemaker `describe-action`
- `LW_CFG_AWS_SAGEMAKER_DESCRIBE_ALGORITHM` — sagemaker `describe-algorithm`
- `LW_CFG_AWS_SAGEMAKER_DESCRIBE_APP` — sagemaker `describe-app`
- `LW_CFG_AWS_SAGEMAKER_DESCRIBE_APP_IMAGE_CONFIG` — sagemaker `describe-app-image-config`
- `LW_CFG_AWS_SAGEMAKER_DESCRIBE_ARTIFACT` — sagemaker `describe-artifact`
- `LW_CFG_AWS_SAGEMAKER_DESCRIBE_AUTO_ML_JOB` — sagemaker `describe-auto-ml-job`
- `LW_CFG_AWS_SAGEMAKER_DESCRIBE_CODE_REPOSITORY` — sagemaker `describe-code-repository`
- `LW_CFG_AWS_SAGEMAKER_DESCRIBE_COMPILATION_JOB` — sagemaker `describe-compilation-job`
- `LW_CFG_AWS_SAGEMAKER_DESCRIBE_CONTEXT` — sagemaker `describe-context`
- `LW_CFG_AWS_SAGEMAKER_DESCRIBE_DEVICE` — sagemaker `describe-device`
- `LW_CFG_AWS_SAGEMAKER_DESCRIBE_DEVICE_FLEET` — sagemaker `describe-device-fleet`
- `LW_CFG_AWS_SAGEMAKER_DESCRIBE_DOMAIN` — sagemaker `describe-domain`
- `LW_CFG_AWS_SAGEMAKER_DESCRIBE_EDGE_DEPLOYMENT_PLAN` — sagemaker `describe-edge-deployment-plan`
- `LW_CFG_AWS_SAGEMAKER_DESCRIBE_EDGE_PACKAGING_JOB` — sagemaker `describe-edge-packaging-job`
- `LW_CFG_AWS_SAGEMAKER_DESCRIBE_ENDPOINT` — sagemaker `describe-endpoint`
- `LW_CFG_AWS_SAGEMAKER_DESCRIBE_ENDPOINT_CONFIG` — sagemaker `describe-endpoint-config`
- `LW_CFG_AWS_SAGEMAKER_DESCRIBE_EXPERIMENT` — sagemaker `describe-experiment`
- `LW_CFG_AWS_SAGEMAKER_DESCRIBE_FEATURE_GROUP` — sagemaker `describe-feature-group`
- `LW_CFG_AWS_SAGEMAKER_DESCRIBE_FLOW_DEFINITION` — sagemaker `describe-flow-definition`
- `LW_CFG_AWS_SAGEMAKER_DESCRIBE_HUMAN_TASK_UI` — sagemaker `describe-human-task-ui`
- `LW_CFG_AWS_SAGEMAKER_DESCRIBE_HYPER_PARAMETER_TUNING_JOB` — sagemaker `describe-hyper-parameter-tuning-job`
- `LW_CFG_AWS_SAGEMAKER_DESCRIBE_IMAGE` — sagemaker `describe-image`
- `LW_CFG_AWS_SAGEMAKER_DESCRIBE_IMAGE_VERSION` — sagemaker `describe-image-version`
- `LW_CFG_AWS_SAGEMAKER_DESCRIBE_INFERENCE_EXPERIMENT` — sagemaker `describe-inference-experiment`
- `LW_CFG_AWS_SAGEMAKER_DESCRIBE_INFERENCE_RECOMMENDATIONS_JOB` — sagemaker `describe-inference-recommendations-job`
- `LW_CFG_AWS_SAGEMAKER_DESCRIBE_LABELING_JOB` — sagemaker `describe-labeling-job`
- `LW_CFG_AWS_SAGEMAKER_DESCRIBE_LINEAGE_GROUP` — sagemaker `describe-lineage-group`
- `LW_CFG_AWS_SAGEMAKER_DESCRIBE_MODEL` — sagemaker `describe-model`
- `LW_CFG_AWS_SAGEMAKER_DESCRIBE_MODEL_CARD` — sagemaker `describe-model-card`
- `LW_CFG_AWS_SAGEMAKER_DESCRIBE_MODEL_CARD_EXPORT_JOB` — sagemaker `describe-model-card-export-job`
- `LW_CFG_AWS_SAGEMAKER_DESCRIBE_MODEL_PACKAGE` — sagemaker `describe-model-package`
- `LW_CFG_AWS_SAGEMAKER_DESCRIBE_MODEL_PACKAGE_GROUP` — sagemaker `describe-model-package-group`
- `LW_CFG_AWS_SAGEMAKER_DESCRIBE_MONITORING_SCHEDULE` — sagemaker `describe-monitoring-schedule`
- `LW_CFG_AWS_SAGEMAKER_DESCRIBE_NOTEBOOK_INSTANCE` — sagemaker `describe-notebook-instance`
- `LW_CFG_AWS_SAGEMAKER_DESCRIBE_NOTEBOOK_INSTANCE_LIFECYCLE_CONFIG` — sagemaker `describe-notebook-instance-lifecycle-config`
- `LW_CFG_AWS_SAGEMAKER_DESCRIBE_PIPELINE` — sagemaker `describe-pipeline`
- `LW_CFG_AWS_SAGEMAKER_DESCRIBE_PIPELINE_DEFINITION_FOR_EXECUTION` — sagemaker `describe-pipeline-definition-for-execution`
- `LW_CFG_AWS_SAGEMAKER_DESCRIBE_PIPELINE_EXECUTION` — sagemaker `describe-pipeline-execution`
- `LW_CFG_AWS_SAGEMAKER_DESCRIBE_PROCESSING_JOB` — sagemaker `describe-processing-job`
- `LW_CFG_AWS_SAGEMAKER_DESCRIBE_PROJECT` — sagemaker `describe-project`
- `LW_CFG_AWS_SAGEMAKER_DESCRIBE_SPACE` — sagemaker `describe-space`
- `LW_CFG_AWS_SAGEMAKER_DESCRIBE_STUDIO_LIFECYCLE_CONFIG` — sagemaker `describe-studio-lifecycle-config`
- `LW_CFG_AWS_SAGEMAKER_DESCRIBE_SUBSCRIBED_WORKTEAM` — sagemaker `describe-subscribed-workteam`
- `LW_CFG_AWS_SAGEMAKER_DESCRIBE_TRAINING_JOB` — sagemaker `describe-training-job`
- `LW_CFG_AWS_SAGEMAKER_DESCRIBE_TRANSFORM_JOB` — sagemaker `describe-transform-job`
- `LW_CFG_AWS_SAGEMAKER_DESCRIBE_TRIAL` — sagemaker `describe-trial`
- `LW_CFG_AWS_SAGEMAKER_DESCRIBE_TRIAL_COMPONENT` — sagemaker `describe-trial-component`
- `LW_CFG_AWS_SAGEMAKER_DESCRIBE_USER_PROFILE` — sagemaker `describe-user-profile`
- `LW_CFG_AWS_SAGEMAKER_DESCRIBE_WORKFORCE` — sagemaker `describe-workforce`
- `LW_CFG_AWS_SAGEMAKER_DESCRIBE_WORKTEAM` — sagemaker `describe-workteam`
- `LW_CFG_AWS_SAGEMAKER_DEVICES` — sagemaker `list-devices`
- `LW_CFG_AWS_SAGEMAKER_DEVICE_FLEETS` — sagemaker `list-device-fleets`
- `LW_CFG_AWS_SAGEMAKER_DOMAINS` — sagemaker `list-domains`
- `LW_CFG_AWS_SAGEMAKER_EDGE_DEPLOYMENT_PLANS` — sagemaker `list-edge-deployment-plans`
- `LW_CFG_AWS_SAGEMAKER_EDGE_PACKAGING_JOBS` — sagemaker `list-edge-packaging-jobs`
- `LW_CFG_AWS_SAGEMAKER_ENDPOINTS` — sagemaker `list-endpoints`
- `LW_CFG_AWS_SAGEMAKER_ENDPOINT_CONFIGS` — sagemaker `list-endpoint-configs`
- `LW_CFG_AWS_SAGEMAKER_EXPERIMENTS` — sagemaker `list-experiments`
- `LW_CFG_AWS_SAGEMAKER_FEATURE_GROUPS` — sagemaker `list-feature-groups`
- `LW_CFG_AWS_SAGEMAKER_FLOW_DEFINITIONS` — sagemaker `list-flow-definitions`
- `LW_CFG_AWS_SAGEMAKER_GET_DEVICE_FLEET_REPORT` — sagemaker `get-device-fleet-report`
- `LW_CFG_AWS_SAGEMAKER_GET_LINEAGE_GROUP_POLICY` — sagemaker `get-lineage-group-policy`
- `LW_CFG_AWS_SAGEMAKER_GET_MODEL_PACKAGE_GROUP_POLICY` — sagemaker `get-model-package-group-policy`
- `LW_CFG_AWS_SAGEMAKER_HUMAN_TASK_UIS` — sagemaker `list-human-task-uis`
- `LW_CFG_AWS_SAGEMAKER_HYPER_PARAMETER_TUNING_JOBS` — sagemaker `list-hyper-parameter-tuning-jobs`
- `LW_CFG_AWS_SAGEMAKER_IMAGES` — sagemaker `list-images`
- `LW_CFG_AWS_SAGEMAKER_IMAGE_VERSIONS` — sagemaker `list-image-versions`
- `LW_CFG_AWS_SAGEMAKER_INFERENCE_EXPERIMENTS` — sagemaker `list-inference-experiments`
- `LW_CFG_AWS_SAGEMAKER_INFERENCE_RECOMMENDATIONS_JOBS` — sagemaker `list-inference-recommendations-jobs`
- `LW_CFG_AWS_SAGEMAKER_INFERENCE_RECOMMENDATIONS_JOB_STEPS` — sagemaker `list-inference-recommendations-job-steps`
- `LW_CFG_AWS_SAGEMAKER_LABELING_JOBS` — sagemaker `list-labeling-jobs`
- `LW_CFG_AWS_SAGEMAKER_LABELING_JOBS_FOR_WORKTEAM` — sagemaker `list-labeling-jobs-for-workteam`
- `LW_CFG_AWS_SAGEMAKER_LINEAGE_GROUPS` — sagemaker `list-lineage-groups`
- `LW_CFG_AWS_SAGEMAKER_MODELS` — sagemaker `list-models`
- `LW_CFG_AWS_SAGEMAKER_MODEL_BIAS_JOB_DEFINITIONS` — sagemaker `list-model-bias-job-definitions`
- `LW_CFG_AWS_SAGEMAKER_MODEL_CARDS` — sagemaker `list-model-cards`
- `LW_CFG_AWS_SAGEMAKER_MODEL_CARD_EXPORT_JOBS` — sagemaker `list-model-card-export-jobs`
- `LW_CFG_AWS_SAGEMAKER_MODEL_CARD_VERSIONS` — sagemaker `list-model-card-versions`
- `LW_CFG_AWS_SAGEMAKER_MODEL_EXPLAINABILITY_JOB_DEFINITIONS` — sagemaker `list-model-explainability-job-definitions`
- `LW_CFG_AWS_SAGEMAKER_MODEL_PACKAGES` — sagemaker `list-model-packages`
- `LW_CFG_AWS_SAGEMAKER_MODEL_PACKAGE_GROUPS` — sagemaker `list-model-package-groups`
- `LW_CFG_AWS_SAGEMAKER_MODEL_QUALITY_JOB_DEFINITIONS` — sagemaker `list-model-quality-job-definitions`
- `LW_CFG_AWS_SAGEMAKER_MONITORING_ALERTS` — sagemaker `list-monitoring-alerts`
- `LW_CFG_AWS_SAGEMAKER_NOTEBOOK_INSTANCES` — sagemaker `list-notebook-instances`
- `LW_CFG_AWS_SAGEMAKER_NOTEBOOK_INSTANCE_LIFECYCLE_CONFIGS` — sagemaker `list-notebook-instance-lifecycle-configs`
- `LW_CFG_AWS_SAGEMAKER_PIPELINES` — sagemaker `list-pipelines`
- `LW_CFG_AWS_SAGEMAKER_PIPELINE_EXECUTIONS` — sagemaker `list-pipeline-executions`
- `LW_CFG_AWS_SAGEMAKER_PIPELINE_PARAMETERS_FOR_EXECUTION` — sagemaker `list-pipeline-parameters-for-execution`
- `LW_CFG_AWS_SAGEMAKER_PROCESSING_JOBS` — sagemaker `list-processing-jobs`
- `LW_CFG_AWS_SAGEMAKER_PROJECTS` — sagemaker `list-projects`
- `LW_CFG_AWS_SAGEMAKER_SPACES` — sagemaker `list-spaces`
- `LW_CFG_AWS_SAGEMAKER_STUDIO_LIFECYCLE_CONFIGS` — sagemaker `list-studio-lifecycle-configs`
- `LW_CFG_AWS_SAGEMAKER_SUBSCRIBED_WORKTEAMS` — sagemaker `list-subscribed-workteams`
- `LW_CFG_AWS_SAGEMAKER_TRAINING_JOBS` — sagemaker `list-training-jobs`
- `LW_CFG_AWS_SAGEMAKER_TRAINING_JOBS_FOR_HYPER_PARAMETER_TUNING_JOB` — sagemaker `list-training-jobs-for-hyper-parameter-tuning-job`
- `LW_CFG_AWS_SAGEMAKER_TRANSFORM_JOBS` — sagemaker `list-transform-jobs`
- `LW_CFG_AWS_SAGEMAKER_TRIALS` — sagemaker `list-trials`
- `LW_CFG_AWS_SAGEMAKER_TRIAL_COMPONENTS` — sagemaker `list-trial-components`
- `LW_CFG_AWS_SAGEMAKER_USER_PROFILES` — sagemaker `list-user-profiles`
- `LW_CFG_AWS_SAGEMAKER_WORKFORCES` — sagemaker `list-workforces`
- `LW_CFG_AWS_SAGEMAKER_WORKTEAMS` — sagemaker `list-workteams`
- `LW_CFG_AWS_SAGEMAKER_MONITORING_SCHEDULES` — Results from Amazon SageMaker Service 'list-monitoring-schedules'

### Schemas

- `LW_CFG_AWS_SCHEMAS_DESCRIBE_DISCOVERER` — Results from Schemas 'describe-discoverer'
- `LW_CFG_AWS_SCHEMAS_DESCRIBE_REGISTRY` — Results from Schemas 'describe-registry'
- `LW_CFG_AWS_SCHEMAS_DESCRIBE_SCHEMA` — Results from Schemas 'describe-schema'
- `LW_CFG_AWS_SCHEMAS_DISCOVERERS` — Results from Schemas 'list-discoverers'
- `LW_CFG_AWS_SCHEMAS_GET_RESOURCE_POLICY` — Results from Schemas 'get-resource-policy'
- `LW_CFG_AWS_SCHEMAS_REGISTRIES` — Results from Schemas 'list-registries'
- `LW_CFG_AWS_SCHEMAS_SCHEMAS` — Results from Schemas 'list-schemas'
- `LW_CFG_AWS_SCHEMAS_SCHEMA_VERSIONS` — Results from Schemas 'list-schema-versions'

### Secrets Manager

- `LW_CFG_AWS_SECRETSMANAGER_DESCRIBE_SECRET` — secretsmanager `describe-secret`
- `LW_CFG_AWS_SECRETSMANAGER_GET_RESOURCE_POLICY` — secretsmanager `get-resource-policy`
- `LW_CFG_AWS_SECRETSMANAGER_SECRETS` — secretsmanager `list-secrets`
- `LW_CFG_AWS_SECRETSMANAGER_SECRET_VERSION_IDS` — secretsmanager `list-secret-version-ids`

### SecurityHub

- `LW_CFG_AWS_SECURITYHUB_ACTION_TARGETS` — AWS SecurityHub `describe-action-targets`
- `LW_CFG_AWS_SECURITYHUB_DESCRIBE_HUB` — AWS SecurityHub `describe-hub`
- `LW_CFG_AWS_SECURITYHUB_DESCRIBE_ORGANIZATION_CONFIGURATION` — AWS SecurityHub `describe-organization-configuration`
- `LW_CFG_AWS_SECURITYHUB_ENABLED_PRODUCTS_FOR_IMPORT` — AWS SecurityHub `list-enabled-products-for-import`
- `LW_CFG_AWS_SECURITYHUB_FINDING_AGGREGATORS` — AWS SecurityHub `list-finding-aggregators`
- `LW_CFG_AWS_SECURITYHUB_GET_ADMINISTRATOR_ACCOUNT` — AWS SecurityHub `get-administrator-account`
- `LW_CFG_AWS_SECURITYHUB_GET_ENABLED_STANDARDS` — AWS SecurityHub `get-enabled-standards`
- `LW_CFG_AWS_SECURITYHUB_GET_FINDING_AGGREGATOR` — AWS SecurityHub `get-finding-aggregator`
- `LW_CFG_AWS_SECURITYHUB_GET_INSIGHTS` — AWS SecurityHub `get-insights`
- `LW_CFG_AWS_SECURITYHUB_GET_INSIGHT_RESULTS` — AWS SecurityHub `get-insight-results`
- `LW_CFG_AWS_SECURITYHUB_INVITATIONS` — AWS SecurityHub `list-invitations`
- `LW_CFG_AWS_SECURITYHUB_MEMBERS` — AWS SecurityHub `list-members`
- `LW_CFG_AWS_SECURITYHUB_ORGANIZATION_ADMIN_ACCOUNTS` — AWS SecurityHub `list-organization-admin-accounts`
- `LW_CFG_AWS_SECURITYHUB_STANDARDS_CONTROLS` — AWS SecurityHub `describe-standards-controls`
