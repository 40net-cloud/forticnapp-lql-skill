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
