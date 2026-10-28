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
