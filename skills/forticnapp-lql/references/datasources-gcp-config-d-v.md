<!-- Generated from FortiCNAPP 26.2 LQL Reference Guide (fetched 2026-10-28). Source:
     https://docs.fortinet.com/document/forticnapp/latest/lql-reference/771173/datasource-metadata -->

# Datasource Metadata

## Google Cloud Configuration Datasources

All Google Cloud configuration datasources listed in this section have the same metadata available.

- `BATCH_START_TIME` (Timestamp) — Beginning of time interval
- `BATCH_END_TIME` (Timestamp) — End of time interval
- `QUERY_START_TIME` (Timestamp) — Start time of query for this resource
- `QUERY_END_TIME` (Timestamp) — End time of query for this resource
- `URN` (String) — URN for the resource
- `API_KEY` (String) — Key describing the API used to fetch data for this resource
- `SERVICE` (String) — Service this resource belongs to
- `ORGANIZATION_ID` (Number) — Google Cloud Organization ID
- `ORGANIZATION_NAME` (String) — Google Cloud Organization name
- `PROJECT_NUMBER` (Number) — Google Cloud Project number
- `PROJECT_ID` (String) — Unique ID for the project
- `PROJECT_NAME` (String) — Project Name (display name)
- `FOLDER_IDS` (JSON) — Numeric folder IDs as an array
- `FOLDER_NAMES` (JSON) — Human-friendly folder names as an array. Though a corresponding entry in FOLDER_NAMES exists for each entry in FOLDER_IDS, Lacework may not be able to retrieve it due to permissions, which depend on the integration. Most project integrations will not have the necessary permissions to resolve the folderNames.
- `PARENT_RESOURCE_ID` (String) — Parent resource ID for this resource
- `RESOURCE_TYPE` (String) — Type of this resource
- `RESOURCE_ID` (String) — Identifier for this resource
- `RESOURCE_REGION` (String) — Region this resource belongs to
- `RESOURCE_CONFIG` (JSON) — JSON Definition of this resource
- `RESOURCE_TAGS` (JSON) — Tags (labels) associated with this resource

### Data Loss Prevention

- `LW_CFG_GCP_DLP_DEIDENTIFYTEMPLATE` — Results for GCP dlp DeidentifyTemplate resource objects
- `LW_CFG_GCP_DLP_DEIDENTIFYTEMPLATE_IAMPOLICY` — Results for GCP dlp DeidentifyTemplate iamPolicy objects
- `LW_CFG_GCP_DLP_DLPJOB` — Results for GCP dlp DlpJob resource objects
- `LW_CFG_GCP_DLP_DLPJOB_IAMPOLICY` — Results for GCP dlp DlpJob iamPolicy objects
- `LW_CFG_GCP_DLP_INSPECTTEMPLATE` — Results for GCP dlp InspectTemplate resource objects
- `LW_CFG_GCP_DLP_INSPECTTEMPLATE_IAMPOLICY` — Results for GCP dlp InspectTemplate iamPolicy objects
- `LW_CFG_GCP_DLP_JOBTRIGGER` — Results for GCP dlp JobTrigger resource objects
- `LW_CFG_GCP_DLP_JOBTRIGGER_IAMPOLICY` — Results for GCP dlp JobTrigger iamPolicy objects
- `LW_CFG_GCP_DLP_STOREDINFOTYPE` — Results for GCP dlp StoredInfoType resource objects
- `LW_CFG_GCP_DLP_STOREDINFOTYPE_IAMPOLICY` — Results for GCP dlp StoredInfoType iamPolicy objects

### Database Migration

- `LW_CFG_GCP_DATAMIGRATION_CONNECTIONPROFILE` — Results for GCP datamigration ConnectionProfile resource objects
- `LW_CFG_GCP_DATAMIGRATION_CONNECTIONPROFILE_IAMPOLICY` — Results for GCP datamigration ConnectionProfile iamPolicy objects
- `LW_CFG_GCP_DATAMIGRATION_MIGRATIONJOB` — Results for GCP datamigration MigrationJob resource objects
- `LW_CFG_GCP_DATAMIGRATION_MIGRATIONJOB_IAMPOLICY` — Results for GCP datamigration MigrationJob iamPolicy objects

### Dataflow

- `LW_CFG_GCP_DATAFLOW_JOB` — Results for GCP dataflow Job resource objects
- `LW_CFG_GCP_DATAFLOW_JOB_IAMPOLICY` — Results for GCP dataflow Job iamPolicy objects

### Dataplex

- `LW_CFG_GCP_DATAPLEX_ASSET` — Results for GCP dataplex Asset resource objects
- `LW_CFG_GCP_DATAPLEX_ASSET_IAMPOLICY` — Results for GCP dataplex Asset iamPolicy objects
- `LW_CFG_GCP_DATAPLEX_LAKE` — Results for GCP dataplex Lake resource objects
- `LW_CFG_GCP_DATAPLEX_LAKE_IAMPOLICY` — Results for GCP dataplex Lake iamPolicy objects
- `LW_CFG_GCP_DATAPLEX_TASK` — Results for GCP dataplex Task resource objects
- `LW_CFG_GCP_DATAPLEX_TASK_IAMPOLICY` — Results for GCP dataplex Task iamPolicy objects
- `LW_CFG_GCP_DATAPLEX_ZONE` — Results for GCP dataplex Zone resource objects
- `LW_CFG_GCP_DATAPLEX_ZONE_IAMPOLICY` — Results for GCP dataplex Zone iamPolicy objects

### Dataproc

- `LW_CFG_GCP_DATAPROC_CLUSTER` — Google Cloud dataproc Cluster resource objects
- `LW_CFG_GCP_DATAPROC_CLUSTER_IAMPOLICY` — Results for GCP dataproc Cluster iamPolicy objects
- `LW_CFG_GCP_DATAPROC_JOB` — Results for GCP dataproc Job resource objects
- `LW_CFG_GCP_DATAPROC_JOB_IAMPOLICY` — Results for GCP dataproc Job iamPolicy objects

### Datastream

- `LW_CFG_GCP_DATASTREAM_CONNECTIONPROFILE` — Results for GCP datastream ConnectionProfile resource objects
- `LW_CFG_GCP_DATASTREAM_CONNECTIONPROFILE_IAMPOLICY` — Results for GCP datastream ConnectionProfile iamPolicy objects
- `LW_CFG_GCP_DATASTREAM_PRIVATECONNECTION` — Results for GCP datastream PrivateConnection resource objects
- `LW_CFG_GCP_DATASTREAM_PRIVATECONNECTION_IAMPOLICY` — Results for GCP datastream PrivateConnection iamPolicy objects
- `LW_CFG_GCP_DATASTREAM_STREAM` — Results for GCP datastream Stream resource objects
- `LW_CFG_GCP_DATASTREAM_STREAM_IAMPOLICY` — Results for GCP datastream Stream iamPolicy objects

### Dialogflow

- `LW_CFG_GCP_DIALOGFLOW_AGENT` — Results for GCP dialogflow Agent resource objects
- `LW_CFG_GCP_DIALOGFLOW_AGENT_IAMPOLICY` — Results for GCP dialogflow Agent iamPolicy objects
- `LW_CFG_GCP_DIALOGFLOW_CONVERSATIONPROFILE` — Results for GCP dialogflow ConversationProfile resource objects
- `LW_CFG_GCP_DIALOGFLOW_CONVERSATIONPROFILE_IAMPOLICY` — Results for GCP dialogflow ConversationProfile iamPolicy objects
- `LW_CFG_GCP_DIALOGFLOW_KNOWLEDGEBASE` — Results for GCP dialogflow KnowledgeBase resource objects
- `LW_CFG_GCP_DIALOGFLOW_KNOWLEDGEBASE_IAMPOLICY` — Results for GCP dialogflow KnowledgeBase iamPolicy objects
- `LW_CFG_GCP_DIALOGFLOW_LOCATIONSETTINGS` — Results for GCP dialogflow LocationSettings resource objects
- `LW_CFG_GCP_DIALOGFLOW_LOCATIONSETTINGS_IAMPOLICY` — Results for GCP dialogflow LocationSettings iamPolicy objects

### DNS

- `LW_CFG_GCP_DNS_MANAGEDZONE` — Google Cloud dns ManagedZone resource objects
- `LW_CFG_GCP_DNS_POLICY` — Google Cloud dns Policy resource objects
- `LW_CFG_GCP_DNS_MANAGEDZONE_IAMPOLICY` — Results for GCP dns ManagedZone iamPolicy objects
- `LW_CFG_GCP_DNS_POLICY_IAMPOLICY` — Results for GCP dns Policy iamPolicy objects

### Document AI

- `LW_CFG_GCP_DOCUMENTAI_HUMANREVIEWCONFIG` — Results for GCP documentai HumanReviewConfig resource objects
- `LW_CFG_GCP_DOCUMENTAI_HUMANREVIEWCONFIG_IAMPOLICY` — Results for GCP documentai HumanReviewConfig iamPolicy objects
- `LW_CFG_GCP_DOCUMENTAI_LABELERPOOL` — Results for GCP documentai LabelerPool resource objects
- `LW_CFG_GCP_DOCUMENTAI_LABELERPOOL_IAMPOLICY` — Results for GCP documentai LabelerPool iamPolicy objects
- `LW_CFG_GCP_DOCUMENTAI_PROCESSOR` — Results for GCP documentai Processor resource objects
- `LW_CFG_GCP_DOCUMENTAI_PROCESSORVERSION` — Results for GCP documentai ProcessorVersion resource objects
- `LW_CFG_GCP_DOCUMENTAI_PROCESSORVERSION_IAMPOLICY` — Results for GCP documentai ProcessorVersion iamPolicy objects
- `LW_CFG_GCP_DOCUMENTAI_PROCESSOR_IAMPOLICY` — Results for GCP documentai Processor iamPolicy objects

### Essential Contact

- `LW_CFG_GCP_ESSENTIALCONTACT_CONTACT` — Google Cloud Essential Contacts contacts resource objects

### Eventarc

- `LW_CFG_GCP_EVENTARC_TRIGGER` — Results for GCP eventarc Trigger resource objects
- `LW_CFG_GCP_EVENTARC_TRIGGER_IAMPOLICY` — Results for GCP eventarc Trigger iamPolicy objects

### Extensions

- `LW_CFG_GCP_EXTENSIONS_INGRESS` — Results for GCP extensions Ingress resource objects
- `LW_CFG_GCP_EXTENSIONS_INGRESS_IAMPOLICY` — Results for GCP extensions Ingress iamPolicy objects

### File

- `LW_CFG_GCP_FILE_BACKUP` — Results for GCP file Backup resource objects
- `LW_CFG_GCP_FILE_BACKUP_IAMPOLICY` — Results for GCP file Backup iamPolicy objects
- `LW_CFG_GCP_FILE_INSTANCE` — Results for GCP file Instance resource objects
- `LW_CFG_GCP_FILE_INSTANCE_IAMPOLICY` — Results for GCP file Instance iamPolicy objects

### Firestore

- `LW_CFG_GCP_FIRESTORE_DATABASE` — Results for GCP firestore Database resource objects
- `LW_CFG_GCP_FIRESTORE_DATABASE_IAMPOLICY` — Results for GCP firestore Database iamPolicy objects

### Game Services

- `LW_CFG_GCP_GAMESERVICES_GAMESERVERCLUSTER` — Results for GCP gameservices GameServerCluster resource objects
- `LW_CFG_GCP_GAMESERVICES_GAMESERVERCLUSTER_IAMPOLICY` — Results for GCP gameservices GameServerCluster iamPolicy objects
- `LW_CFG_GCP_GAMESERVICES_GAMESERVERCONFIG` — Results for GCP gameservices GameServerConfig resource objects
- `LW_CFG_GCP_GAMESERVICES_GAMESERVERCONFIG_IAMPOLICY` — Results for GCP gameservices GameServerConfig iamPolicy objects
- `LW_CFG_GCP_GAMESERVICES_GAMESERVERDEPLOYMENT` — Results for GCP gameservices GameServerDeployment resource objects
- `LW_CFG_GCP_GAMESERVICES_GAMESERVERDEPLOYMENT_IAMPOLICY` — Results for GCP gameservices GameServerDeployment iamPolicy objects
- `LW_CFG_GCP_GAMESERVICES_REALM` — Results for GCP gameservices Realm resource objects
- `LW_CFG_GCP_GAMESERVICES_REALM_IAMPOLICY` — Results for GCP gameservices Realm iamPolicy objects

### GKE Hub

- `LW_CFG_GCP_GKEHUB_MEMBERSHIP` — Results for GCP gkehub Membership resource objects
- `LW_CFG_GCP_GKEHUB_MEMBERSHIP_IAMPOLICY` — Results for GCP gkehub Membership iamPolicy objects

### Healthcare

- `LW_CFG_GCP_HEALTHCARE_CONSENTSTORE` — Results for GCP healthcare ConsentStore resource objects
- `LW_CFG_GCP_HEALTHCARE_CONSENTSTORE_IAMPOLICY` — Results for GCP healthcare ConsentStore iamPolicy objects
- `LW_CFG_GCP_HEALTHCARE_DATASET` — Results for GCP healthcare Dataset resource objects
- `LW_CFG_GCP_HEALTHCARE_DATASET_IAMPOLICY` — Results for GCP healthcare Dataset iamPolicy objects
- `LW_CFG_GCP_HEALTHCARE_DICOMSTORE` — Results for GCP healthcare DicomStore resource objects
- `LW_CFG_GCP_HEALTHCARE_DICOMSTORE_IAMPOLICY` — Results for GCP healthcare DicomStore iamPolicy objects
- `LW_CFG_GCP_HEALTHCARE_FHIRSTORE` — Results for GCP healthcare FhirStore resource objects
- `LW_CFG_GCP_HEALTHCARE_FHIRSTORE_IAMPOLICY` — Results for GCP healthcare FhirStore iamPolicy objects
- `LW_CFG_GCP_HEALTHCARE_HL7V2STORE` — Results for GCP healthcare Hl7V2Store resource objects
- `LW_CFG_GCP_HEALTHCARE_HL7V2STORE_IAMPOLICY` — Results for GCP healthcare Hl7V2Store iamPolicy objects

### Identity and Access Management

- `LW_CFG_GCP_IAM_IAMPOLICY_ALL` — All iamPolicy objects for all resource types
- `LW_CFG_GCP_IAM_ROLE` — Results for GCP iam Role resource objects
- `LW_CFG_GCP_IAM_ROLE_IAMPOLICY` — Results for GCP iam Role iamPolicy objects
- `LW_CFG_GCP_IAM_SERVICEACCOUNT` — Google Cloud iam ServiceAccount resource objects
- `LW_CFG_GCP_IAM_SERVICEACCOUNT_IAMPOLICY` — Google Cloud iam ServiceAccount IAMPolicy objects (the corresponding access permissions for iam ServiceAccount IAMPolicy)
- `LW_CFG_GCP_IAM_SERVICEACCOUNTKEY` — Google Cloud iam ServiceAccountKey resource objects
- `LW_CFG_GCP_IAM_SERVICEACCOUNTKEY_IAMPOLICY` — Results for GCP iam ServiceAccountKey iamPolicy objects

### Kubernetes

- `LW_CFG_GCP_K8S_NAMESPACE` — Results for GCP k8s Namespace resource objects
- `LW_CFG_GCP_K8S_NAMESPACE_IAMPOLICY` — Results for GCP k8s Namespace iamPolicy objects
- `LW_CFG_GCP_K8S_NODE` — Results for GCP k8s Node resource objects
- `LW_CFG_GCP_K8S_NODE_IAMPOLICY` — Results for GCP k8s Node iamPolicy objects
- `LW_CFG_GCP_K8S_POD` — Results for GCP k8s Pod resource objects
- `LW_CFG_GCP_K8S_POD_IAMPOLICY` — Results for GCP k8s Pod iamPolicy objects
- `LW_CFG_GCP_K8S_SERVICE` — Results for GCP k8s Service resource objects
- `LW_CFG_GCP_K8S_SERVICE_IAMPOLICY` — Results for GCP k8s Service iamPolicy objects

### Logging

- `LW_CFG_GCP_LOGGING_LOGMETRIC` — Google Cloud logging LogMetric resource objects
- `LW_CFG_GCP_LOGGING_LOGSINK` — Google Cloud logging LogSink resource objects
- `LW_CFG_GCP_LOGGING_LOGBUCKET` — Results for GCP logging LogBucket resource objects
- `LW_CFG_GCP_LOGGING_LOGBUCKET_IAMPOLICY` — Results for GCP logging LogBucket iamPolicy objects
- `LW_CFG_GCP_LOGGING_LOGMETRIC_IAMPOLICY` — Results for GCP logging LogMetric iamPolicy objects
- `LW_CFG_GCP_LOGGING_LOGSINK_IAMPOLICY` — Results for GCP logging LogSink iamPolicy objects

### Managed Identities

- `LW_CFG_GCP_MANAGEDIDENTITIES_DOMAIN` — Results for GCP managedidentities Domain resource objects
- `LW_CFG_GCP_MANAGEDIDENTITIES_DOMAIN_IAMPOLICY` — Results for GCP managedidentities Domain iamPolicy objects

### Memcache

- `LW_CFG_GCP_MEMCACHE_INSTANCE` — Results for GCP memcache Instance resource objects
- `LW_CFG_GCP_MEMCACHE_INSTANCE_IAMPOLICY` — Results for GCP memcache Instance iamPolicy objects

### Metastore

- `LW_CFG_GCP_METASTORE_BACKUP` — Results for GCP metastore Backup resource objects
- `LW_CFG_GCP_METASTORE_BACKUP_IAMPOLICY` — Results for GCP metastore Backup iamPolicy objects
- `LW_CFG_GCP_METASTORE_METADATAIMPORT` — Results for GCP metastore MetadataImport resource objects
- `LW_CFG_GCP_METASTORE_METADATAIMPORT_IAMPOLICY` — Results for GCP metastore MetadataImport iamPolicy objects
- `LW_CFG_GCP_METASTORE_SERVICE` — Results for GCP metastore Service resource objects
- `LW_CFG_GCP_METASTORE_SERVICE_IAMPOLICY` — Results for GCP metastore Service iamPolicy objects

### Monitoring

- `LW_CFG_GCP_MONITORING_ALERTPOLICY` — Google Cloud monitoring AlertPolicy resource objects
- `LW_CFG_GCP_MONITORING_ALERTPOLICY_IAMPOLICY` — Results for GCP monitoring AlertPolicy iamPolicy objects

### Network Connectivity

- `LW_CFG_GCP_NETWORKCONNECTIVITY_HUB` — Results for GCP networkconnectivity Hub resource objects
- `LW_CFG_GCP_NETWORKCONNECTIVITY_HUB_IAMPOLICY` — Results for GCP networkconnectivity Hub iamPolicy objects
- `LW_CFG_GCP_NETWORKCONNECTIVITY_SPOKE` — Results for GCP networkconnectivity Spoke resource objects
- `LW_CFG_GCP_NETWORKCONNECTIVITY_SPOKE_IAMPOLICY` — Results for GCP networkconnectivity Spoke iamPolicy objects

### Network Management

- `LW_CFG_GCP_NETWORKMANAGEMENT_CONNECTIVITYTEST` — Results for GCP networkmanagement ConnectivityTest resource objects
- `LW_CFG_GCP_NETWORKMANAGEMENT_CONNECTIVITYTEST_IAMPOLICY` — Results for GCP networkmanagement ConnectivityTest iamPolicy objects

### Networking

- `LW_CFG_GCP_NETWORKING_INGRESS` — Results for GCP networking Ingress resource objects
- `LW_CFG_GCP_NETWORKING_INGRESS_IAMPOLICY` — Results for GCP networking Ingress iamPolicy objects
- `LW_CFG_GCP_NETWORKING_NETWORKPOLICY` — Results for GCP networking NetworkPolicy resource objects
- `LW_CFG_GCP_NETWORKING_NETWORKPOLICY_IAMPOLICY` — Results for GCP networking NetworkPolicy iamPolicy objects

### Organization Policy

- `LW_CFG_GCP_ORGPOLICY_POLICY` — Results for GCP orgpolicy Policy resource objects
- `LW_CFG_GCP_ORGPOLICY_POLICY_IAMPOLICY` — Results for GCP orgpolicy Policy iamPolicy objects

### OS Config

- `LW_CFG_GCP_OSCONFIG_OSPOLICYASSIGNMENT` — Results for GCP osconfig OSPolicyAssignment resource objects
- `LW_CFG_GCP_OSCONFIG_OSPOLICYASSIGNMENTREPORT` — Results for GCP osconfig OSPolicyAssignmentReport resource objects
- `LW_CFG_GCP_OSCONFIG_OSPOLICYASSIGNMENTREPORT_IAMPOLICY` — Results for GCP osconfig OSPolicyAssignmentReport iamPolicy objects
- `LW_CFG_GCP_OSCONFIG_OSPOLICYASSIGNMENT_IAMPOLICY` — Results for GCP osconfig OSPolicyAssignment iamPolicy objects
- `LW_CFG_GCP_OSCONFIG_PATCHDEPLOYMENT` — Results for GCP osconfig PatchDeployment resource objects
- `LW_CFG_GCP_OSCONFIG_PATCHDEPLOYMENT_IAMPOLICY` — Results for GCP osconfig PatchDeployment iamPolicy objects
- `LW_CFG_GCP_OSCONFIG_VULNERABILITYREPORT` — Results for GCP osconfig VulnerabilityReport resource objects
- `LW_CFG_GCP_OSCONFIG_VULNERABILITYREPORT_IAMPOLICY` — Results for GCP osconfig VulnerabilityReport iamPolicy objects

### Pub/Sub

- `LW_CFG_GCP_PUBSUB_SNAPSHOT` — Results for GCP pubsub Snapshot resource objects
- `LW_CFG_GCP_PUBSUB_SNAPSHOT_IAMPOLICY` — Results for GCP pubsub Snapshot iamPolicy objects
- `LW_CFG_GCP_PUBSUB_SUBSCRIPTION` — Results for GCP pubsub Subscription resource objects
- `LW_CFG_GCP_PUBSUB_SUBSCRIPTION_IAMPOLICY` — Results for GCP pubsub Subscription iamPolicy objects
- `LW_CFG_GCP_PUBSUB_TOPIC` — Results for GCP pubsub Topic resource objects
- `LW_CFG_GCP_PUBSUB_TOPIC_IAMPOLICY` — Results for GCP pubsub Topic iamPolicy objects

### Redis

- `LW_CFG_GCP_REDIS_INSTANCE` — Results for GCP redis Instance resource objects
- `LW_CFG_GCP_REDIS_INSTANCE_IAMPOLICY` — Results for GCP redis Instance iamPolicy objects

### Role-Based Access Control

- `LW_CFG_GCP_RBAC_CLUSTERROLE` — Results for GCP rbac ClusterRole resource objects
- `LW_CFG_GCP_RBAC_CLUSTERROLEBINDING` — Results for GCP rbac ClusterRoleBinding resource objects
- `LW_CFG_GCP_RBAC_CLUSTERROLEBINDING_IAMPOLICY` — Results for GCP rbac ClusterRoleBinding iamPolicy objects
- `LW_CFG_GCP_RBAC_CLUSTERROLE_IAMPOLICY` — Results for GCP rbac ClusterRole iamPolicy objects
- `LW_CFG_GCP_RBAC_ROLE` — Results for GCP rbac Role resource objects
- `LW_CFG_GCP_RBAC_ROLEBINDING` — Results for GCP rbac RoleBinding resource objects
- `LW_CFG_GCP_RBAC_ROLEBINDING_IAMPOLICY` — Results for GCP rbac RoleBinding iamPolicy objects
- `LW_CFG_GCP_RBAC_ROLE_IAMPOLICY` — Results for GCP rbac Role iamPolicy objects

### Run

- `LW_CFG_GCP_RUN_DOMAINMAPPING` — Results for GCP run DomainMapping resource objects
- `LW_CFG_GCP_RUN_DOMAINMAPPING_IAMPOLICY` — Results for GCP run DomainMapping iamPolicy objects
- `LW_CFG_GCP_RUN_EXECUTION` — Results for GCP run Execution resource objects
- `LW_CFG_GCP_RUN_EXECUTION_IAMPOLICY` — Results for GCP run Execution iamPolicy objects
- `LW_CFG_GCP_RUN_JOB` — Results for GCP run Job resource objects
- `LW_CFG_GCP_RUN_JOB_IAMPOLICY` — Results for GCP run Job iamPolicy objects
- `LW_CFG_GCP_RUN_REVISION` — Results for GCP run Revision resource objects
- `LW_CFG_GCP_RUN_REVISION_IAMPOLICY` — Results for GCP run Revision iamPolicy objects
- `LW_CFG_GCP_RUN_SERVICE` — Results for GCP run Service resource objects
- `LW_CFG_GCP_RUN_SERVICE_IAMPOLICY` — Results for GCP run Service iamPolicy objects

### Secret Manager

- `LW_CFG_GCP_SECRETMANAGER_SECRET` — Results for GCP secretmanager Secret resource objects
- `LW_CFG_GCP_SECRETMANAGER_SECRETVERSION` — Results for GCP secretmanager SecretVersion resource objects
- `LW_CFG_GCP_SECRETMANAGER_SECRETVERSION_IAMPOLICY` — Results for GCP secretmanager SecretVersion iamPolicy objects
- `LW_CFG_GCP_SECRETMANAGER_SECRET_IAMPOLICY` — Results for GCP secretmanager Secret iamPolicy objects

### Service Directory

- `LW_CFG_GCP_SERVICEDIRECTORY_NAMESPACE` — Results for GCP servicedirectory Namespace resource objects
- `LW_CFG_GCP_SERVICEDIRECTORY_NAMESPACE_IAMPOLICY` — Results for GCP servicedirectory Namespace iamPolicy objects

### Service Management

- `LW_CFG_GCP_SERVICEMANAGEMENT_MANAGEDSERVICE` — Results for GCP servicemanagement ManagedService resource objects
- `LW_CFG_GCP_SERVICEMANAGEMENT_MANAGEDSERVICE_IAMPOLICY` — Results for GCP servicemanagement ManagedService iamPolicy objects

### Service Usage

- `LW_CFG_GCP_SERVICEUSAGE_SERVICE` — Google Cloud serviceusage Service resource objects
- `LW_CFG_GCP_SERVICEUSAGE_SERVICE_IAMPOLICY` — Results for GCP serviceusage Service iamPolicy objects

### Spanner

- `LW_CFG_GCP_SPANNER_BACKUP` — Results for GCP spanner Backup resource objects
- `LW_CFG_GCP_SPANNER_BACKUP_IAMPOLICY` — Results for GCP spanner Backup iamPolicy objects
- `LW_CFG_GCP_SPANNER_DATABASE` — Results for GCP spanner Database resource objects
- `LW_CFG_GCP_SPANNER_DATABASE_IAMPOLICY` — Results for GCP spanner Database iamPolicy objects
- `LW_CFG_GCP_SPANNER_INSTANCE` — Results for GCP spanner Instance resource objects
- `LW_CFG_GCP_SPANNER_INSTANCE_IAMPOLICY` — Results for GCP spanner Instance iamPolicy objects

### SQL Admin

- `LW_CFG_GCP_SQLADMIN_INSTANCE` — Google Cloud sqladmin Instance resource objects
- `LW_CFG_GCP_SQLADMIN_INSTANCE_IAMPOLICY` — Results for GCP sqladmin Instance iamPolicy objects
- `LW_CFG_GCP_SQLADMIN_BACKUPRUN` — Results for GCP sqladmin BackupRun resource objects
- `LW_CFG_GCP_SQLADMIN_BACKUPRUN_IAMPOLICY` — Results for GCP sqladmin BackupRun iamPolicy objects

### Storage

- `LW_CFG_GCP_STORAGE_BUCKET` — Google Cloud storage Bucket resource objects
- `LW_CFG_GCP_STORAGE_BUCKET_IAMPOLICY` — Results for GCP storage Bucket iamPolicy objects
- `LW_CFG_GCP_STORAGE_BUCKET_POLICY` — Google Cloud storage Bucket IAMPolicy objects (the corresponding access permissions for storage Bucket IAMPolicy)

### Tensor Processing Units

- `LW_CFG_GCP_TPU_NODE` — Results for GCP tpu Node resource objects
- `LW_CFG_GCP_TPU_NODE_IAMPOLICY` — Results for GCP tpu Node iamPolicy objects

### VPC Access

- `LW_CFG_GCP_VPCACCESS_CONNECTOR` — Results for GCP vpcaccess Connector resource objects
- `LW_CFG_GCP_VPCACCESS_CONNECTOR_IAMPOLICY` — Results for GCP vpcaccess Connector iamPolicy objects
