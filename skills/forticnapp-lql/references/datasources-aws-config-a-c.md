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
