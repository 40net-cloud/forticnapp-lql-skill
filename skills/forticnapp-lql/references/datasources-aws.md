<!-- Generated from FortiCNAPP 26.2 LQL Reference Guide (fetched 2026-08-26). Source:
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

### Access Analyzer

- `LW_CFG_AWS_ACCESSANALYZER` — accessanalyzer `list-analyzers`
- `LW_CFG_AWS_ACCESSANALYZER_FINDINGS` — accessanalyzer `list-findings`

### Account

- `LW_CFG_AWS_ACCOUNT_GET_ALTERNATE_CONTACT` — Results from AWS Account 'get-alternate-contact'

### Accounts

- `LW_CFG_AWS_ACCOUNTS` — `build-integration-account-urn`.

### ACM

- `LW_CFG_AWS_ACM` — acm `list-certificates`
- `LW_CFG_AWS_ACM_DESCRIBE_CERTIFICATE` — acm `describe-certificate`

### ACM Private Certificate Authority

- `LW_CFG_AWS_ACM_PCA_CERTIFICATE_AUTHORITIES` — Results from AWS Certificate Manager Private Certificate Authority 'list-certificate-authorities'
- `LW_CFG_AWS_ACM_PCA_GET_CERTIFICATE_AUTHORITY_CERTIFICATE` — Results from AWS Certificate Manager Private Certificate Authority 'get-certificate-authority-certificate'
- `LW_CFG_AWS_ACM_PCA_GET_POLICY` — Results from AWS Certificate Manager Private Certificate Authority 'get-policy'
- `LW_CFG_AWS_ACM_PCA_PERMISSIONS` — Results from AWS Certificate Manager Private Certificate Authority 'list-permissions'

### All

- `LW_CFG_AWS_ALL` — All AWS config API keys

### AMP (Managed Service for Prometheus)

- `LW_CFG_AWS_AMP_DESCRIBE_ALERT_MANAGER_DEFINITION` — amp `describe-alert-manager-definition`
- `LW_CFG_AWS_AMP_DESCRIBE_LOGGING_CONFIGURATION` — amp `describe-logging-configuration`
- `LW_CFG_AWS_AMP_DESCRIBE_RULE_GROUPS_NAMESPACE` — amp `describe-rule-groups-namespace`
- `LW_CFG_AWS_AMP_DESCRIBE_SCRAPER` — amp `describe-scraper`
- `LW_CFG_AWS_AMP_DESCRIBE_WORKSPACE` — amp `describe-workspace`
- `LW_CFG_AWS_AMP_RULE_GROUPS_NAMESPACES` — amp `list-rule-groups-namespaces`
- `LW_CFG_AWS_AMP_SCRAPERS` — amp `list-scrapers`
- `LW_CFG_AWS_AMP_WORKSPACES` — amp `list-workspaces`

### API Gateway

- `LW_CFG_AWS_APIGATEWAY_GET_API_KEYS` — Amazon API Gateway `get-api-keys`
- `LW_CFG_AWS_APIGATEWAY_GET_AUTHORIZERS` — Amazon API Gateway `get-authorizers`
- `LW_CFG_AWS_APIGATEWAY_GET_BASE_PATH_MAPPINGS` — Amazon API Gateway `get-base-path-mappings`
- `LW_CFG_AWS_APIGATEWAY_GET_CLIENT_CERTIFICATES` — Amazon API Gateway `get-client-certificates`
- `LW_CFG_AWS_APIGATEWAY_GET_DEPLOYMENTS` — Amazon API Gateway `get-deployments`
- `LW_CFG_AWS_APIGATEWAY_GET_DOCUMENTATION_PARTS` — Amazon API Gateway `get-documentation-parts`
- `LW_CFG_AWS_APIGATEWAY_GET_DOCUMENTATION_VERSIONS` — Amazon API Gateway `get-documentation-versions`
- `LW_CFG_AWS_APIGATEWAY_GET_DOMAIN_NAMES` — Amazon API Gateway `get-domain-names`
- `LW_CFG_AWS_APIGATEWAY_GET_GATEWAY_RESPONSES` — Amazon API Gateway `get-gateway-responses`
- `LW_CFG_AWS_APIGATEWAY_GET_MODELS` — Amazon API Gateway `get-models`
- `LW_CFG_AWS_APIGATEWAY_GET_REQUEST_VALIDATORS` — Amazon API Gateway `get-request-validators`
- `LW_CFG_AWS_APIGATEWAY_GET_RESOURCES` — Amazon API Gateway `get-resources`
- `LW_CFG_AWS_APIGATEWAY_GET_REST_APIS` — Amazon API Gateway `get-rest-apis`
- `LW_CFG_AWS_APIGATEWAY_GET_SDK_TYPES` — Amazon API Gateway `get-sdk-types`
- `LW_CFG_AWS_APIGATEWAY_GET_STAGES` — Amazon API Gateway `get-stages`
- `LW_CFG_AWS_APIGATEWAY_GET_USAGE_PLANS` — Amazon API Gateway `get-usage-plans`
- `LW_CFG_AWS_APIGATEWAY_GET_USAGE_PLAN_KEYS` — Amazon API Gateway `get-usage-plan-keys`
- `LW_CFG_AWS_APIGATEWAY_GET_VPC_LINKS` — Amazon API Gateway `get-vpc-links`

### API Gateway V2

- `LW_CFG_AWS_APIGATEWAYV2_GET_APIS` — AmazonApiGatewayV2 `get-apis`
- `LW_CFG_AWS_APIGATEWAYV2_GET_API_MAPPINGS` — AmazonApiGatewayV2 `get-api-mappings`
- `LW_CFG_AWS_APIGATEWAYV2_GET_AUTHORIZERS` — AmazonApiGatewayV2 `get-authorizers`
- `LW_CFG_AWS_APIGATEWAYV2_GET_DEPLOYMENTS` — AmazonApiGatewayV2 `get-deployments`
- `LW_CFG_AWS_APIGATEWAYV2_GET_DOMAIN_NAMES` — AmazonApiGatewayV2 `get-domain-names`
- `LW_CFG_AWS_APIGATEWAYV2_GET_INTEGRATIONS` — AmazonApiGatewayV2 `get-integrations`
- `LW_CFG_AWS_APIGATEWAYV2_GET_INTEGRATION_RESPONSES` — AmazonApiGatewayV2 `get-integration-responses`
- `LW_CFG_AWS_APIGATEWAYV2_GET_MODELS` — AmazonApiGatewayV2 `get-models`
- `LW_CFG_AWS_APIGATEWAYV2_GET_ROUTES` — AmazonApiGatewayV2 `get-routes`
- `LW_CFG_AWS_APIGATEWAYV2_GET_ROUTE_RESPONSES` — AmazonApiGatewayV2 `get-route-responses`
- `LW_CFG_AWS_APIGATEWAYV2_GET_STAGES` — AmazonApiGatewayV2 `get-stages`
- `LW_CFG_AWS_APIGATEWAYV2_GET_VPC_LINKS` — AmazonApiGatewayV2 `get-vpc-links`

### App Runner

- `LW_CFG_AWS_APPRUNNER_AUTO_SCALING_CONFIGURATIONS` — apprunner `list-auto-scaling-configurations`
- `LW_CFG_AWS_APPRUNNER_AUTO_SCALING_CONFIGURATION` — apprunner `describe-auto-scaling-configuration`
- `LW_CFG_AWS_APPRUNNER_CONNECTIONS` — apprunner `list-connections`
- `LW_CFG_AWS_APPRUNNER_OBSERVABILITY_CONFIGURATIONS` — apprunner `list-observability-configurations`
- `LW_CFG_AWS_APPRUNNER_OBSERVABILITY_CONFIGURATION` — apprunner `describe-observability-configuration`
- `LW_CFG_AWS_APPRUNNER_SERVICES` — apprunner `list-services`
- `LW_CFG_AWS_APPRUNNER_SERVICE` — apprunner `describe-service`
- `LW_CFG_AWS_APPRUNNER_OPERATIONS` — apprunner `list-operations`
- `LW_CFG_AWS_APPRUNNER_VPC_CONNECTORS` — apprunner `list-vpc-connectors`
- `LW_CFG_AWS_APPRUNNER_VPC_INGRESS_CONNECTIONS` — apprunner `list-vpc-ingress-connections`
- `LW_CFG_AWS_APPRUNNER_CUSTOM_DOMAINS` — apprunner `describe-custom-domains`
- `LW_CFG_AWS_APPRUNNER_VPC_INGRESS_CONNECTION` — apprunner `describe-vpc-ingress-connection`
- `LW_CFG_AWS_APPRUNNER_DESCRIBE_AUTO_SCALING_CONFIGURATION` — Results from AWS App Runner 'describe-auto-scaling-configuration'
- `LW_CFG_AWS_APPRUNNER_DESCRIBE_OBSERVABILITY_CONFIGURATION` — Results from AWS App Runner 'describe-observability-configuration'
- `LW_CFG_AWS_APPRUNNER_DESCRIBE_SERVICE` — Results from AWS App Runner 'describe-service'
- `LW_CFG_AWS_APPRUNNER_DESCRIBE_VPC_INGRESS_CONNECTION` — Results from AWS App Runner 'describe-vpc-ingress-connection'

### AppConfig

- `LW_CFG_AWS_APPCONFIG_APPLICATIONS` — Results from Amazon AppConfig 'list-applications'
- `LW_CFG_AWS_APPCONFIG_CONFIGURATION_PROFILES` — Results from Amazon AppConfig 'list-configuration-profiles'
- `LW_CFG_AWS_APPCONFIG_DEPLOYMENTS` — Results from Amazon AppConfig 'list-deployments'
- `LW_CFG_AWS_APPCONFIG_DEPLOYMENT_STRATEGIES` — Results from Amazon AppConfig 'list-deployment-strategies'
- `LW_CFG_AWS_APPCONFIG_ENVIRONMENTS` — Results from Amazon AppConfig 'list-environments'
- `LW_CFG_AWS_APPCONFIG_EXTENSIONS` — Results from Amazon AppConfig 'list-extensions'
- `LW_CFG_AWS_APPCONFIG_EXTENSION_ASSOCIATIONS` — Results from Amazon AppConfig 'list-extension-associations'
- `LW_CFG_AWS_APPCONFIG_GET_CONFIGURATION_PROFILE` — Results from Amazon AppConfig 'get-configuration-profile'
- `LW_CFG_AWS_APPCONFIG_GET_DEPLOYMENT` — Results from Amazon AppConfig 'get-deployment'
- `LW_CFG_AWS_APPCONFIG_GET_EXTENSION` — Results from Amazon AppConfig 'get-extension'
- `LW_CFG_AWS_APPCONFIG_GET_EXTENSION_ASSOCIATION` — Results from Amazon AppConfig 'get-extension-association'
- `LW_CFG_AWS_APPCONFIG_GET_HOSTED_CONFIGURATION_VERSION` — Results from Amazon AppConfig 'get-hosted-configuration-version'
- `LW_CFG_AWS_APPCONFIG_HOSTED_CONFIGURATION_VERSIONS` — Results from Amazon AppConfig 'list-hosted-configuration-versions'

### Appflow

- `LW_CFG_AWS_APPFLOW_CONNECTORS` — Results from Amazon Appflow 'list-connectors'
- `LW_CFG_AWS_APPFLOW_CONNECTOR_PROFILES` — Results from Amazon Appflow 'describe-connector-profiles'
- `LW_CFG_AWS_APPFLOW_DESCRIBE_CONNECTOR` — Results from Amazon Appflow 'describe-connector'
- `LW_CFG_AWS_APPFLOW_DESCRIBE_FLOW` — Results from Amazon Appflow 'describe-flow'
- `LW_CFG_AWS_APPFLOW_FLOWS` — Results from Amazon Appflow 'list-flows'
- `LW_CFG_AWS_APPFLOW_FLOW_EXECUTION_RECORDS` — Results from Amazon Appflow 'describe-flow-execution-records'

### Application Auto Scaling

- `LW_CFG_AWS_APPLICATION_AUTOSCALING_SCALING_ACTIVITIES` — Results from Application Auto Scaling 'describe-scaling-activities'
- `LW_CFG_AWS_APPLICATION_AUTOSCALING_SCALING_POLICIES` — Results from Application Auto Scaling 'describe-scaling-policies'
- `LW_CFG_AWS_APPLICATION_AUTOSCALING_SCHEDULED_ACTIONS` — Results from Application Auto Scaling 'describe-scheduled-actions'

### Application Autoscaling

- `LW_CFG_AWS_APPLICATION_AUTOSCALING_SCALABLE_TARGETS` — Application Auto Scaling `describe-scalable-targets`

### AppStream

- `LW_CFG_AWS_APPSTREAM_APPLICATIONS` — appstream `describe-applications`
- `LW_CFG_AWS_APPSTREAM_APPLICATION_FLEET_ASSOCIATIONS` — appstream `describe-application-fleet-associations`
- `LW_CFG_AWS_APPSTREAM_APP_BLOCKS` — appstream `describe-app-blocks`
- `LW_CFG_AWS_APPSTREAM_APP_BLOCK_BUILDERS` — appstream `describe-app-block-builders`
- `LW_CFG_AWS_APPSTREAM_APP_BLOCK_BUILDER_APP_BLOCK_ASSOCIATIONS` — appstream `describe-app-block-builder-app-block-associations`
- `LW_CFG_AWS_APPSTREAM_ASSOCIATED_FLEETS` — appstream `list-associated-fleets`
- `LW_CFG_AWS_APPSTREAM_ASSOCIATED_STACKS` — appstream `list-associated-stacks`
- `LW_CFG_AWS_APPSTREAM_DESCRIBE_THEME_FOR_STACK` — appstream `describe-theme-for-stack`
- `LW_CFG_AWS_APPSTREAM_DIRECTORY_CONFIGS` — appstream `describe-directory-configs`
- `LW_CFG_AWS_APPSTREAM_ENTITLED_APPLICATIONS` — appstream `list-entitled-applications`
- `LW_CFG_AWS_APPSTREAM_ENTITLEMENTS` — appstream `describe-entitlements`
- `LW_CFG_AWS_APPSTREAM_FLEETS` — appstream `describe-fleets`
- `LW_CFG_AWS_APPSTREAM_IMAGES` — appstream `describe-images`
- `LW_CFG_AWS_APPSTREAM_IMAGE_BUILDERS` — appstream `describe-image-builders`
- `LW_CFG_AWS_APPSTREAM_IMAGE_PERMISSIONS` — appstream `describe-image-permissions`
- `LW_CFG_AWS_APPSTREAM_SESSIONS` — appstream `describe-sessions`
- `LW_CFG_AWS_APPSTREAM_STACKS` — appstream `describe-stacks`
- `LW_CFG_AWS_APPSTREAM_USAGE_REPORT_SUBSCRIPTIONS` — appstream `describe-usage-report-subscriptions`
- `LW_CFG_AWS_APPSTREAM_USERS` — appstream `describe-users`
- `LW_CFG_AWS_APPSTREAM_USER_STACK_ASSOCIATIONS` — appstream `describe-user-stack-associations`

### AppSync

- `LW_CFG_AWS_APPSYNC_API_KEYS` — appsync `list-api-keys`
- `LW_CFG_AWS_APPSYNC_DATA_SOURCES` — appsync `list-data-sources`
- `LW_CFG_AWS_APPSYNC_DOMAIN_NAMES` — appsync `list-domain-names`
- `LW_CFG_AWS_APPSYNC_FUNCTIONS` — appsync `list-functions`
- `LW_CFG_AWS_APPSYNC_GET_API_ASSOCIATION` — appsync `get-api-association`
- `LW_CFG_AWS_APPSYNC_GET_API_CACHE` — appsync `get-api-cache`
- `LW_CFG_AWS_APPSYNC_GRAPHQL_APIS` — appsync `list-graphql-apis`
- `LW_CFG_AWS_APPSYNC_RESOLVERS` — appsync `list-resolvers`
- `LW_CFG_AWS_APPSYNC_RESOLVERS_BY_FUNCTION` — appsync `list-resolvers-by-function`
- `LW_CFG_AWS_APPSYNC_TYPES` — appsync `list-types`

### Athena

- `LW_CFG_AWS_ATHENA_APPLICATION_DPU_SIZES` — Amazon Athena `list-application-dpu-sizes`
- `LW_CFG_AWS_ATHENA_CALCULATION_EXECUTIONS` — Amazon Athena `list-calculation-executions`
- `LW_CFG_AWS_ATHENA_DATABASES` — Amazon Athena `list-databases`
- `LW_CFG_AWS_ATHENA_DATA_CATALOGS` — Amazon Athena `list-data-catalogs`
- `LW_CFG_AWS_ATHENA_ENGINE_VERSIONS` — Amazon Athena `list-engine-versions`
- `LW_CFG_AWS_ATHENA_EXECUTORS` — Amazon Athena `list-executors`
- `LW_CFG_AWS_ATHENA_GET_WORK_GROUP` — Amazon Athena `get-work-group`
- `LW_CFG_AWS_ATHENA_NAMED_QUERIES` — Amazon Athena `list-named-queries`
- `LW_CFG_AWS_ATHENA_NOTEBOOK_METADATA` — Amazon Athena `list-notebook-metadata`
- `LW_CFG_AWS_ATHENA_NOTEBOOK_SESSIONS` — Amazon Athena `list-notebook-sessions`
- `LW_CFG_AWS_ATHENA_PREPARED_STATEMENTS` — Amazon Athena `list-prepared-statements`
- `LW_CFG_AWS_ATHENA_QUERY_EXECUTIONS` — Amazon Athena `list-query-executions`
- `LW_CFG_AWS_ATHENA_SESSIONS` — Amazon Athena `list-sessions`
- `LW_CFG_AWS_ATHENA_TABLE_METADATA` — Amazon Athena `list-table-metadata`
- `LW_CFG_AWS_ATHENA_WORK_GROUPS` — Amazon Athena `list-work-groups`

### Auto Scaling

- `LW_CFG_AWS_AUTOSCALING` — Auto Scaling `describe-launch-configurations`
- `LW_CFG_AWS_AUTOSCALING_ADJUSTMENT_TYPES` — Auto Scaling `describe-adjustment-types`
- `LW_CFG_AWS_AUTOSCALING_AUTO_SCALING_GROUPS` — Auto Scaling `describe-auto-scaling-groups`
- `LW_CFG_AWS_AUTOSCALING_AUTO_SCALING_INSTANCES` — Auto Scaling `describe-auto-scaling-instances`
- `LW_CFG_AWS_AUTOSCALING_AUTO_SCALING_NOTIFICATION_TYPES` — Auto Scaling `describe-auto-scaling-notification-types`
- `LW_CFG_AWS_AUTOSCALING_INSTANCE_REFRESHES` — Auto Scaling `describe-instance-refreshes`
- `LW_CFG_AWS_AUTOSCALING_LIFECYCLE_HOOKS` — Auto Scaling `describe-lifecycle-hooks`
- `LW_CFG_AWS_AUTOSCALING_LIFECYCLE_HOOK_TYPES` — Auto Scaling `describe-lifecycle-hook-types`
- `LW_CFG_AWS_AUTOSCALING_LOAD_BALANCERS` — Auto Scaling `describe-load-balancers`
- `LW_CFG_AWS_AUTOSCALING_LOAD_BALANCER_TARGET_GROUPS` — Auto Scaling `describe-load-balancer-target-groups`
- `LW_CFG_AWS_AUTOSCALING_METRIC_COLLECTION_TYPES` — Auto Scaling `describe-metric-collection-types`
- `LW_CFG_AWS_AUTOSCALING_NOTIFICATION_CONFIGURATIONS` — Auto Scaling `describe-notification-configurations`
- `LW_CFG_AWS_AUTOSCALING_POLICIES` — Auto Scaling `describe-policies`
- `LW_CFG_AWS_AUTOSCALING_SCALING_ACTIVITIES` — Auto Scaling `describe-scaling-activities`
- `LW_CFG_AWS_AUTOSCALING_SCALING_PROCESS_TYPES` — Auto Scaling `describe-scaling-process-types`
- `LW_CFG_AWS_AUTOSCALING_SCHEDULED_ACTIONS` — Auto Scaling `describe-scheduled-actions`
- `LW_CFG_AWS_AUTOSCALING_TERMINATION_POLICY_TYPES` — Auto Scaling `describe-termination-policy-types`
- `LW_CFG_AWS_AUTOSCALING_TRAFFIC_SOURCES` — Auto Scaling `describe-traffic-sources`
- `LW_CFG_AWS_AUTOSCALING_WARM_POOL` — Auto Scaling `describe-warm-pool`

### Backup

- `LW_CFG_AWS_BACKUP_BACKUP_VAULTS` — backup `list-backup-vaults`
- `LW_CFG_AWS_BACKUP_GET_BACKUP_VAULT_ACCESS_POLICY` — backup `get-backup-vault-access-policy`
- `LW_CFG_AWS_BACKUP_GET_BACKUP_VAULT_NOTIFICATIONS` — backup `get-backup-vault-notifications`
- `LW_CFG_AWS_BACKUP_BACKUP_JOBS` — Results from AWS Backup 'list-backup-jobs'
- `LW_CFG_AWS_BACKUP_BACKUP_PLANS` — Results from AWS Backup 'list-backup-plans'
- `LW_CFG_AWS_BACKUP_BACKUP_PLAN_TEMPLATES` — Results from AWS Backup 'list-backup-plan-templates'
- `LW_CFG_AWS_BACKUP_BACKUP_PLAN_VERSIONS` — Results from AWS Backup 'list-backup-plan-versions'
- `LW_CFG_AWS_BACKUP_BACKUP_SELECTIONS` — Results from AWS Backup 'list-backup-selections'
- `LW_CFG_AWS_BACKUP_COPY_JOBS` — Results from AWS Backup 'list-copy-jobs'
- `LW_CFG_AWS_BACKUP_DESCRIBE_BACKUP_JOB` — Results from AWS Backup 'describe-backup-job'
- `LW_CFG_AWS_BACKUP_DESCRIBE_BACKUP_VAULT` — Results from AWS Backup 'describe-backup-vault'
- `LW_CFG_AWS_BACKUP_DESCRIBE_FRAMEWORK` — Results from AWS Backup 'describe-framework'
- `LW_CFG_AWS_BACKUP_DESCRIBE_PROTECTED_RESOURCE` — Results from AWS Backup 'describe-protected-resource'
- `LW_CFG_AWS_BACKUP_FRAMEWORKS` — Results from AWS Backup 'list-frameworks'
- `LW_CFG_AWS_BACKUP_GET_BACKUP_PLAN` — Results from AWS Backup 'get-backup-plan'
- `LW_CFG_AWS_BACKUP_GET_BACKUP_PLAN_FROM_TEMPLATE` — Results from AWS Backup 'get-backup-plan-from-template'
- `LW_CFG_AWS_BACKUP_GET_BACKUP_SELECTION` — Results from AWS Backup 'get-backup-selection'
- `LW_CFG_AWS_BACKUP_GET_LEGAL_HOLD` — Results from AWS Backup 'get-legal-hold'
- `LW_CFG_AWS_BACKUP_LEGAL_HOLDS` — Results from AWS Backup 'list-legal-holds'
- `LW_CFG_AWS_BACKUP_PROTECTED_RESOURCES` — Results from AWS Backup 'list-protected-resources'
- `LW_CFG_AWS_BACKUP_RECOVERY_POINTS_BY_RESOURCE` — Results from AWS Backup 'list-recovery-points-by-resource'
- `LW_CFG_AWS_BACKUP_REPORT_PLANS` — Results from AWS Backup 'list-report-plans'
- `LW_CFG_AWS_BACKUP_RESTORE_JOBS` — Results from AWS Backup 'list-restore-jobs'

### Batch

- `LW_CFG_AWS_BATCH_COMPUTE_ENVIRONMENTS` — Results from AWS Batch 'describe-compute-environments'
- `LW_CFG_AWS_BATCH_JOBS` — Results from AWS Batch 'list-jobs'
- `LW_CFG_AWS_BATCH_JOB_DEFINITIONS` — Results from AWS Batch 'describe-job-definitions'
- `LW_CFG_AWS_BATCH_JOB_DESCRIPTION` — Results from AWS Batch 'describe-jobs'
- `LW_CFG_AWS_BATCH_JOB_QUEUES` — Results from AWS Batch 'describe-job-queues'
- `LW_CFG_AWS_BATCH_SCHEDULING_POLICIES` — Results from AWS Batch 'list-scheduling-policies'
- `LW_CFG_AWS_BATCH_SCHEDULING_POLICY_DESCRIPTIONS` — Results from AWS Batch 'describe-scheduling-policies'

### Bedrock

- `LW_CFG_AWS_BEDROCK_CUSTOM_MODELS` — Bedrock `list-custom-models`
- `LW_CFG_AWS_BEDROCK_GET_CUSTOM_MODEL` — Bedrock `get-custom-model`
- `LW_CFG_AWS_BEDROCK_GET_MODEL_INVOCATION_LOGGING_CONFIGURATION` — Bedrock `get-model-invocation-logging-configuration`

### Budgets

- `LW_CFG_AWS_BUDGETS_BUDGETS` — budgets `describe-budgets`
- `LW_CFG_AWS_BUDGETS_BUDGET_ACTIONS_FOR_ACCOUNT` — budgets `describe-budget-actions-for-account`
- `LW_CFG_AWS_BUDGETS_BUDGET_ACTION_HISTORIES` — budgets `describe-budget-action-histories`
- `LW_CFG_AWS_BUDGETS_DESCRIBE_BUDGET_PERFORMANCE_HISTORY` — budgets `describe-budget-performance-history`
- `LW_CFG_AWS_BUDGETS_NOTIFICATIONS_FOR_BUDGET` — budgets `describe-notifications-for-budget`
- `LW_CFG_AWS_BUDGETS_SUBSCRIBERS_FOR_NOTIFICATION` — budgets `describe-subscribers-for-notification`

### Cloud Map

- `LW_CFG_AWS_SERVICEDISCOVERY_GET_INSTANCE` — servicediscovery `get-instance`
- `LW_CFG_AWS_SERVICEDISCOVERY_GET_NAMESPACE` — servicediscovery `get-instance`
- `LW_CFG_AWS_SERVICEDISCOVERY_GET_OPERATION` — servicediscovery `get-operation`
- `LW_CFG_AWS_SERVICEDISCOVERY_GET_SERVICE` — servicediscovery `get-service`
- `LW_CFG_AWS_SERVICEDISCOVERY_GET_SERVICE_ATTRIBUTES` — servicediscovery `get-service-attributes`
- `LW_CFG_AWS_SERVICEDISCOVERY_INSTANCES` — servicediscovery `list-instances`
- `LW_CFG_AWS_SERVICEDISCOVERY_NAMESPACES` — servicediscovery `list-namespaces`
- `LW_CFG_AWS_SERVICEDISCOVERY_OPERATIONS` — servicediscovery `list-operations`
- `LW_CFG_AWS_SERVICEDISCOVERY_SERVICES` — servicediscovery `list-services`

### CloudFormation

- `LW_CFG_AWS_CLOUDFORMATION_DESCRIBE_STACK_RESOURCE` — AWS CloudFormation `describe-stack-resource`
- `LW_CFG_AWS_CLOUDFORMATION_DESCRIBE_STACK_SET` — AWS CloudFormation `describe-stack-set`
- `LW_CFG_AWS_CLOUDFORMATION_DESCRIBE_STACK_SET_OPERATION` — AWS CloudFormation `describe-stack-set-operation`
- `LW_CFG_AWS_CLOUDFORMATION_GET_STACK_POLICY` — AWS CloudFormation `get-stack-policy`
- `LW_CFG_AWS_CLOUDFORMATION_STACKS` — AWS CloudFormation `describe-stacks`
- `LW_CFG_AWS_CLOUDFORMATION_STACK_INSTANCES` — AWS CloudFormation `list-stack-instances`
- `LW_CFG_AWS_CLOUDFORMATION_STACK_RESOURCES` — AWS CloudFormation `list-stack-resources`
- `LW_CFG_AWS_CLOUDFORMATION_STACK_RESOURCE_DRIFTS` — AWS CloudFormation `describe-stack-resource-drifts`
- `LW_CFG_AWS_CLOUDFORMATION_STACK_SETS` — AWS CloudFormation `list-stack-sets`
- `LW_CFG_AWS_CLOUDFORMATION_STACK_SET_OPERATIONS` — AWS CloudFormation `list-stack-set-operations`
- `LW_CFG_AWS_CLOUDFORMATION_STACK_SET_OPERATION_RESULTS` — AWS CloudFormation `list-stack-set-operation-results`

### CloudFront

- `LW_CFG_AWS_CLOUDFRONT` — AWS CloudFront `list-distributions`
- `LW_CFG_AWS_CLOUDFRONT_GET_DISTRIBUTION_CONFIG` — AWS CloudFront `get-distribution-config`

### CloudTrail

- `LW_CFG_AWS_CLOUDTRAIL` — cloudtrail `describe-trails`
- `LW_CFG_AWS_CLOUDTRAIL_GET_EVENT_SELECTORS` — cloudtrail `get-event-selectors`
- `LW_CFG_AWS_CLOUDTRAIL_GET_TRAIL_STATUS` — cloudtrail `get-trail-status`
- `LW_CFG_AWS_CLOUDTRAIL_SHADOW_TRAILS` — cloudtrail `describe-trails`

### CloudWatch

- `LW_CFG_AWS_CLOUDWATCH` — cloudwatch `describe-alarms`

### CloudWatch Observability Access Manager

- `LW_CFG_AWS_OAM_ATTACHED_LINKS` — oam `list-attached-links`
- `LW_CFG_AWS_OAM_GET_LINK` — oam `get-link`
- `LW_CFG_AWS_OAM_GET_SINK` — oam `get-sink`
- `LW_CFG_AWS_OAM_GET_SINK_POLICY` — oam `get-sink-policy`
- `LW_CFG_AWS_OAM_LINKS` — oam `list-links`
- `LW_CFG_AWS_OAM_SINKS` — oam `list-sinks`

### CodeBuild

- `LW_CFG_AWS_CODEBUILD_BATCH_GET_BUILDS` — AWS CodeBuild `batch-get-builds`
- `LW_CFG_AWS_CODEBUILD_BUILDS` — AWS CodeBuild `list-builds`
- `LW_CFG_AWS_CODEBUILD_BATCH_GET_PROJECTS` — AWS CodeBuild `batch-get-projects`
- `LW_CFG_AWS_CODEBUILD_PROJECTS` — AWS CodeBuild `list-projects`

### CodePipeline

- `LW_CFG_AWS_CODEPIPELINE_ACTION_EXECUTIONS` — Results from AWS CodePipeline 'list-action-executions'
- `LW_CFG_AWS_CODEPIPELINE_ACTION_TYPES` — Results from AWS CodePipeline 'list-action-types'
- `LW_CFG_AWS_CODEPIPELINE_GET_ACTION_TYPE` — Results from AWS CodePipeline 'get-action-type'
- `LW_CFG_AWS_CODEPIPELINE_GET_PIPELINE` — Results from AWS CodePipeline 'get-pipeline'
- `LW_CFG_AWS_CODEPIPELINE_GET_PIPELINE_EXECUTION` — Results from AWS CodePipeline 'get-pipeline-execution'
- `LW_CFG_AWS_CODEPIPELINE_GET_PIPELINE_STATE` — Results from AWS CodePipeline 'get-pipeline-state'
- `LW_CFG_AWS_CODEPIPELINE_PIPELINES` — Results from AWS CodePipeline 'list-pipelines'
- `LW_CFG_AWS_CODEPIPELINE_PIPELINE_EXECUTIONS` — Results from AWS CodePipeline 'list-pipeline-executions'
- `LW_CFG_AWS_CODEPIPELINE_RULE_EXECUTIONS` — Results from AWS CodePipeline 'list-rule-executions'
- `LW_CFG_AWS_CODEPIPELINE_RULE_TYPES` — Results from AWS CodePipeline 'list-rule-types'
- `LW_CFG_AWS_CODEPIPELINE_WEBHOOKS` — Results from AWS CodePipeline 'list-webhooks'

### Cognito

- `LW_CFG_AWS_COGNITO_IDP_USER_POOLS` — cognito-idp `list-user-pools`
- `LW_CFG_AWS_COGNITO_IDP_USERS` — congito-idp `list-users`
- `LW_CFG_AWS_COGNITO_IDP_RISK_CONFIGURATION` — cognito-idp `describe-risk-configuration`
- `LW_CFG_AWS_COGNITO_IDP_USER_POOL` — cognito-idp `describe-user-pool`
- `LW_CFG_AWS_COGNITO_IDP_USER_POOL_DOMAIN` — cognito-idp `describe-user-pool-domain`
- `LW_CFG_AWS_COGNITO_GET_CSV_HEADER` — cognito-idp `get-csv-header`
- `LW_CFG_AWS_COGNITO_GET_SIGNING_CERTIFICATE` — cognito-idp `get-signing-certificate`
- `LW_CFG_AWS_COGNITO_IDP_GET_UI_CUSTOMIZATION` — cognito-idp `get-ui-customization`
- `LW_CFG_AWS_COGNITO_IDP_GET_USER_POOL_MFA_CONFIG` — cognito-idp `get-user-pool-mfa-config`
- `LW_CFG_AWS_COGNITO_IDP_GROUPS` — cognito-idp `list-groups`
- `LW_CFG_AWS_COGNITO_IDP_IDENTITY_PROVIDERS` — cognito-idp `list-identity-providers`
- `LW_CFG_AWS_COGNITO_IDP_IDENTITY_PROVIDER` — cognito-idp `describe-identity-provider`
- `LW_CFG_AWS_COGNITO_IDP_RESOURCE_SERVERS` — cognito-idp `list-resource-servers`
- `LW_CFG_AWS_COGNITO_IDP_USER_IMPORT_JOBS` — cognito-idp `list-user-import-jobs`
- `LW_CFG_AWS_COGNITO_IDP_USER_POOL_CLIENTS` — cognito-idp `list-user-pool-clients`
- `LW_CFG_AWS_COGNITO_IDP_USER_POOL_CLIENT` — cognito-idp `describe-user-pool-client`
- `LW_CFG_AWS_COGNITO_IDP_DESCRIBE_IDENTITY_PROVIDER` — Results from Amazon Cognito Identity Provider 'describe-identity-provider'
- `LW_CFG_AWS_COGNITO_IDP_DESCRIBE_RISK_CONFIGURATION` — Results from Amazon Cognito Identity Provider 'describe-risk-configuration'
- `LW_CFG_AWS_COGNITO_IDP_DESCRIBE_USER_POOL` — Results from Amazon Cognito Identity Provider 'describe-user-pool'
- `LW_CFG_AWS_COGNITO_IDP_DESCRIBE_USER_POOL_CLIENT` — Results from Amazon Cognito Identity Provider 'describe-user-pool-client'
- `LW_CFG_AWS_COGNITO_IDP_DESCRIBE_USER_POOL_DOMAIN` — Results from Amazon Cognito Identity Provider 'describe-user-pool-domain'
- `LW_CFG_AWS_COGNITO_IDP_GET_CSV_HEADER` — Results from Amazon Cognito Identity Provider 'get-csv-header'
- `LW_CFG_AWS_COGNITO_IDP_GET_SIGNING_CERTIFICATE` — Results from Amazon Cognito Identity Provider 'get-signing-certificate'

### Compute Optimizer

- `LW_CFG_AWS_COMPUTE_OPTIMIZER_GET_AUTO_SCALING_GROUP_RECOMMENDATIONS` — Results from AWS Compute Optimizer 'get-auto-scaling-group-recommendations'
- `LW_CFG_AWS_COMPUTE_OPTIMIZER_GET_EBS_VOLUME_RECOMMENDATIONS` — Results from AWS Compute Optimizer 'get-ebs-volume-recommendations'
- `LW_CFG_AWS_COMPUTE_OPTIMIZER_GET_EC2_INSTANCE_RECOMMENDATIONS` — Results from AWS Compute Optimizer 'get-ec2-instance-recommendations'
- `LW_CFG_AWS_COMPUTE_OPTIMIZER_GET_ENROLLMENT_STATUS` — Results from AWS Compute Optimizer 'get-enrollment-status'
- `LW_CFG_AWS_COMPUTE_OPTIMIZER_GET_LAMBDA_FUNCTION_RECOMMENDATIONS` — Results from AWS Compute Optimizer 'get-lambda-function-recommendations'
- `LW_CFG_AWS_COMPUTE_OPTIMIZER_GET_RECOMMENDATION_PREFERENCES` — Results from AWS Compute Optimizer 'get-recommendation-preferences'
- `LW_CFG_AWS_COMPUTE_OPTIMIZER_GET_RECOMMENDATION_SUMMARIES` — Results from AWS Compute Optimizer 'get-recommendation-summaries'
- `LW_CFG_AWS_COMPUTE_OPTIMIZER_RECOMMENDATION_EXPORT_JOBS` — Results from AWS Compute Optimizer 'describe-recommendation-export-jobs'

### Config

- `LW_CFG_AWS_CONFIG_CONFIGURATION_RECORDERS` — configservice `describe-configuration-recorders`
- `LW_CFG_AWS_CONFIG_CONFIGURATION_RECORDERS_STATUS` — configservice `describe-configuration-recorder-status`
- `LW_CFG_AWS_CONFIG_DELIVERY_CHANNELS` — configservice `describe-delivery-channels`
- `LW_CFG_AWS_CONFIG_DELIVERY_CHANNELS_STATUS` — configservice `describe-delivery-channel-status`

### Cost Explorer

- `LW_CFG_AWS_CE_COMMITMENT_PURCHASE_ANALYSES` — ce `list-commitment-purchase-analyses`
- `LW_CFG_AWS_CE_COST_ALLOCATION_TAGS` — ce `list-cost-allocation-tags`
- `LW_CFG_AWS_CE_COST_ALLOCATION_TAG_BACKFILL_HISTORY` — ce `list-cost-allocation-tag-backfill-history`
- `LW_CFG_AWS_CE_COST_CATEGORY_DEFINITIONS` — ce `list-cost-category-definitions`
- `LW_CFG_AWS_CE_DESCRIBE_COST_CATEGORY_DEFINITION` — ce `describe-cost-category-definition`
- `LW_CFG_AWS_CE_GET_ANOMALY_MONITORS` — ce `get-anomaly-monitors`
- `LW_CFG_AWS_CE_GET_ANOMALY_SUBSCRIPTIONS` — ce `get-anomaly-subscriptions`
- `LW_CFG_AWS_CE_GET_COMMITMENT_PURCHASE_ANALYSIS` — ce `get-commitment-purchase-analysis`

### Cost Optimization Hub

- `LW_CFG_AWS_COST_OPTIMIZATION_HUB_ENROLLMENT_STATUSES` — Results from Cost Optimization Hub 'list-enrollment-statuses'
- `LW_CFG_AWS_COST_OPTIMIZATION_HUB_GET_PREFERENCES` — Results from Cost Optimization Hub 'get-preferences'
- `LW_CFG_AWS_COST_OPTIMIZATION_HUB_GET_RECOMMENDATION` — Results from Cost Optimization Hub 'get-recommendation'
- `LW_CFG_AWS_COST_OPTIMIZATION_HUB_RECOMMENDATIONS` — Results from Cost Optimization Hub 'list-recommendations'

### DataSync

- `LW_CFG_AWS_DATASYNC_AGENTS` — Results from AWS DataSync 'list-agents'
- `LW_CFG_AWS_DATASYNC_DESCRIBE_AGENT` — Results from AWS DataSync 'describe-agent'
- `LW_CFG_AWS_DATASYNC_DESCRIBE_DISCOVERY_JOB` — Results from AWS DataSync 'describe-discovery-job'
- `LW_CFG_AWS_DATASYNC_DESCRIBE_LOCATION_AZURE_BLOB` — Results from AWS DataSync 'describe-location-azure-blob'
- `LW_CFG_AWS_DATASYNC_DESCRIBE_LOCATION_EFS` — Results from AWS DataSync 'describe-location-efs'
- `LW_CFG_AWS_DATASYNC_DESCRIBE_LOCATION_FSX_LUSTRE` — Results from AWS DataSync 'describe-location-fsx-lustre'
- `LW_CFG_AWS_DATASYNC_DESCRIBE_LOCATION_FSX_WINDOWS` — Results from AWS DataSync 'describe-location-fsx-windows'
- `LW_CFG_AWS_DATASYNC_DESCRIBE_LOCATION_HDFS` — Results from AWS DataSync 'describe-location-hdfs'
- `LW_CFG_AWS_DATASYNC_DESCRIBE_LOCATION_NFS` — Results from AWS DataSync 'describe-location-nfs'
- `LW_CFG_AWS_DATASYNC_DESCRIBE_LOCATION_OBJECT_STORAGE` — Results from AWS DataSync 'describe-location-object-storage'
- `LW_CFG_AWS_DATASYNC_DESCRIBE_LOCATION_S3` — Results from AWS DataSync 'describe-location-s3'
- `LW_CFG_AWS_DATASYNC_DESCRIBE_LOCATION_SMB` — Results from AWS DataSync 'describe-location-smb'
- `LW_CFG_AWS_DATASYNC_DESCRIBE_STORAGE_SYSTEM` — Results from AWS DataSync 'describe-storage-system'
- `LW_CFG_AWS_DATASYNC_DESCRIBE_TASK` — Results from AWS DataSync 'describe-task'
- `LW_CFG_AWS_DATASYNC_DESCRIBE_TASK_EXECUTION` — Results from AWS DataSync 'describe-task-execution'
- `LW_CFG_AWS_DATASYNC_DISCOVERY_JOBS` — Results from AWS DataSync 'list-discovery-jobs'
- `LW_CFG_AWS_DATASYNC_LOCATIONS` — Results from AWS DataSync 'list-locations'
- `LW_CFG_AWS_DATASYNC_STORAGE_SYSTEMS` — Results from AWS DataSync 'list-storage-systems'
- `LW_CFG_AWS_DATASYNC_TASKS` — Results from AWS DataSync 'list-tasks'
- `LW_CFG_AWS_DATASYNC_TASK_EXECUTIONS` — Results from AWS DataSync 'list-task-executions'

### DAX

- `LW_CFG_AWS_DAX_CLUSTERS` — dax `describe-clusters`
- `LW_CFG_AWS_DAX_PARAMETERS` — dax `describe-parameters`
- `LW_CFG_AWS_DAX_PARAMETER_GROUPS` — dax `describe-parameter-groups`
- `LW_CFG_AWS_DAX_SUBNET_GROUPS` — dax `describe-subnet-groups`

### Detective

- `LW_CFG_AWS_DETECTIVE_DATASOURCE_PACKAGES` — Results from Amazon Detective 'list-datasource-packages'
- `LW_CFG_AWS_DETECTIVE_GET_INVESTIGATION` — Results from Amazon Detective 'get-investigation'
- `LW_CFG_AWS_DETECTIVE_GRAPHS` — Results from Amazon Detective 'list-graphs'
- `LW_CFG_AWS_DETECTIVE_INDICATORS` — Results from Amazon Detective 'list-indicators'
- `LW_CFG_AWS_DETECTIVE_INVESTIGATIONS` — Results from Amazon Detective 'list-investigations'
- `LW_CFG_AWS_DETECTIVE_INVITATIONS` — Results from Amazon Detective 'list-invitations'
- `LW_CFG_AWS_DETECTIVE_MEMBERS` — Results from Amazon Detective 'list-members'

### Direct Connect

- `LW_CFG_AWS_DIRECTCONNECT_CONNECTIONS` — Results from AWS Direct Connect 'describe-connections'
- `LW_CFG_AWS_DIRECTCONNECT_CUSTOMER_METADATA` — Results from AWS Direct Connect 'describe-customer-metadata'
- `LW_CFG_AWS_DIRECTCONNECT_DESCRIBE_LOA` — Results from AWS Direct Connect 'describe-loa'
- `LW_CFG_AWS_DIRECTCONNECT_DIRECT_CONNECT_GATEWAYS` — Results from AWS Direct Connect 'describe-direct-connect-gateways'
- `LW_CFG_AWS_DIRECTCONNECT_DIRECT_CONNECT_GATEWAY_ASSOCIATIONS` — Results from AWS Direct Connect 'describe-direct-connect-gateway-associations'
- `LW_CFG_AWS_DIRECTCONNECT_DIRECT_CONNECT_GATEWAY_ASSOCIATION_PROPOSALS` — Results from AWS Direct Connect 'describe-direct-connect-gateway-association-proposals'
- `LW_CFG_AWS_DIRECTCONNECT_DIRECT_CONNECT_GATEWAY_ATTACHMENTS` — Results from AWS Direct Connect 'describe-direct-connect-gateway-attachments'
- `LW_CFG_AWS_DIRECTCONNECT_LAGS` — Results from AWS Direct Connect 'describe-lags'
- `LW_CFG_AWS_DIRECTCONNECT_LOCATIONS` — Results from AWS Direct Connect 'describe-locations'
- `LW_CFG_AWS_DIRECTCONNECT_VIRTUAL_GATEWAYS` — Results from AWS Direct Connect 'describe-virtual-gateways'
- `LW_CFG_AWS_DIRECTCONNECT_VIRTUAL_INTERFACES` — Results from AWS Direct Connect 'describe-virtual-interfaces'

### DMS

- `LW_CFG_AWS_DMS_ACCOUNT_ATTRIBUTES` — AWS Database Migration Service `describe-account-attributes`
- `LW_CFG_AWS_DMS_APPLICABLE_INDIVIDUAL_ASSESSMENTS` — AWS Database Migration Service `describe-applicable-individual-assessments`
- `LW_CFG_AWS_DMS_CERTIFICATES` — AWS Database Migration Service `describe-certificates`
- `LW_CFG_AWS_DMS_DESCRIBE_ENDPOINT_SETTINGS` — AWS Database Migration Service `describe-endpoint-settings`
- `LW_CFG_AWS_DMS_DESCRIBE_REFRESH_SCHEMAS_STATUS` — AWS Database Migration Service `describe-refresh-schemas-status`
- `LW_CFG_AWS_DMS_ENDPOINTS` — AWS Database Migration Service `describe-endpoints`
- `LW_CFG_AWS_DMS_EVENT_SUBSCRIPTIONS` — AWS Database Migration Service `describe-event-subscriptions`
- `LW_CFG_AWS_DMS_FLEET_ADVISOR_COLLECTORS` — AWS Database Migration Service `describe-fleet-advisor-collectors`
- `LW_CFG_AWS_DMS_FLEET_ADVISOR_DATABASES` — AWS Database Migration Service `describe-fleet-advisor-databases`
- `LW_CFG_AWS_DMS_FLEET_ADVISOR_LSA_ANALYSIS` — AWS Database Migration Service `describe-fleet-advisor-lsa-analysis`
- `LW_CFG_AWS_DMS_FLEET_ADVISOR_SCHEMAS` — AWS Database Migration Service `describe-fleet-advisor-schemas`
- `LW_CFG_AWS_DMS_PENDING_MAINTENANCE_ACTIONS` — AWS Database Migration Service `describe-pending-maintenance-actions`
- `LW_CFG_AWS_DMS_REPLICATION_INSTANCES` — AWS Database Migration Service `describe-replication-instances`
- `LW_CFG_AWS_DMS_REPLICATION_INSTANCE_TASK_LOGS` — AWS Database Migration Service `describe-replication-instance-task-logs`
- `LW_CFG_AWS_DMS_REPLICATION_SUBNET_GROUPS` — AWS Database Migration Service `describe-replication-subnet-groups`
- `LW_CFG_AWS_DMS_REPLICATION_TASKS` — AWS Database Migration Service `describe-replication-tasks`
- `LW_CFG_AWS_DMS_REPLICATION_TASK_ASSESSMENT_RESULTS` — AWS Database Migration Service `describe-replication-task-assessment-results`
- `LW_CFG_AWS_DMS_REPLICATION_TASK_ASSESSMENT_RUNS` — AWS Database Migration Service `describe-replication-task-assessment-runs`
- `LW_CFG_AWS_DMS_REPLICATION_TASK_INDIVIDUAL_ASSESSMENTS` — AWS Database Migration Service `describe-replication-task-individual-assessments`
- `LW_CFG_AWS_DMS_SCHEMAS` — AWS Database Migration Service `describe-schemas`
- `LW_CFG_AWS_DMS_TABLE_STATISTICS` — AWS Database Migration Service `describe-table-statistics`

### DocumentDB with MongoDB Compatibility

- `LW_CFG_AWS_DOCDB_DB_CLUSTERS` — Amazon DocumentDB with MongoDB compatibility `describe-db-clusters`
- `LW_CFG_AWS_DOCDB_DB_CLUSTER_PARAMETER_GROUPS` — Amazon DocumentDB with MongoDB compatibility `describe-db-cluster-parameter-groups`
- `LW_CFG_AWS_DOCDB_DB_CLUSTER_SNAPSHOTS` — Amazon DocumentDB with MongoDB compatibility `describe-db-cluster-snapshots`
- `LW_CFG_AWS_DOCDB_DB_ENGINE_VERSIONS` — Amazon DocumentDB with MongoDB compatibility `describe-db-engine-versions`
- `LW_CFG_AWS_DOCDB_DB_INSTANCES` — Amazon DocumentDB with MongoDB compatibility `describe-db-instances`
- `LW_CFG_AWS_DOCDB_DB_SUBNET_GROUPS` — Amazon DocumentDB with MongoDB compatibility `describe-db-subnet-groups`
- `LW_CFG_AWS_DOCDB_DESCRIBE_DB_CLUSTER_SNAPSHOT_ATTRIBUTES` — Amazon DocumentDB with MongoDB compatibility `describe-db-cluster-snapshot-attributes`
- `LW_CFG_AWS_DOCDB_ENGINE_DEFAULT_CLUSTER_PARAMETERS` — Amazon DocumentDB with MongoDB compatibility `describe-engine-default-cluster-parameters`
- `LW_CFG_AWS_DOCDB_EVENT_SUBSCRIPTIONS` — Amazon DocumentDB with MongoDB compatibility `describe-event-subscriptions`
- `LW_CFG_AWS_DOCDB_GLOBAL_CLUSTERS` — Amazon DocumentDB with MongoDB compatibility `describe-global-clusters`

### DynamoDB

- `LW_CFG_AWS_DYNAMODB_BACKUPS` — dynamodb `list-backups`
- `LW_CFG_AWS_DYNAMODB_DESCRIBE_CONTINUOUS_BACKUPS` — dynamodb `describe-continuous-backups`
- `LW_CFG_AWS_DYNAMODB_EXPORT` — dynamodb `describe-export`
- `LW_CFG_AWS_DYNAMODB_EXPORTS` — dynamodb `list-exports`
- `LW_CFG_AWS_DYNAMODB_GLOBAL_TABLE` — dynamodb `describe-global-table`
- `LW_CFG_AWS_DYNAMODB_GLOBAL_TABLES` — dynamodb `list-global-tables`
- `LW_CFG_AWS_DYNAMODB_TABLES` — dynamodb `list-tables`
- `LW_CFG_AWS_DYNAMODB_TABLES_DESCRIBE_TABLE` — dynamodb `describe-table`
- `LW_CFG_AWS_DYNAMODB_DESCRIBE_EXPORT` — Results from Amazon DynamoDB 'describe-export'
- `LW_CFG_AWS_DYNAMODB_DESCRIBE_GLOBAL_TABLE` — Results from Amazon DynamoDB 'describe-global-table'

### EC2

- `LW_CFG_AWS_EC2_ADDRESSES` — ec2 `describe-addresses`
- `LW_CFG_AWS_EC2_CUSTOMER_GATEWAYS` — ec2 `describe-customer-gateways`
- `LW_CFG_AWS_EC2_DHCP_OPTIONS` — ec2 `describe-dhcp-options`
- `LW_CFG_AWS_EC2_EBS_ENCRYPTION_BY_DEFAULT` — ec2 `get-ebs-encryption-by-default`
- `LW_CFG_AWS_EC2_GET_MANAGED_PREFIX_LIST_ENTRIES` — ec2 `get-managed-prefix-list-entries`
- `LW_CFG_AWS_EC2_HOSTS` — ec2 `describe-hosts`
- `LW_CFG_AWS_EC2_IMAGES` — ec2 `describe-images`
- `LW_CFG_AWS_EC2_INSTANCES` — ec2 `describe-instances`
- `LW_CFG_AWS_EC2_INTERNET_GATEWAYS` — ec2 `describe-internet-gateways`
- `LW_CFG_AWS_EC2_KEY_PAIRS` — ec2 `describe-key-pairs`
- `LW_CFG_AWS_EC2_LAUNCH_TEMPLATE_VERSIONS` — ec2 `describe-launch-template-versions`
- `LW_CFG_AWS_EC2_LAUNCH_TEMPLATES` — ec2 `describe-launch-templates`
- `LW_CFG_AWS_EC2_MANAGED_PREFIX_LISTS` — ec2 `describe-managed-prefix-lists`
- `LW_CFG_AWS_EC2_NAT_GATEWAYS` — ec2 `describe-nat-gateways`
- `LW_CFG_AWS_EC2_NETWORK_ACLS` — ec2 `describe-network-acls`
- `LW_CFG_AWS_EC2_NETWORK_INTERFACES` — ec2 `describe-network-interfaces`
- `LW_CFG_AWS_EC2_REGIONS` — ec2 `describe-regions`
- `LW_CFG_AWS_EC2_ROUTE_TABLES` — ec2 `describe-route-tables`
- `LW_CFG_AWS_EC2_SECURITY_GROUPS` — ec2 `describe-security-groups`
- `LW_CFG_AWS_EC2_SNAPSHOTS` — ec2 `describe-snapshots`
- `LW_CFG_AWS_EC2_SNAPSHOTS_DESCRIBE_ATTRIBUTES` — ec2 `describe-snapshot-attribute` This currently contains only the values of the createVolumePermission attribute for non-encrypted volumes.
- `LW_CFG_AWS_EC2_SPOT_INSTANCE_REQUESTS` — ec2 `describe-spot-instance-requests`
- `LW_CFG_AWS_EC2_SUBNETS` — ec2 `describe-subnets`
- `LW_CFG_AWS_EC2_TRANSIT_GATEWAY_PEERING_ATTACHMENTS` — ec2 `describe-transit-gateway-peering-attachments`
- `LW_CFG_AWS_EC2_TRANSIT_GATEWAY_ROUTE_TABLES` — ec2 `describe-transit-gateway-route-tables`
- `LW_CFG_AWS_EC2_TRANSIT_GATEWAY_VPC_ATTACHMENTS` — ec2 `describe-transit-gateway-vpc-attachments`
- `LW_CFG_AWS_EC2_TRANSIT_GATEWAYS` — ec2 `describe-transit-gateways`
- `LW_CFG_AWS_EC2_SEARCH_TRANSIT_GATEWAY_ROUTES` — ec2 `search-transit-gateway-routes`
- `LW_CFG_AWS_EC2_VOLUMES` — ec2 `describe-volumes`
- `LW_CFG_AWS_EC2_VPC_ENDPOINTS` — ec2 `describe-vpc-endpoints`
- `LW_CFG_AWS_EC2_VPC_FLOW_LOGS` — ec2 `describe-flow-logs`
- `LW_CFG_AWS_EC2_VPC_PEERING_CONNECTIONS` — ec2 `describe-vpc-peering-connections`
- `LW_CFG_AWS_EC2_VPCS` — ec2 `describe-vpcs`
- `LW_CFG_AWS_EC2_VPN_CONNECTIONS` — ec2 `describe-vpn-connections`
- `LW_CFG_AWS_EC2_VPN_GATEWAYS` — ec2 `describe-vpn-gateways`
- `LW_CFG_AWS_EC2_TRANSIT_GATEWAY_ATTACHMENTS` — Results from Amazon Elastic Compute Cloud 'describe-transit-gateway-attachments'
- `LW_CFG_AWS_EC2_RESERVED_INSTANCES` — Results from Amazon Elastic Compute Cloud 'describe-reserved-instances'

### EC2 Image Builder

- `LW_CFG_AWS_IMAGEBUILDER_COMPONENTS` — Results from EC2 Image Builder 'list-components'
- `LW_CFG_AWS_IMAGEBUILDER_COMPONENT_BUILD_VERSIONS` — Results from EC2 Image Builder 'list-component-build-versions'
- `LW_CFG_AWS_IMAGEBUILDER_CONTAINER_RECIPES` — Results from EC2 Image Builder 'list-container-recipes'
- `LW_CFG_AWS_IMAGEBUILDER_DISTRIBUTION_CONFIGURATIONS` — Results from EC2 Image Builder 'list-distribution-configurations'
- `LW_CFG_AWS_IMAGEBUILDER_GET_COMPONENT` — Results from EC2 Image Builder 'get-component'
- `LW_CFG_AWS_IMAGEBUILDER_GET_COMPONENT_POLICY` — Results from EC2 Image Builder 'get-component-policy'
- `LW_CFG_AWS_IMAGEBUILDER_GET_CONTAINER_RECIPE` — Results from EC2 Image Builder 'get-container-recipe'
- `LW_CFG_AWS_IMAGEBUILDER_GET_CONTAINER_RECIPE_POLICY` — Results from EC2 Image Builder 'get-container-recipe-policy'
- `LW_CFG_AWS_IMAGEBUILDER_GET_DISTRIBUTION_CONFIGURATION` — Results from EC2 Image Builder 'get-distribution-configuration'
- `LW_CFG_AWS_IMAGEBUILDER_GET_IMAGE` — Results from EC2 Image Builder 'get-image'
- `LW_CFG_AWS_IMAGEBUILDER_GET_IMAGE_PIPELINE` — Results from EC2 Image Builder 'get-image-pipeline'
- `LW_CFG_AWS_IMAGEBUILDER_GET_IMAGE_POLICY` — Results from EC2 Image Builder 'get-image-policy'
- `LW_CFG_AWS_IMAGEBUILDER_GET_IMAGE_RECIPE` — Results from EC2 Image Builder 'get-image-recipe'
- `LW_CFG_AWS_IMAGEBUILDER_GET_IMAGE_RECIPE_POLICY` — Results from EC2 Image Builder 'get-image-recipe-policy'
- `LW_CFG_AWS_IMAGEBUILDER_GET_INFRASTRUCTURE_CONFIGURATION` — Results from EC2 Image Builder 'get-infrastructure-configuration'
- `LW_CFG_AWS_IMAGEBUILDER_GET_LIFECYCLE_POLICY` — Results from EC2 Image Builder 'get-lifecycle-policy'
- `LW_CFG_AWS_IMAGEBUILDER_GET_WORKFLOW` — Results from EC2 Image Builder 'get-workflow'
- `LW_CFG_AWS_IMAGEBUILDER_GET_WORKFLOW_STEP_EXECUTION` — Results from EC2 Image Builder 'get-workflow-step-execution'
- `LW_CFG_AWS_IMAGEBUILDER_IMAGES` — Results from EC2 Image Builder 'list-images'
- `LW_CFG_AWS_IMAGEBUILDER_IMAGE_BUILD_VERSIONS` — Results from EC2 Image Builder 'list-image-build-versions'
- `LW_CFG_AWS_IMAGEBUILDER_IMAGE_PACKAGES` — Results from EC2 Image Builder 'list-image-packages'
- `LW_CFG_AWS_IMAGEBUILDER_IMAGE_PIPELINES` — Results from EC2 Image Builder 'list-image-pipelines'
- `LW_CFG_AWS_IMAGEBUILDER_IMAGE_RECIPES` — Results from EC2 Image Builder 'list-image-recipes'
- `LW_CFG_AWS_IMAGEBUILDER_IMAGE_SCAN_FINDINGS` — Results from EC2 Image Builder 'list-image-scan-findings'
- `LW_CFG_AWS_IMAGEBUILDER_IMAGE_SCAN_FINDING_AGGREGATIONS` — Results from EC2 Image Builder 'list-image-scan-finding-aggregations'
- `LW_CFG_AWS_IMAGEBUILDER_INFRASTRUCTURE_CONFIGURATIONS` — Results from EC2 Image Builder 'list-infrastructure-configurations'
- `LW_CFG_AWS_IMAGEBUILDER_LIFECYCLE_EXECUTIONS` — Results from EC2 Image Builder 'list-lifecycle-executions'
- `LW_CFG_AWS_IMAGEBUILDER_LIFECYCLE_EXECUTION_RESOURCES` — Results from EC2 Image Builder 'list-lifecycle-execution-resources'
- `LW_CFG_AWS_IMAGEBUILDER_LIFECYCLE_POLICIES` — Results from EC2 Image Builder 'list-lifecycle-policies'
- `LW_CFG_AWS_IMAGEBUILDER_WORKFLOWS` — Results from EC2 Image Builder 'list-workflows'
- `LW_CFG_AWS_IMAGEBUILDER_WORKFLOW_BUILD_VERSIONS` — Results from EC2 Image Builder 'list-workflow-build-versions'
- `LW_CFG_AWS_IMAGEBUILDER_WORKFLOW_EXECUTIONS` — Results from EC2 Image Builder 'list-workflow-executions'
- `LW_CFG_AWS_IMAGEBUILDER_WORKFLOW_STEP_EXECUTIONS` — Results from EC2 Image Builder 'list-workflow-step-executions'

### ECS

- `LW_CFG_AWS_ECS_CLUSTERS` — ecs `list-clusters`
- `LW_CFG_AWS_ECS_CLUSTERS_DESCRIBE_CLUSTER` — ecs `describe-clusters`
- `LW_CFG_AWS_ECS_CONTAINER_INSTANCES` — ecs `list-container-instances`
- `LW_CFG_AWS_ECS_DESCRIBE_CONTAINER_INSTANCES` — ecs `describe-container-instances`
- `LW_CFG_AWS_ECS_DESCRIBE_SERVICES` — ecs `describe-services`
- `LW_CFG_AWS_ECS_DESCRIBE_TASKS` — ecs `describe-tasks`
- `LW_CFG_AWS_ECS_DESCRIBE_TASK_DEFINITION` — ecs `describe-task-definition`
- `LW_CFG_AWS_ECS_SERVICES` — ecs `list-services`
- `LW_CFG_AWS_ECS_TASKS` — ecs `list-tasks`
- `LW_CFG_AWS_ECS_TASK_DEFINITIONS` — ecs `list-task-definitions`
- `LW_CFG_AWS_ECS_TASK_DEFINITION_FAMILIES` — Results from Amazon EC2 Container Service 'list-task-definition-families'

### EFS

- `LW_CFG_AWS_EFS_DESCRIBE_ACCESS_POINTS` — efs `describe-file-systems`
- `LW_CFG_AWS_EFS_DESCRIBE_ACCOUNT_PREFERENCES` — efs `describe-account-preferences`
- `LW_CFG_AWS_EFS_DESCRIBE_BACKUP_POLICY` — efs `describe-backup-policy`
- `LW_CFG_AWS_EFS_DESCRIBE_FILE_SYSTEMS` — efs `describe-file-systems`
- `LW_CFG_AWS_EFS_DESCRIBE_FILE_SYSTEM_POLICY` — efs `describe-file-system-policy`
- `LW_CFG_AWS_EFS_DESCRIBE_LIFECYCLE_CONFIGURATION` — efs `describe-lifecycle-configuration`
- `LW_CFG_AWS_EFS_DESCRIBE_MOUNT_TARGETS` — efs `describe-mount-targets`
- `LW_CFG_AWS_EFS_DESCRIBE_MOUNT_TARGET_SECURITY_GROUPS` — efs `describe-mount-target-security-groups`
- `LW_CFG_AWS_EFS_DESCRIBE_REPLICATION_CONFIGURATIONS` — efs `describe-replication-configurations`

### EKS

- `LW_CFG_AWS_EKS_CLUSTERS` — eks `list-clusters`
- `LW_CFG_AWS_EKS_CLUSTERS_DESCRIBE_CLUSTER` — eks `describe-cluster`
- `LW_CFG_AWS_EKS_DESCRIBE_NODEGROUP` — eks `describe-nodegroup`
- `LW_CFG_AWS_EKS_NODEGROUPS` — eks `list-nodegroups`
- `LW_CFG_AWS_EKS_DESCRIBE_ADDON` — eks `describe-addon`
- `LW_CFG_AWS_EKS_ADDONS` — eks `list-addons`

### Elastic Beanstalk

- `LW_CFG_AWS_ELASTICBEANSTALK_APPLICATIONS` — AWS Elastic Beanstalk `describe-applications`
- `LW_CFG_AWS_ELASTICBEANSTALK_APPLICATION_VERSIONS` — AWS Elastic Beanstalk `describe-application-versions`
- `LW_CFG_AWS_ELASTICBEANSTALK_DESCRIBE_CONFIGURATION_SETTINGS` — AWS Elastic Beanstalk `describe-configuration-settings`
- `LW_CFG_AWS_ELASTICBEANSTALK_DESCRIBE_ENVIRONMENT_HEALTH` — AWS Elastic Beanstalk `describe-environment-health`
- `LW_CFG_AWS_ELASTICBEANSTALK_DESCRIBE_ENVIRONMENT_RESOURCES` — AWS Elastic Beanstalk `describe-environment-resources`
- `LW_CFG_AWS_ELASTICBEANSTALK_ENVIRONMENTS` — AWS Elastic Beanstalk `describe-environments`
- `LW_CFG_AWS_ELASTICBEANSTALK_ENVIRONMENT_MANAGED_ACTIONS` — AWS Elastic Beanstalk `describe-environment-managed-actions`
- `LW_CFG_AWS_ELASTICBEANSTALK_ENVIRONMENT_MANAGED_ACTION_HISTORY` — AWS Elastic Beanstalk `describe-environment-managed-action-history`
- `LW_CFG_AWS_ELASTICBEANSTALK_EVENTS` — AWS Elastic Beanstalk `describe-events`

### Elastic Container Registry

- `LW_CFG_AWS_ECR_GET_LIFECYCLE_POLICY` — ecr `get-lifecycle-policy`
- `LW_CFG_AWS_ECR_REPOSITORIES` — ecr `describe-repositories`
- `LW_CFG_AWS_ECR_REPOSITORIES_GET_POLICY` — ecr `get-repository-policy`

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

### IoT Events

- `LW_CFG_AWS_IOTEVENTS_ALARM_MODELS` — Results from AWS IoT Events 'list-alarm-models'
- `LW_CFG_AWS_IOTEVENTS_ALARM_MODEL_VERSIONS` — Results from AWS IoT Events 'list-alarm-model-versions'
- `LW_CFG_AWS_IOTEVENTS_DESCRIBE_ALARM_MODEL` — Results from AWS IoT Events 'describe-alarm-model'
- `LW_CFG_AWS_IOTEVENTS_DESCRIBE_DETECTOR_MODEL` — Results from AWS IoT Events 'describe-detector-model'
- `LW_CFG_AWS_IOTEVENTS_DESCRIBE_INPUT` — Results from AWS IoT Events 'describe-input'
- `LW_CFG_AWS_IOTEVENTS_DESCRIBE_LOGGING_OPTIONS` — Results from AWS IoT Events 'describe-logging-options'
- `LW_CFG_AWS_IOTEVENTS_DETECTOR_MODELS` — Results from AWS IoT Events 'list-detector-models'
- `LW_CFG_AWS_IOTEVENTS_DETECTOR_MODEL_VERSIONS` — Results from AWS IoT Events 'list-detector-model-versions'
- `LW_CFG_AWS_IOTEVENTS_INPUTS` — Results from AWS IoT Events 'list-inputs'

### IoT Greengrass V2

- `LW_CFG_AWS_GREENGRASSV2_CLIENT_DEVICES_ASSOCIATED_WITH_CORE_DEVICE` — Results from AWS IoT Greengrass V2 'list-client-devices-associated-with-core-device'
- `LW_CFG_AWS_GREENGRASSV2_COMPONENTS` — Results from AWS IoT Greengrass V2 'list-components'
- `LW_CFG_AWS_GREENGRASSV2_COMPONENT_VERSIONS` — Results from AWS IoT Greengrass V2 'list-component-versions'
- `LW_CFG_AWS_GREENGRASSV2_CORE_DEVICES` — Results from AWS IoT Greengrass V2 'list-core-devices'
- `LW_CFG_AWS_GREENGRASSV2_DEPLOYMENTS` — Results from AWS IoT Greengrass V2 'list-deployments'
- `LW_CFG_AWS_GREENGRASSV2_DESCRIBE_COMPONENT` — Results from AWS IoT Greengrass V2 'describe-component'
- `LW_CFG_AWS_GREENGRASSV2_EFFECTIVE_DEPLOYMENTS` — Results from AWS IoT Greengrass V2 'list-effective-deployments'
- `LW_CFG_AWS_GREENGRASSV2_GET_COMPONENT` — Results from AWS IoT Greengrass V2 'get-component'
- `LW_CFG_AWS_GREENGRASSV2_GET_CORE_DEVICE` — Results from AWS IoT Greengrass V2 'get-core-device'
- `LW_CFG_AWS_GREENGRASSV2_GET_DEPLOYMENT` — Results from AWS IoT Greengrass V2 'get-deployment'
- `LW_CFG_AWS_GREENGRASSV2_INSTALLED_COMPONENTS` — Results from AWS IoT Greengrass V2 'list-installed-components'

### Kinesis

- `LW_CFG_AWS_KINESIS_DESCRIBE_STREAM_SUMMARY` — kinesis `describe-stream-summary`
- `LW_CFG_AWS_KINESIS_STREAMS` — kinesis `list-streams`

### Kinesis Analytics

- `LW_CFG_AWS_KINESISANALYTICSV2_DESCRIBE_APPLICATION` — Results from Amazon Kinesis Analytics 'describe-application'
- `LW_CFG_AWS_KINESISANALYTICSV2_DESCRIBE_APPLICATION_VERSION` — Results from Amazon Kinesis Analytics 'describe-application-version'

### Kinesis Data Analytics v2

- `LW_CFG_AWS_KINESISANALYTICSV2_APPLICATIONS` — kinesisanalyticsv2 `list-applications`
- `LW_CFG_AWS_KINESISANALYTICSV2_APPLICATION` — kinesisanalyticsv2 `describe-application`
- `LW_CFG_AWS_KINESISANALYTICSV2_APPLICATION_VERSION` — kinesisanalyticsv2 `describe-application-version`
- `LW_CFG_AWS_KINESISANALYTICSV2_APPLICATION_SNAPSHOTS` — kinesisanalyticsv2 `list-application-snapshots`
- `LW_CFG_AWS_KINESISANALYTICSV2_APPLICATION_VERSIONS` — kinesisanalyticsv2 `list-application-versions`

### Kinesis Data Firehose

- `LW_CFG_AWS_FIREHOSE_DELIVERY_STREAMS` — firehose `list-delivery-streams`
- `LW_CFG_AWS_FIREHOSE_DESCRIBE_DELIVERY_STREAM` — firehose `describe-delivery-stream`

### Kinesis Video Streams

- `LW_CFG_AWS_KINESISVIDEO_DESCRIBE_EDGE_CONFIGURATION` — Results from Amazon Kinesis Video Streams 'describe-edge-configuration'
- `LW_CFG_AWS_KINESISVIDEO_DESCRIBE_IMAGE_GENERATION_CONFIGURATION` — Results from Amazon Kinesis Video Streams 'describe-image-generation-configuration'
- `LW_CFG_AWS_KINESISVIDEO_DESCRIBE_MEDIA_STORAGE_CONFIGURATION` — Results from Amazon Kinesis Video Streams 'describe-media-storage-configuration'
- `LW_CFG_AWS_KINESISVIDEO_DESCRIBE_NOTIFICATION_CONFIGURATION` — Results from Amazon Kinesis Video Streams 'describe-notification-configuration'
- `LW_CFG_AWS_KINESISVIDEO_GET_DATA_ENDPOINT` — Results from Amazon Kinesis Video Streams 'get-data-endpoint'
- `LW_CFG_AWS_KINESISVIDEO_MAPPED_RESOURCE_CONFIGURATION` — Results from Amazon Kinesis Video Streams 'describe-mapped-resource-configuration'
- `LW_CFG_AWS_KINESISVIDEO_SIGNALING_CHANNELS` — Results from Amazon Kinesis Video Streams 'list-signaling-channels'
- `LW_CFG_AWS_KINESISVIDEO_STREAMS` — Results from Amazon Kinesis Video Streams 'list-streams'

### KMS

- `LW_CFG_AWS_KMS_ALIASES` — kms `list-aliases`
- `LW_CFG_AWS_KMS_KEYS` — kms `list-keys`
- `LW_CFG_AWS_KMS_KEYS_DESCRIBE_KEY` — kms `describe-key`
- `LW_CFG_AWS_KMS_KEYS_GET_POLICY` — kms `get-key-policy`
- `LW_CFG_AWS_KMS_KEYS_GET_ROTATION_STATUS` — kms `get-key-rotation-status`
- `LW_CFG_AWS_KMS_GRANTS` — Results from AWS Key Management Service 'list-grants'

### Lake Formation

- `LW_CFG_AWS_LAKEFORMATION_DATA_CELLS_FILTER` — Results from AWS Lake Formation 'list-data-cells-filter'
- `LW_CFG_AWS_LAKEFORMATION_DESCRIBE_LAKE_FORMATION_IDENTITY_CENTER_CONFIGURATION` — Results from AWS Lake Formation 'describe-lake-formation-identity-center-configuration'
- `LW_CFG_AWS_LAKEFORMATION_GET_DATA_LAKE_PRINCIPAL` — Results from AWS Lake Formation 'get-data-lake-principal'
- `LW_CFG_AWS_LAKEFORMATION_GET_DATA_LAKE_SETTINGS` — Results from AWS Lake Formation 'get-data-lake-settings'
- `LW_CFG_AWS_LAKEFORMATION_GET_EFFECTIVE_PERMISSIONS_FOR_PATH` — Results from AWS Lake Formation 'get-effective-permissions-for-path'
- `LW_CFG_AWS_LAKEFORMATION_GET_TABLE_OBJECTS` — Results from AWS Lake Formation 'get-table-objects'
- `LW_CFG_AWS_LAKEFORMATION_PERMISSIONS` — Results from AWS Lake Formation 'list-permissions'
- `LW_CFG_AWS_LAKEFORMATION_RESOURCES` — Results from AWS Lake Formation 'list-resources'
- `LW_CFG_AWS_LAKEFORMATION_TABLE_STORAGE_OPTIMIZERS` — Results from AWS Lake Formation 'list-table-storage-optimizers'

### Lambda

- `LW_CFG_AWS_LAMBDA_GET_FUNCTION_CODE_SIGNING_CONFIG` — lambda `get-function-code-signing-config`
- `LW_CFG_AWS_LAMBDA_GET_POLICY` — lambda `get-policy`
- `LW_CFG_AWS_LAMBDA_FUNCTION_URL_CONFIGS` — lambda `list-function-url-configs`
- `LW_CFG_AWS_LAMBDA` — lambda `list-functions`
- `LW_CFG_AWS_LAMBDA_PROVISIONED_CONCURRENCY_CONFIGS` — lambda `list-provisioned-concurrency-configs`

### Logs

- `LW_CFG_AWS_LOGS` — logs `describe-log-groups`
- `LW_CFG_AWS_LOGS_DESCRIBE_METRIC_FILTERS` — logs `describe-metric-filters`

### MediaTailor

- `LW_CFG_AWS_MEDIATAILOR_ALERTS` — Results from AWS MediaTailor 'list-alerts'
- `LW_CFG_AWS_MEDIATAILOR_CHANNELS` — Results from AWS MediaTailor 'list-channels'
- `LW_CFG_AWS_MEDIATAILOR_DESCRIBE_CHANNEL` — Results from AWS MediaTailor 'describe-channel'
- `LW_CFG_AWS_MEDIATAILOR_DESCRIBE_LIVE_SOURCE` — Results from AWS MediaTailor 'describe-live-source'
- `LW_CFG_AWS_MEDIATAILOR_DESCRIBE_PROGRAM` — Results from AWS MediaTailor 'describe-program'
- `LW_CFG_AWS_MEDIATAILOR_DESCRIBE_SOURCE_LOCATION` — Results from AWS MediaTailor 'describe-source-location'
- `LW_CFG_AWS_MEDIATAILOR_DESCRIBE_VOD_SOURCE` — Results from AWS MediaTailor 'describe-vod-source'
- `LW_CFG_AWS_MEDIATAILOR_GET_CHANNEL_POLICY` — Results from AWS MediaTailor 'get-channel-policy'
- `LW_CFG_AWS_MEDIATAILOR_GET_CHANNEL_SCHEDULE` — Results from AWS MediaTailor 'get-channel-schedule'
- `LW_CFG_AWS_MEDIATAILOR_GET_PLAYBACK_CONFIGURATION` — Results from AWS MediaTailor 'get-playback-configuration'
- `LW_CFG_AWS_MEDIATAILOR_GET_PREFETCH_SCHEDULE` — Results from AWS MediaTailor 'get-prefetch-schedule'
- `LW_CFG_AWS_MEDIATAILOR_LIVE_SOURCES` — Results from AWS MediaTailor 'list-live-sources'
- `LW_CFG_AWS_MEDIATAILOR_PLAYBACK_CONFIGURATIONS` — Results from AWS MediaTailor 'list-playback-configurations'
- `LW_CFG_AWS_MEDIATAILOR_PREFETCH_SCHEDULES` — Results from AWS MediaTailor 'list-prefetch-schedules'
- `LW_CFG_AWS_MEDIATAILOR_SOURCE_LOCATIONS` — Results from AWS MediaTailor 'list-source-locations'
- `LW_CFG_AWS_MEDIATAILOR_VOD_SOURCES` — Results from AWS MediaTailor 'list-vod-sources'

### MemoryDB

- `LW_CFG_AWS_MEMORYDB_ACLS` — Results from Amazon MemoryDB 'describe-acls'
- `LW_CFG_AWS_MEMORYDB_CLUSTERS` — Results from Amazon MemoryDB 'describe-clusters'
- `LW_CFG_AWS_MEMORYDB_ENGINE_VERSIONS` — Results from Amazon MemoryDB 'describe-engine-versions'
- `LW_CFG_AWS_MEMORYDB_LIST_ALLOWED_MULTI_REGION_CLUSTER_UPDATES` — Results from Amazon MemoryDB 'list-allowed-multi-region-cluster-updates'
- `LW_CFG_AWS_MEMORYDB_LIST_ALLOWED_NODE_TYPE_UPDATES` — Results from Amazon MemoryDB 'list-allowed-node-type-updates'
- `LW_CFG_AWS_MEMORYDB_MULTI_REGION_CLUSTERS` — Results from Amazon MemoryDB 'describe-multi-region-clusters'
- `LW_CFG_AWS_MEMORYDB_PARAMETERS` — Results from Amazon MemoryDB 'describe-parameters'
- `LW_CFG_AWS_MEMORYDB_PARAMETER_GROUPS` — Results from Amazon MemoryDB 'describe-parameter-groups'
- `LW_CFG_AWS_MEMORYDB_RESERVED_NODES` — Results from Amazon MemoryDB 'describe-reserved-nodes'
- `LW_CFG_AWS_MEMORYDB_RESERVED_NODES_OFFERINGS` — Results from Amazon MemoryDB 'describe-reserved-nodes-offerings'
- `LW_CFG_AWS_MEMORYDB_SERVICE_UPDATES` — Results from Amazon MemoryDB 'describe-service-updates'
- `LW_CFG_AWS_MEMORYDB_SNAPSHOTS` — Results from Amazon MemoryDB 'describe-snapshots'
- `LW_CFG_AWS_MEMORYDB_SUBNET_GROUPS` — Results from Amazon MemoryDB 'describe-subnet-groups'
- `LW_CFG_AWS_MEMORYDB_USERS` — Results from Amazon MemoryDB 'describe-users'

### MQ

- `LW_CFG_AWS_MQ_BROKERS` — MQ `list-brokers`
- `LW_CFG_AWS_MQ_BROKER` — MQ `describer-broker`
- `LW_CFG_AWS_MQ_USERS` — MQ `describe-user`
- `LW_CFG_AWS_MQ_BROKER_ENGINE_TYPES` — MQ `describe-broker-engine-types`
- `LW_CFG_AWS_MQ_BROKER_INSTANCE_OPTIONS` — MQ `describe-broker-instance-options`
- `LW_CFG_AWS_MQ_CONFIGURATIONS` — MQ `list-configurations`
- `LW_CFG_AWS_MQ_CONFIGURATION_REVISIONS` — MQ `list-configuration-revisions`
- `LW_CFG_AWS_MQ_CONFIGURATION_REVISION` — MQ `describe-configuration-revision`
- `LW_CFG_AWS_MQ_DESCRIBE_BROKER` — Results from AmazonMQ 'describe-broker'
- `LW_CFG_AWS_MQ_DESCRIBE_CONFIGURATION_REVISION` — Results from AmazonMQ 'describe-configuration-revision'
- `LW_CFG_AWS_MQ_DESCRIBE_USER` — Results from AmazonMQ 'describe-user'

### MSK (Managed Streaming for Apache Kafka)

- `LW_CFG_AWS_KAFKA_CLUSTERS_V2` — kafka `list-clusters-v2`
- `LW_CFG_AWS_KAFKA_GET_BOOTSTRAP_BROKERS` — kafka `get-bootstrap-brokers`
- `LW_CFG_AWS_KAFKA_GET_COMPATIBLE_KAFKA_VERSIONS` — kafka `get-compatible-kafka-versions`
- `LW_CFG_AWS_KAFKA_CLUSTER_OPERATIONS` — kafka `list-cluster-operations`
- `LW_CFG_AWS_KAFKA_NODES` — kafka `list-nodes`
- `LW_CFG_AWS_KAFKA_SCRAM_SECRETS` — kafka `list-scram-secrets`
- `LW_CFG_AWS_KAFKA_CONFIGURATIONS` — kafka `list-configurations`
- `LW_CFG_AWS_KAFKA_CONFIGURATION` — kafka `describe-configuration`
- `LW_CFG_AWS_KAFKA_CONFIGURATION_REVISIONS` — kafka `list-configuration-revisions`
- `LW_CFG_AWS_KAFKA_CONFIGURATION_REVISION` — kafka `describe-configuration-revision`
- `LW_CFG_AWS_KAFKA_KAFKA_VERSIONS` — kafka `list-kafka-versions`
- `LW_CFG_AWS_KAFKA_DESCRIBE_CONFIGURATION_REVISION` — Results from Managed Streaming for Kafka 'describe-configuration-revision'

### Neptune

- `LW_CFG_AWS_NEPTUNE_DB_CLUSTERS` — Amazon Neptune `describe-db-clusters`
- `LW_CFG_AWS_NEPTUNE_DB_CLUSTER_ENDPOINTS` — Amazon Neptune `describe-db-cluster-endpoints`
- `LW_CFG_AWS_NEPTUNE_DB_CLUSTER_PARAMETER_GROUPS` — Amazon Neptune `describe-db-cluster-parameter-groups`
- `LW_CFG_AWS_NEPTUNE_DB_CLUSTER_SNAPSHOTS` — Amazon Neptune `describe-db-cluster-snapshots`
- `LW_CFG_AWS_NEPTUNE_DB_INSTANCES` — Amazon Neptune `describe-db-instances`
- `LW_CFG_AWS_NEPTUNE_DB_PARAMETER_GROUPS` — Amazon Neptune `describe-db-parameter-groups`
- `LW_CFG_AWS_NEPTUNE_DB_SUBNET_GROUPS` — Amazon Neptune `describe-db-subnet-groups`
- `LW_CFG_AWS_NEPTUNE_DESCRIBE_DB_CLUSTER_SNAPSHOT_ATTRIBUTES` — Amazon Neptune `describe-db-cluster-snapshot-attributes`
- `LW_CFG_AWS_NEPTUNE_DESCRIBE_VALID_DB_INSTANCE_MODIFICATIONS` — Amazon Neptune `describe-valid-db-instance-modifications`
- `LW_CFG_AWS_NEPTUNE_ENGINE_DEFAULT_CLUSTER_PARAMETERS` — Amazon Neptune `describe-engine-default-cluster-parameters`
- `LW_CFG_AWS_NEPTUNE_ENGINE_DEFAULT_PARAMETERS` — Amazon Neptune `describe-engine-default-parameters`
- `LW_CFG_AWS_NEPTUNE_EVENT_CATEGORIES` — Amazon Neptune `describe-event-categories`
- `LW_CFG_AWS_NEPTUNE_EVENT_SUBSCRIPTIONS` — Amazon Neptune `describe-event-subscriptions`
- `LW_CFG_AWS_NEPTUNE_GLOBAL_CLUSTERS` — Amazon Neptune `describe-global-clusters`

### Network Firewall

- `LW_CFG_AWS_NETWORK_FIREWALL_DESCRIBE_FIREWALL` — AWS Network Firewall `describe-firewall`
- `LW_CFG_AWS_NETWORK_FIREWALL_DESCRIBE_FIREWALL_POLICY` — AWS Network Firewall `describe-firewall-policy`
- `LW_CFG_AWS_NETWORK_FIREWALL_DESCRIBE_LOGGING_CONFIGURATION` — AWS Network Firewall `describe-logging-configuration`
- `LW_CFG_AWS_NETWORK_FIREWALL_DESCRIBE_RULE_GROUP` — AWS Network Firewall `describe-rule-group`
- `LW_CFG_AWS_NETWORK_FIREWALL_FIREWALLS` — AWS Network Firewall `list-firewalls`
- `LW_CFG_AWS_NETWORK_FIREWALL_FIREWALL_POLICIES` — AWS Network Firewall `list-firewall-policies`
- `LW_CFG_AWS_NETWORK_FIREWALL_RULE_GROUPS` — AWS Network Firewall `list-rule-groups`

### Opensearch

- `LW_CFG_AWS_OPENSEARCH` — opensearch `list-domain-names`
- `LW_CFG_AWS_OPENSEARCH_DESCRIBE_DOMAIN` — opensearch `describe-domain`

### Organizations

- `LW_CFG_AWS_ORGANIZATIONS_ACCOUNTS` — Results from AWS Organizations 'list-accounts'
- `LW_CFG_AWS_ORGANIZATIONS_ACCOUNTS_FOR_PARENT` — Results from AWS Organizations 'list-accounts-for-parent'
- `LW_CFG_AWS_ORGANIZATIONS_AWS_SERVICE_ACCESS_FOR_ORGANIZATION` — Results from AWS Organizations 'list-aws-service-access-for-organization'
- `LW_CFG_AWS_ORGANIZATIONS_DELEGATED_ADMINISTRATORS` — Results from AWS Organizations 'list-delegated-administrators'
- `LW_CFG_AWS_ORGANIZATIONS_DELEGATED_SERVICES_FOR_ACCOUNT` — Results from AWS Organizations 'list-delegated-services-for-account'
- `LW_CFG_AWS_ORGANIZATIONS_DESCRIBE_ACCOUNT` — Results from AWS Organizations 'describe-account'
- `LW_CFG_AWS_ORGANIZATIONS_DESCRIBE_EFFECTIVE_POLICY` — Results from AWS Organizations 'describe-effective-policy'
- `LW_CFG_AWS_ORGANIZATIONS_DESCRIBE_ORGANIZATION` — Results from AWS Organizations 'describe-organization'
- `LW_CFG_AWS_ORGANIZATIONS_DESCRIBE_ORGANIZATIONAL_UNIT` — Results from AWS Organizations 'describe-organizational-unit'
- `LW_CFG_AWS_ORGANIZATIONS_DESCRIBE_POLICY` — Results from AWS Organizations 'describe-policy'
- `LW_CFG_AWS_ORGANIZATIONS_DESCRIBE_RESOURCE_POLICY` — Results from AWS Organizations 'describe-resource-policy'
- `LW_CFG_AWS_ORGANIZATIONS_ORGANIZATIONAL_UNITS_FOR_PARENT` — Results from AWS Organizations 'list-organizational-units-for-parent'
- `LW_CFG_AWS_ORGANIZATIONS_POLICIES` — Results from AWS Organizations 'list-policies'
- `LW_CFG_AWS_ORGANIZATIONS_ROOTS` — Results from AWS Organizations 'list-roots'
- `LW_CFG_AWS_ORGANIZATIONS_TARGETS_FOR_POLICY` — Results from AWS Organizations 'list-targets-for-policy'
- `LW_CFG_AWS_ORGANIZATION_DETAILS_DESCRIBE_ORGANIZATION` — Results from AWS Organizations 'describe-organization'

### Personalize

- `LW_CFG_AWS_PERSONALIZE_BATCH_INFERENCE_JOBS` — Results from Amazon Personalize 'list-batch-inference-jobs'
- `LW_CFG_AWS_PERSONALIZE_BATCH_SEGMENT_JOBS` — Results from Amazon Personalize 'list-batch-segment-jobs'
- `LW_CFG_AWS_PERSONALIZE_CAMPAIGNS` — Results from Amazon Personalize 'list-campaigns'
- `LW_CFG_AWS_PERSONALIZE_DATASETS` — Results from Amazon Personalize 'list-datasets'
- `LW_CFG_AWS_PERSONALIZE_DATASET_EXPORT_JOBS` — Results from Amazon Personalize 'list-dataset-export-jobs'
- `LW_CFG_AWS_PERSONALIZE_DATASET_GROUPS` — Results from Amazon Personalize 'list-dataset-groups'
- `LW_CFG_AWS_PERSONALIZE_DATASET_IMPORT_JOBS` — Results from Amazon Personalize 'list-dataset-import-jobs'
- `LW_CFG_AWS_PERSONALIZE_DATA_DELETION_JOBS` — Results from Amazon Personalize 'list-data-deletion-jobs'
- `LW_CFG_AWS_PERSONALIZE_DESCRIBE_BATCH_INFERENCE_JOB` — Results from Amazon Personalize 'describe-batch-inference-job'
- `LW_CFG_AWS_PERSONALIZE_DESCRIBE_BATCH_SEGMENT_JOB` — Results from Amazon Personalize 'describe-batch-segment-job'
- `LW_CFG_AWS_PERSONALIZE_DESCRIBE_CAMPAIGN` — Results from Amazon Personalize 'describe-campaign'
- `LW_CFG_AWS_PERSONALIZE_DESCRIBE_DATASET` — Results from Amazon Personalize 'describe-dataset'
- `LW_CFG_AWS_PERSONALIZE_DESCRIBE_DATASET_EXPORT_JOB` — Results from Amazon Personalize 'describe-dataset-export-job'
- `LW_CFG_AWS_PERSONALIZE_DESCRIBE_DATASET_GROUP` — Results from Amazon Personalize 'describe-dataset-group'
- `LW_CFG_AWS_PERSONALIZE_DESCRIBE_DATASET_IMPORT_JOB` — Results from Amazon Personalize 'describe-dataset-import-job'
- `LW_CFG_AWS_PERSONALIZE_DESCRIBE_DATA_DELETION_JOB` — Results from Amazon Personalize 'describe-data-deletion-job'
- `LW_CFG_AWS_PERSONALIZE_DESCRIBE_EVENT_TRACKER` — Results from Amazon Personalize 'describe-event-tracker'
- `LW_CFG_AWS_PERSONALIZE_DESCRIBE_FILTER` — Results from Amazon Personalize 'describe-filter'
- `LW_CFG_AWS_PERSONALIZE_DESCRIBE_METRIC_ATTRIBUTION` — Results from Amazon Personalize 'describe-metric-attribution'
- `LW_CFG_AWS_PERSONALIZE_DESCRIBE_RECIPE` — Results from Amazon Personalize 'describe-recipe'
- `LW_CFG_AWS_PERSONALIZE_DESCRIBE_RECOMMENDER` — Results from Amazon Personalize 'describe-recommender'
- `LW_CFG_AWS_PERSONALIZE_DESCRIBE_SCHEMA` — Results from Amazon Personalize 'describe-schema'
- `LW_CFG_AWS_PERSONALIZE_DESCRIBE_SOLUTION` — Results from Amazon Personalize 'describe-solution'
- `LW_CFG_AWS_PERSONALIZE_DESCRIBE_SOLUTION_VERSION` — Results from Amazon Personalize 'describe-solution-version'
- `LW_CFG_AWS_PERSONALIZE_EVENT_TRACKERS` — Results from Amazon Personalize 'list-event-trackers'
- `LW_CFG_AWS_PERSONALIZE_FILTERS` — Results from Amazon Personalize 'list-filters'
- `LW_CFG_AWS_PERSONALIZE_GET_SOLUTION_METRICS` — Results from Amazon Personalize 'get-solution-metrics'
- `LW_CFG_AWS_PERSONALIZE_METRIC_ATTRIBUTIONS` — Results from Amazon Personalize 'list-metric-attributions'
- `LW_CFG_AWS_PERSONALIZE_METRIC_ATTRIBUTION_METRICS` — Results from Amazon Personalize 'list-metric-attribution-metrics'
- `LW_CFG_AWS_PERSONALIZE_RECIPES` — Results from Amazon Personalize 'list-recipes'
- `LW_CFG_AWS_PERSONALIZE_RECOMMENDERS` — Results from Amazon Personalize 'list-recommenders'
- `LW_CFG_AWS_PERSONALIZE_SCHEMAS` — Results from Amazon Personalize 'list-schemas'
- `LW_CFG_AWS_PERSONALIZE_SOLUTIONS` — Results from Amazon Personalize 'list-solutions'
- `LW_CFG_AWS_PERSONALIZE_SOLUTION_VERSIONS` — Results from Amazon Personalize 'list-solution-versions'

### Q in Connect

- `LW_CFG_AWS_QCONNECT_AI_AGENTS` — qconnect `list-ai-agents`
- `LW_CFG_AWS_QCONNECT_AI_AGENT_VERSIONS` — qconnect `list-ai-agent-versions`
- `LW_CFG_AWS_QCONNECT_AI_GUARDRAILS` — qconnect `list-ai-guardrails`
- `LW_CFG_AWS_QCONNECT_AI_GUARDRAIL_VERSIONS` — qconnect `list-ai-guardrail-versions`
- `LW_CFG_AWS_QCONNECT_AI_PROMPTS` — qconnect `list-ai-prompts`
- `LW_CFG_AWS_QCONNECT_AI_PROMPT_VERSIONS` — qconnect `list-ai-prompt-versions`
- `LW_CFG_AWS_QCONNECT_ASSISTANTS` — qconnect `list-assistants`
- `LW_CFG_AWS_QCONNECT_ASSISTANT_ASSOCIATIONS` — qconnect `list-assistant-associations`
- `LW_CFG_AWS_QCONNECT_CONTENTS` — qconnect `list-contents`
- `LW_CFG_AWS_QCONNECT_CONTENT_ASSOCIATIONS` — qconnect `list-content-associations`
- `LW_CFG_AWS_QCONNECT_GET_AI_AGENT` — qconnect `get-ai-agent`
- `LW_CFG_AWS_QCONNECT_GET_AI_GUARDRAIL` — qconnect `get-ai-guardrail`
- `LW_CFG_AWS_QCONNECT_GET_AI_PROMPT` — qconnect `get-ai-prompt`
- `LW_CFG_AWS_QCONNECT_GET_CONTENT` — qconnect `get-content`
- `LW_CFG_AWS_QCONNECT_GET_IMPORT_JOB` — qconnect `get-import-job`
- `LW_CFG_AWS_QCONNECT_GET_KNOWLEDGE_BASE` — qconnect `get-knowledge-base`
- `LW_CFG_AWS_QCONNECT_GET_MESSAGE_TEMPLATE` — qconnect `get-message-template`
- `LW_CFG_AWS_QCONNECT_GET_QUICK_RESPONSE` — qconnect `get-quick-response`
- `LW_CFG_AWS_QCONNECT_IMPORT_JOBS` — qconnect `list-import-jobs`
- `LW_CFG_AWS_QCONNECT_KNOWLEDGE_BASES` — qconnect `list-knowledge-bases`
- `LW_CFG_AWS_QCONNECT_MESSAGE_TEMPLATES` — qconnect `list-message-templates`
- `LW_CFG_AWS_QCONNECT_MESSAGE_TEMPLATE_VERSIONS` — qconnect `list-message-template-versions`
- `LW_CFG_AWS_QCONNECT_QUICK_RESPONSES` — qconnect `list-quick-responses`

### QBusiness

- `LW_CFG_AWS_QBUSINESS_APPLICATIONS` — Results from QBusiness 'list-applications'
- `LW_CFG_AWS_QBUSINESS_DATA_ACCESSORS` — Results from QBusiness 'list-data-accessors'
- `LW_CFG_AWS_QBUSINESS_DATA_SOURCES` — Results from QBusiness 'list-data-sources'
- `LW_CFG_AWS_QBUSINESS_DATA_SOURCE_SYNC_JOBS` — Results from QBusiness 'list-data-source-sync-jobs'
- `LW_CFG_AWS_QBUSINESS_DOCUMENTS` — Results from QBusiness 'list-documents'
- `LW_CFG_AWS_QBUSINESS_GET_APPLICATION` — Results from QBusiness 'get-application'
- `LW_CFG_AWS_QBUSINESS_GET_CHAT_CONTROLS_CONFIGURATION` — Results from QBusiness 'get-chat-controls-configuration'
- `LW_CFG_AWS_QBUSINESS_GET_DATA_ACCESSOR` — Results from QBusiness 'get-data-accessor'
- `LW_CFG_AWS_QBUSINESS_GET_DATA_SOURCE` — Results from QBusiness 'get-data-source'
- `LW_CFG_AWS_QBUSINESS_GET_INDEX` — Results from QBusiness 'get-index'
- `LW_CFG_AWS_QBUSINESS_GET_PLUGIN` — Results from QBusiness 'get-plugin'
- `LW_CFG_AWS_QBUSINESS_GET_POLICY` — Results from QBusiness 'get-policy'
- `LW_CFG_AWS_QBUSINESS_GET_RETRIEVER` — Results from QBusiness 'get-retriever'
- `LW_CFG_AWS_QBUSINESS_GET_WEB_EXPERIENCE` — Results from QBusiness 'get-web-experience'
- `LW_CFG_AWS_QBUSINESS_INDICES` — Results from QBusiness 'list-indices'
- `LW_CFG_AWS_QBUSINESS_PLUGINS` — Results from QBusiness 'list-plugins'
- `LW_CFG_AWS_QBUSINESS_PLUGIN_ACTIONS` — Results from QBusiness 'list-plugin-actions'
- `LW_CFG_AWS_QBUSINESS_PLUGIN_TYPE_ACTIONS` — Results from QBusiness 'list-plugin-type-actions'
- `LW_CFG_AWS_QBUSINESS_PLUGIN_TYPE_METADATA` — Results from QBusiness 'list-plugin-type-metadata'
- `LW_CFG_AWS_QBUSINESS_RETRIEVERS` — Results from QBusiness 'list-retrievers'
- `LW_CFG_AWS_QBUSINESS_WEB_EXPERIENCES` — Results from QBusiness 'list-web-experiences'

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

### Service Catalog AppRegistry

- `LW_CFG_AWS_SERVICECATALOG_APPREGISTRY_APPLICATIONS` — servicecatalog-appregistry `list-applications`
- `LW_CFG_AWS_SERVICECATALOG_APPREGISTRY_ASSOCIATED_ATTRIBUTE_GROUPS` — servicecatalog-appregistry `list-associated-attribute-groups`
- `LW_CFG_AWS_SERVICECATALOG_APPREGISTRY_ASSOCIATED_RESOURCES` — servicecatalog-appregistry `list-associated-resources`
- `LW_CFG_AWS_SERVICECATALOG_APPREGISTRY_ATTRIBUTE_GROUPS` — servicecatalog-appregistry `list-attribute-groups`
- `LW_CFG_AWS_SERVICECATALOG_APPREGISTRY_ATTRIBUTE_GROUPS_FOR_APPLICATION` — servicecatalog-appregistry `list-attribute-groups-for-application`
- `LW_CFG_AWS_SERVICECATALOG_APPREGISTRY_GET_APPLICATION` — servicecatalog-appregistry `get-application`
- `LW_CFG_AWS_SERVICECATALOG_APPREGISTRY_GET_ASSOCIATED_RESOURCE` — servicecatalog-appregistry `get-associated-resource`
- `LW_CFG_AWS_SERVICECATALOG_APPREGISTRY_GET_ATTRIBUTE_GROUP` — servicecatalog-appregistry `get-attribute-group`

### Simple Email Service version 1 and 2

- `LW_CFG_AWS_SES_ACTIVE_RECEIPT_RULE_SET` — SES `describe-active-receipt-rule-set`
- `LW_CFG_AWS_SES_RECEIPT_FILTERS` — SES `list-receipt-filters`
- `LW_CFG_AWS_SES_RECEIPT_RULE_SETS` — SES `list-receipt-rule-sets`
- `LW_CFG_AWS_SESV2_CONFIGURATION_SETS` — SESv2 `list-configuration-sets`
- `LW_CFG_AWS_SESV2_CONTACTS` — Results from Amazon Simple Email Service 'list-contacts'
- `LW_CFG_AWS_SESV2_CONTACT_LISTS` — Results from Amazon Simple Email Service 'list-contact-lists'
- `LW_CFG_AWS_SESV2_CUSTOM_VERIFICATION_EMAIL_TEMPLATES` — Results from Amazon Simple Email Service 'list-custom-verification-email-templates'
- `LW_CFG_AWS_SESV2_DEDICATED_IP_POOLS` — SESv2 `list-dedicated-ip-pools`
- `LW_CFG_AWS_SESV2_EMAIL_IDENTITIES` — Results from Amazon Simple Email Service 'list-email-identities'
- `LW_CFG_AWS_SESV2_EMAIL_TEMPLATES` — Results from Amazon Simple Email Service 'list-email-templates'
- `LW_CFG_AWS_SESV2_EXPORT_JOBS` — Results from Amazon Simple Email Service 'list-export-jobs'
- `LW_CFG_AWS_SESV2_GET_CONTACT` — Results from Amazon Simple Email Service 'get-contact'
- `LW_CFG_AWS_SESV2_GET_CONFIGURATION_SET` — SESv2 `get-configuration-set`
- `LW_CFG_AWS_SESV2_GET_CONFIGURATION_SET_EVENT_DESTINATIONS` — SESv2 `get-configuration-set-event-destinations`
- `LW_CFG_AWS_SESV2_GET_CONTACT_LIST` — Results from Amazon Simple Email Service 'get-contact-list'
- `LW_CFG_AWS_SESV2_GET_CUSTOM_VERIFICATION_EMAIL_TEMPLATE` — Results from Amazon Simple Email Service 'get-custom-verification-email-template'
- `LW_CFG_AWS_SESV2_GET_EMAIL_IDENTITY` — Results from Amazon Simple Email Service 'get-email-identity'
- `LW_CFG_AWS_SESV2_GET_EMAIL_IDENTITY_POLICIES` — Results from Amazon Simple Email Service 'get-email-identity-policies'
- `LW_CFG_AWS_SESV2_GET_EMAIL_TEMPLATE` — Results from Amazon Simple Email Service 'get-email-template'
- `LW_CFG_AWS_SESV2_GET_EXPORT_JOB` — Results from Amazon Simple Email Service 'get-export-job'
- `LW_CFG_AWS_SESV2_GET_IMPORT_JOB` — Results from Amazon Simple Email Service 'get-import-job'
- `LW_CFG_AWS_SESV2_GET_MULTI_REGION_ENDPOINT` — Results from Amazon Simple Email Service 'get-multi-region-endpoint'
- `LW_CFG_AWS_SESV2_GET_SUPPRESSED_DESTINATION` — Results from Amazon Simple Email Service 'get-suppressed-destination'
- `LW_CFG_AWS_SESV2_IMPORT_JOBS` — Results from Amazon Simple Email Service 'list-import-jobs'
- `LW_CFG_AWS_SESV2_MULTI_REGION_ENDPOINTS` — Results from Amazon Simple Email Service 'list-multi-region-endpoints'
- `LW_CFG_AWS_SESV2_RECOMMENDATIONS` — Results from Amazon Simple Email Service 'list-recommendations'
- `LW_CFG_AWS_SESV2_SUPPRESSED_DESTINATIONS` — Results from Amazon Simple Email Service 'list-suppressed-destinations'

### SNS

- `LW_CFG_AWS_SNS_GET_DATA_PROTECTION_POLICY` — Amazon Simple Notification Service `get-data-protection-policy`
- `LW_CFG_AWS_SNS_GET_SUBSCRIPTION_ATTRIBUTES` — Amazon Simple Notification Service `get-subscription-attributes`
- `LW_CFG_AWS_SNS_GET_TOPIC_ATTRIBUTES` — Amazon Simple Notification Service `get-topic-attributes`
- `LW_CFG_AWS_SNS_PLATFORM_APPLICATIONS` — Amazon Simple Notification Service `list-platform-applications`
- `LW_CFG_AWS_SNS_SUBSCRIPTIONS` — Amazon Simple Notification Service `list-subscriptions`
- `LW_CFG_AWS_SNS_TOPICS` — Amazon Simple Notification Service `list-topics`

### SQS

- `LW_CFG_AWS_SQS_QUEUES` — sqs `list-queues`
- `LW_CFG_AWS_SQS_QUEUE_ATTRIBUTES` — sqs `get-queue-attributes`

### SSM

- `LW_CFG_AWS_SSM_DESCRIBE_DOCUMENT` — Amazon Simple Systems Manager (SSM) `describe-document`
- `LW_CFG_AWS_SSM_DESCRIBE_DOCUMENT_PERMISSION` — Amazon Simple Systems Manager (SSM) `describe-document-permission`
- `LW_CFG_AWS_SSM_DOCUMENTS` — Amazon Simple Systems Manager (SSM) `list-documents`
- `LW_CFG_AWS_SSM_INSTANCE_ASSOCIATIONS_STATUS` — Amazon Simple Systems Manager (SSM) `describe-instance-associations-status`
- `LW_CFG_AWS_SSM_INSTANCE_INFORMATION` — Amazon Simple Systems Manager (SSM) `describe-instance-information`
- `LW_CFG_AWS_SSM_INSTANCE_PATCHES` — Amazon Simple Systems Manager (SSM) `describe-instance-patches`
- `LW_CFG_AWS_SSM_PARAMETERS` — Amazon Simple Systems Manager (SSM) `describe-parameters`
- `LW_CFG_AWS_SSM_GET_CONNECTION_STATUS` — Amazon Simple Systems Manager (SSM) `get-connection-status`
- `LW_CFG_AWS_SSM_SESSIONS` — Amazon Simple Systems Manager (SSM) `describe-sessions`

### SSO

- `LW_CFG_AWS_SSO_ADMIN_ACCOUNTS_FOR_PROVISIONED_PERMISSION_SET` — AWS Single Sign-On Admin `list-accounts-for-provisioned-permission-set`
- `LW_CFG_AWS_SSO_ADMIN_ACCOUNT_ASSIGNMENTS` — AWS Single Sign-On Admin `list-account-assignments`
- `LW_CFG_AWS_SSO_ADMIN_ACCOUNT_ASSIGNMENT_CREATION_STATUS` — AWS Single Sign-On Admin `list-account-assignment-creation-status`
- `LW_CFG_AWS_SSO_ADMIN_ACCOUNT_ASSIGNMENT_DELETION_STATUS` — AWS Single Sign-On Admin `list-account-assignment-deletion-status`
- `LW_CFG_AWS_SSO_ADMIN_CUSTOMER_MANAGED_POLICY_REFERENCES_IN_PERMISSION_SET` — AWS Single Sign-On Admin `list-customer-managed-policy-references-in-permission-set`
- `LW_CFG_AWS_SSO_ADMIN_DESCRIBE_ACCOUNT_ASSIGNMENT_CREATION_STATUS` — AWS Single Sign-On Admin `describe-account-assignment-creation-status`
- `LW_CFG_AWS_SSO_ADMIN_DESCRIBE_ACCOUNT_ASSIGNMENT_DELETION_STATUS` — AWS Single Sign-On Admin `describe-account-assignment-deletion-status`
- `LW_CFG_AWS_SSO_ADMIN_DESCRIBE_INSTANCE_ACCESS_CONTROL_ATTRIBUTE_CONFIGURATION` — AWS Single Sign-On Admin `describe-instance-access-control-attribute-configuration`
- `LW_CFG_AWS_SSO_ADMIN_DESCRIBE_PERMISSION_SET` — AWS Single Sign-On Admin `describe-permission-set`
- `LW_CFG_AWS_SSO_ADMIN_GET_INLINE_POLICY_FOR_PERMISSION_SET` — AWS Single Sign-On Admin `get-inline-policy-for-permission-set`
- `LW_CFG_AWS_SSO_ADMIN_GET_PERMISSIONS_BOUNDARY_FOR_PERMISSION_SET` — AWS Single Sign-On Admin `get-permissions-boundary-for-permission-set`
- `LW_CFG_AWS_SSO_ADMIN_INSTANCES` — AWS Single Sign-On Admin `list-instances`
- `LW_CFG_AWS_SSO_ADMIN_MANAGED_POLICIES_IN_PERMISSION_SET` — AWS Single Sign-On Admin `list-managed-policies-in-permission-set`
- `LW_CFG_AWS_SSO_ADMIN_PERMISSION_SETS` — AWS Single Sign-On Admin `list-permission-sets`
- `LW_CFG_AWS_SSO_ADMIN_PERMISSION_SET_PROVISIONING_STATUS` — AWS Single Sign-On Admin `list-permission-set-provisioning-status`

### SSO Identity Store

- `LW_CFG_AWS_IDENTITYSTORE_GROUPS` — AWS SSO Identity Store `list-groups`
- `LW_CFG_AWS_IDENTITYSTORE_GROUP_MEMBERSHIPS` — AWS SSO Identity Store `list-group-memberships`
- `LW_CFG_AWS_IDENTITYSTORE_GROUP_MEMBERSHIPS_FOR_MEMBER` — AWS SSO Identity Store `list-group-memberships-for-member`
- `LW_CFG_AWS_IDENTITYSTORE_USERS` — AWS SSO Identity Store `list-users`

### Step Functions

- `LW_CFG_AWS_STEPFUNCTIONS_DESCRIBE_STATE_MACHINE` — AWS Step Functions `describe-state-machine`
- `LW_CFG_AWS_STEPFUNCTIONS_STATE_MACHINES` — AWS Step Functions `list-state-machines`

### Transfer Family

- `LW_CFG_AWS_TRANSFER_ACCESSES` — transfer `list-accesses`
- `LW_CFG_AWS_TRANSFER_AGREEMENTS` — transfer `list-agreements`
- `LW_CFG_AWS_TRANSFER_CERTIFICATES` — transfer `list-certificates`
- `LW_CFG_AWS_TRANSFER_CONNECTORS` — transfer `list-connectors`
- `LW_CFG_AWS_TRANSFER_DESCRIBE_ACCESS` — transfer `describe-access`
- `LW_CFG_AWS_TRANSFER_DESCRIBE_AGREEMENT` — transfer `describe-agreement`
- `LW_CFG_AWS_TRANSFER_DESCRIBE_CERTIFICATE` — transfer `describe-certificate`
- `LW_CFG_AWS_TRANSFER_DESCRIBE_CONNECTOR` — transfer `describe-connector`
- `LW_CFG_AWS_TRANSFER_DESCRIBE_EXECUTION` — transfer `describe-execution`
- `LW_CFG_AWS_TRANSFER_DESCRIBE_HOST_KEY` — transfer `describe-host-key`
- `LW_CFG_AWS_TRANSFER_DESCRIBE_PROFILE` — transfer `describe-profile`
- `LW_CFG_AWS_TRANSFER_DESCRIBE_SECURITY_POLICY` — transfer `describe-security-policy`
- `LW_CFG_AWS_TRANSFER_DESCRIBE_SERVER` — transfer `describe-server`
- `LW_CFG_AWS_TRANSFER_DESCRIBE_USER` — transfer `describe-user`
- `LW_CFG_AWS_TRANSFER_DESCRIBE_WEB_APP` — transfer `describe-web-app`
- `LW_CFG_AWS_TRANSFER_DESCRIBE_WEB_APP_CUSTOMIZATION` — transfer `describe-web-app-customization`
- `LW_CFG_AWS_TRANSFER_DESCRIBE_WORKFLOW` — transfer `describe-workflow`
- `LW_CFG_AWS_TRANSFER_EXECUTIONS` — transfer `list-executions`
- `LW_CFG_AWS_TRANSFER_HOST_KEYS` — transfer `list-host-keys`
- `LW_CFG_AWS_TRANSFER_PROFILES` — transfer `list-profiles`
- `LW_CFG_AWS_TRANSFER_SECURITY_POLICIES` — transfer `list-security-policies`
- `LW_CFG_AWS_TRANSFER_SERVERS` — transfer `list-servers`
- `LW_CFG_AWS_TRANSFER_USERS` — transfer `list-users`
- `LW_CFG_AWS_TRANSFER_WEB_APPS` — transfer `list-web-apps`
- `LW_CFG_AWS_TRANSFER_WORKFLOWS` — transfer `list-workflows`

### User Notifications

- `LW_CFG_AWS_NOTIFICATIONS_CHANNELS` — Results from AWS User Notifications 'list-channels'
- `LW_CFG_AWS_NOTIFICATIONS_EVENT_RULES` — Results from AWS User Notifications 'list-event-rules'
- `LW_CFG_AWS_NOTIFICATIONS_GET_EVENT_RULE` — Results from AWS User Notifications 'get-event-rule'
- `LW_CFG_AWS_NOTIFICATIONS_GET_NOTIFICATION_CONFIGURATION` — Results from AWS User Notifications 'get-notification-configuration'
- `LW_CFG_AWS_NOTIFICATIONS_GET_NOTIFICATION_EVENT` — Results from AWS User Notifications 'get-notification-event'
- `LW_CFG_AWS_NOTIFICATIONS_NOTIFICATION_CONFIGURATIONS` — Results from AWS User Notifications 'list-notification-configurations'
- `LW_CFG_AWS_NOTIFICATIONS_NOTIFICATION_EVENTS` — Results from AWS User Notifications 'list-notification-events'
- `LW_CFG_AWS_NOTIFICATIONS_NOTIFICATION_HUBS` — Results from AWS User Notifications 'list-notification-hubs'

### WAF

- `LW_CFG_AWS_WAF_ACTIVATED_RULES_IN_RULE_GROUP` — AWS WAF `list-activated-rules-in-rule-group`
- `LW_CFG_AWS_WAF_BYTE_MATCH_SETS` — AWS WAF `list-byte-match-sets`
- `LW_CFG_AWS_WAF_GEO_MATCH_SETS` — AWS WAF `list-geo-match-sets`
- `LW_CFG_AWS_WAF_GET_BYTE_MATCH_SET` — AWS WAF `get-byte-match-set`
- `LW_CFG_AWS_WAF_GET_GEO_MATCH_SET` — AWS WAF `get-geo-match-set`
- `LW_CFG_AWS_WAF_GET_IP_SET` — AWS WAF `get-ip-set`
- `LW_CFG_AWS_WAF_GET_LOGGING_CONFIGURATION` — AWS WAF `get-logging-configuration`
- `LW_CFG_AWS_WAF_LOGGING_CONFIGURATIONS` — AWS WAF `list-logging-configurations`
- `LW_CFG_AWS_WAF_GET_PERMISSION_POLICY` — AWS WAF `get-permission-policy`
- `LW_CFG_AWS_WAF_GET_RATE_BASED_RULE` — AWS WAF `get-rate-based-rule`
- `LW_CFG_AWS_WAF_GET_RATE_BASED_RULE_MANAGED_KEYS` — AWS WAF `get-rate-based-rule-managed-keys`
- `LW_CFG_AWS_WAF_GET_REGEX_MATCH_SET` — AWS WAF `get-regex-match-set`
- `LW_CFG_AWS_WAF_GET_REGEX_PATTERN_SET` — AWS WAF `get-regex-pattern-set`
- `LW_CFG_AWS_WAF_GET_RULE` — AWS WAF `get-rule`
- `LW_CFG_AWS_WAF_GET_RULE_GROUP` — AWS WAF `get-rule-group`
- `LW_CFG_AWS_WAF_GET_SIZE_CONSTRAINT_SET` — AWS WAF `get-size-constraint-set`
- `LW_CFG_AWS_WAF_GET_SQL_INJECTION_MATCH_SET` — AWS WAF `get-sql-injection-match-set`
- `LW_CFG_AWS_WAF_GET_WEB_ACL` — AWS WAF `get-web-acl`
- `LW_CFG_AWS_WAF_GET_XSS_MATCH_SET` — AWS WAF `get-xss-match-set`
- `LW_CFG_AWS_WAF_IP_SETS` — waf `list-ip-sets`
- `LW_CFG_AWS_WAF_RATE_BASED_RULES` — AWS WAF `list-rate-based-rules`
- `LW_CFG_AWS_WAF_REGEX_MATCH_SETS` — AWS WAF `list-regex-match-sets`
- `LW_CFG_AWS_WAF_REGEX_PATTERN_SETS` — waf `list-regex-pattern-sets`
- `LW_CFG_AWS_WAF_RULES` — AWS WAF `list-rules`
- `LW_CFG_AWS_WAF_RULE_GROUPS` — AWS WAF `list-rule-groups`
- `LW_CFG_AWS_WAF_SIZE_CONSTRAINT_SETS` — AWS WAF `list-size-constraint-sets`
- `LW_CFG_AWS_WAF_SQL_INJECTION_MATCH_SETS` — AWS WAF `list-sql-injection-match-sets`
- `LW_CFG_AWS_WAF_WEB_ACLS` — AWS WAF `list-web-acls`
- `LW_CFG_AWS_WAF_XSS_MATCH_SETS` — AWS WAF `list-xss-match-sets`

### WAF Regional

- `LW_CFG_AWS_WAF_REGIONAL_ACTIVATED_RULES_IN_RULE_GROUP` — Results from AWS WAF Regional 'list-activated-rules-in-rule-group'
- `LW_CFG_AWS_WAF_REGIONAL_BYTE_MATCH_SETS` — Results from AWS WAF Regional 'list-byte-match-sets'
- `LW_CFG_AWS_WAF_REGIONAL_GEO_MATCH_SETS` — Results from AWS WAF Regional 'list-geo-match-sets'
- `LW_CFG_AWS_WAF_REGIONAL_GET_BYTE_MATCH_SET` — Results from AWS WAF Regional 'get-byte-match-set'
- `LW_CFG_AWS_WAF_REGIONAL_GET_GEO_MATCH_SET` — Results from AWS WAF Regional 'get-geo-match-set'
- `LW_CFG_AWS_WAF_REGIONAL_GET_IP_SET` — Results from AWS WAF Regional 'get-ip-set'
- `LW_CFG_AWS_WAF_REGIONAL_GET_LOGGING_CONFIGURATION` — Results from AWS WAF Regional 'get-logging-configuration'
- `LW_CFG_AWS_WAF_REGIONAL_GET_PERMISSION_POLICY` — Results from AWS WAF Regional 'get-permission-policy'
- `LW_CFG_AWS_WAF_REGIONAL_GET_RATE_BASED_RULE` — Results from AWS WAF Regional 'get-rate-based-rule'
- `LW_CFG_AWS_WAF_REGIONAL_GET_REGEX_MATCH_SET` — Results from AWS WAF Regional 'get-regex-match-set'
- `LW_CFG_AWS_WAF_REGIONAL_GET_REGEX_PATTERN_SET` — Results from AWS WAF Regional 'get-regex-pattern-set'
- `LW_CFG_AWS_WAF_REGIONAL_GET_RULE` — AWS WAF Regional `get-rule`
- `LW_CFG_AWS_WAF_REGIONAL_GET_RULE_GROUP` — AWS WAF Regional `get-rule-group`
- `LW_CFG_AWS_WAF_REGIONAL_GET_SIZE_CONSTRAINT_SET` — Results from AWS WAF Regional 'get-size-constraint-set'
- `LW_CFG_AWS_WAF_REGIONAL_GET_SQL_INJECTION_MATCH_SET` — Results from AWS WAF Regional 'get-sql-injection-match-set'
- `LW_CFG_AWS_WAF_REGIONAL_GET_WEB_ACL` — AWS WAF Regional `get-web-acl`
- `LW_CFG_AWS_WAF_REGIONAL_GET_XSS_MATCH_SET` — Results from AWS WAF Regional 'get-xss-match-set'
- `LW_CFG_AWS_WAF_REGIONAL_IP_SETS` — Results from AWS WAF Regional 'list-ip-sets'
- `LW_CFG_AWS_WAF_REGIONAL_RATE_BASED_RULES` — Results from AWS WAF Regional 'list-rate-based-rules'
- `LW_CFG_AWS_WAF_REGIONAL_REGEX_MATCH_SETS` — Results from AWS WAF Regional 'list-regex-match-sets'
- `LW_CFG_AWS_WAF_REGIONAL_REGEX_PATTERN_SETS` — Results from AWS WAF Regional 'list-regex-pattern-sets'
- `LW_CFG_AWS_WAF_REGIONAL_RESOURCES_FOR_WEB_ACL` — AWS WAF Regional `list-resources-for-web-acl`
- `LW_CFG_AWS_WAF_REGIONAL_RULE_GROUPS` — AWS WAF Regional `list-rule-groups`
- `LW_CFG_AWS_WAF_REGIONAL_RULES` — AWS WAF Regional `list-rules`
- `LW_CFG_AWS_WAF_REGIONAL_SIZE_CONSTRAINT_SETS` — Results from AWS WAF Regional 'list-size-constraint-sets'
- `LW_CFG_AWS_WAF_REGIONAL_SQL_INJECTION_MATCH_SETS` — Results from AWS WAF Regional 'list-sql-injection-match-sets'
- `LW_CFG_AWS_WAF_REGIONAL_WEB_ACLS` — AWS WAF Regional `list-web-acls`
- `LW_CFG_AWS_WAF_REGIONAL_XSS_MATCH_SETS` — Results from AWS WAF Regional 'list-xss-match-sets'

### WAF V2

- `LW_CFG_AWS_WAFV2_GET_LOGGING_CONFIGURATION` — wafv2 `get-logging-configuration`
- `LW_CFG_AWS_WAFV2_GET_WEB_ACL` — wafv2 `get-web-acl`
- `LW_CFG_AWS_WAFV2_IP_SETS` — wafv2 `list-ip-sets`
- `LW_CFG_AWS_WAFV2_LIST_RESOURCES_FOR_WEB_ACL` — wafv2 `list-resources-for-web-acl`
- `LW_CFG_AWS_WAFV2_REGEX_PATTERN_SETS` — wafv2 `list-regex-pattern-sets`
- `LW_CFG_AWS_WAFV2_RULE_GROUPS` — wafv2 `list-rule-groups`
- `LW_CFG_AWS_WAFV2_WEB_ACLS` — wafv2 `list-web-acls`

### WorkSpaces

- `LW_CFG_AWS_WORKSPACES_DESCRIBE_WORKSPACES` — AWS Workspaces `describe-workspaces`
- `LW_CFG_AWS_WORKSPACES_WORKSPACES` — Results from Amazon WorkSpaces 'describe-workspaces'


## CloudTrail Logging Datasources

### CloudTrailRawEvents

Events reported by AWS CloudTrail service.

- `INSERT_ID` (Number) — Generated identification
- `INSERT_TIME` (Timestamp) — Time the event was created
- `EVENT_TIME` (Timestamp) — Time the event occurred
- `EVENT` (JSON) — Content of the event
- `EVENT_SOURCE` (String) — The source AWS service principal of the event
- `EVENT_NAME` (String) — Name of the event
- `ERROR_CODE` (String) — Code for the error
