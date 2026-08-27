<!-- Generated from FortiCNAPP 26.2 LQL Reference Guide (fetched 2026-08-26). Source:
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

### AIPlatform

- `LW_CFG_GCP_AIPLATFORM_BATCHPREDICTIONJOB` — Results for GCP aiplatform BatchPredictionJob resource objects
- `LW_CFG_GCP_AIPLATFORM_BATCHPREDICTIONJOB_IAMPOLICY` — Results for GCP aiplatform BatchPredictionJob iamPolicy objects
- `LW_CFG_GCP_AIPLATFORM_CUSTOMJOB` — Results for GCP aiplatform CustomJob resource objects
- `LW_CFG_GCP_AIPLATFORM_CUSTOMJOB_IAMPOLICY` — Results for GCP aiplatform CustomJob iamPolicy objects
- `LW_CFG_GCP_AIPLATFORM_DATALABELINGJOB` — Results for GCP aiplatform DataLabelingJob resource objects
- `LW_CFG_GCP_AIPLATFORM_DATALABELINGJOB_IAMPOLICY` — Results for GCP aiplatform DataLabelingJob iamPolicy objects
- `LW_CFG_GCP_AIPLATFORM_DATASET` — Results for GCP aiplatform Dataset resource objects
- `LW_CFG_GCP_AIPLATFORM_DATASET_IAMPOLICY` — Results for GCP aiplatform Dataset iamPolicy objects
- `LW_CFG_GCP_AIPLATFORM_ENDPOINT` — Results for GCP aiplatform Endpoint resource objects
- `LW_CFG_GCP_AIPLATFORM_ENDPOINT_IAMPOLICY` — Results for GCP aiplatform Endpoint iamPolicy objects
- `LW_CFG_GCP_AIPLATFORM_HYPERPARAMETERTUNINGJOB` — Results for GCP aiplatform HyperparameterTuningJob resource objects
- `LW_CFG_GCP_AIPLATFORM_HYPERPARAMETERTUNINGJOB_IAMPOLICY` — Results for GCP aiplatform HyperparameterTuningJob iamPolicy objects
- `LW_CFG_GCP_AIPLATFORM_METADATASTORE` — Results for GCP aiplatform MetadataStore resource objects
- `LW_CFG_GCP_AIPLATFORM_METADATASTORE_IAMPOLICY` — Results for GCP aiplatform MetadataStore iamPolicy objects
- `LW_CFG_GCP_AIPLATFORM_MODEL` — Results for GCP aiplatform Model resource objects
- `LW_CFG_GCP_AIPLATFORM_MODELDEPLOYMENTMONITORINGJOB` — Results for GCP aiplatform ModelDeploymentMonitoringJob resource objects
- `LW_CFG_GCP_AIPLATFORM_MODELDEPLOYMENTMONITORINGJOB_IAMPOLICY` — Results for GCP aiplatform ModelDeploymentMonitoringJob iamPolicy objects
- `LW_CFG_GCP_AIPLATFORM_MODEL_IAMPOLICY` — Results for GCP aiplatform Model iamPolicy objects
- `LW_CFG_GCP_AIPLATFORM_PIPELINEJOB` — Results for GCP aiplatform PipelineJob resource objects
- `LW_CFG_GCP_AIPLATFORM_PIPELINEJOB_IAMPOLICY` — Results for GCP aiplatform PipelineJob iamPolicy objects
- `LW_CFG_GCP_AIPLATFORM_SPECIALISTPOOL` — Results for GCP aiplatform SpecialistPool resource objects
- `LW_CFG_GCP_AIPLATFORM_SPECIALISTPOOL_IAMPOLICY` — Results for GCP aiplatform SpecialistPool iamPolicy objects
- `LW_CFG_GCP_AIPLATFORM_TRAININGPIPELINE` — Results for GCP aiplatform TrainingPipeline resource objects
- `LW_CFG_GCP_AIPLATFORM_TRAININGPIPELINE_IAMPOLICY` — Results for GCP aiplatform TrainingPipeline iamPolicy objects

### All

- `LW_CFG_GCP_ALL` — Results from all GCP config data

### Anthos

- `LW_CFG_GCP_ANTHOS_CONNECTEDCLUSTER` — Results for GCP anthos ConnectedCluster resource objects
- `LW_CFG_GCP_ANTHOS_CONNECTEDCLUSTER_IAMPOLICY` — Results for GCP anthos ConnectedCluster iamPolicy objects

### API Gateway

- `LW_CFG_GCP_APIGATEWAY_API` — Results for GCP apigateway Api resource objects
- `LW_CFG_GCP_APIGATEWAY_APICONFIG` — Results for GCP apigateway ApiConfig resource objects
- `LW_CFG_GCP_APIGATEWAY_APICONFIG_IAMPOLICY` — Results for GCP apigateway ApiConfig iamPolicy objects
- `LW_CFG_GCP_APIGATEWAY_API_IAMPOLICY` — Results for GCP apigateway Api iamPolicy objects
- `LW_CFG_GCP_APIGATEWAY_GATEWAY` — Results for GCP apigateway Gateway resource objects
- `LW_CFG_GCP_APIGATEWAY_GATEWAY_IAMPOLICY` — Results for GCP apigateway Gateway iamPolicy objects

### API Keys

- `LW_CFG_GCP_APIKEYS_KEY` — Results for GCP apikeys Key resource objects
- `LW_CFG_GCP_APIKEYS_KEY_IAMPOLICY` — Results for GCP apikeys Key iamPolicy objects

### App Engine

- `LW_CFG_GCP_APPENGINE_APPLICATION` — Results for GCP appengine Application resource objects
- `LW_CFG_GCP_APPENGINE_APPLICATION_IAMPOLICY` — Results for GCP appengine Application iamPolicy objects
- `LW_CFG_GCP_APPENGINE_SERVICE` — Results for GCP appengine Service resource objects
- `LW_CFG_GCP_APPENGINE_SERVICE_IAMPOLICY` — Results for GCP appengine Service iamPolicy objects
- `LW_CFG_GCP_APPENGINE_VERSION` — Results for GCP appengine Version resource objects
- `LW_CFG_GCP_APPENGINE_VERSION_IAMPOLICY` — Results for GCP appengine Version iamPolicy objects

### Apps

- `LW_CFG_GCP_APPS_DEPLOYMENT` — Results for GCP apps Deployment resource objects
- `LW_CFG_GCP_APPS_DEPLOYMENT_IAMPOLICY` — Results for GCP apps Deployment iamPolicy objects

### Artifact Registry

- `LW_CFG_GCP_ARTIFACTREGISTRY_DOCKERIMAGE` — Results for GCP artifactregistry DockerImage resource objects
- `LW_CFG_GCP_ARTIFACTREGISTRY_DOCKERIMAGE_IAMPOLICY` — Results for GCP artifactregistry DockerImage iamPolicy objects
- `LW_CFG_GCP_ARTIFACTREGISTRY_REPOSITORY` — Results for GCP artifactregistry Repository resource objects
- `LW_CFG_GCP_ARTIFACTREGISTRY_REPOSITORY_IAMPOLICY` — Results for GCP artifactregistry Repository iamPolicy objects

### Assured Workloads

- `LW_CFG_GCP_ASSUREDWORKLOADS_WORKLOAD` — Results for GCP assuredworkloads Workload resource objects
- `LW_CFG_GCP_ASSUREDWORKLOADS_WORKLOAD_IAMPOLICY` — Results for GCP assuredworkloads Workload iamPolicy objects

### BigQuery

- `LW_CFG_GCP_BIGQUERY_DATASET` — Google Cloud bigquery Dataset resource objects
- `LW_CFG_GCP_BIGQUERY_DATASET_IAMPOLICY` — Google Cloud bigquery Dataset IAMPolicy objects (the corresponding access permissions for bigquery Dataset IAMPolicy)
- `LW_CFG_GCP_BIGQUERY_TABLE` — Google Cloud bigquery Table resource objects
- `LW_CFG_GCP_BIGQUERY_MODEL` — Results for GCP bigquery Model resource objects
- `LW_CFG_GCP_BIGQUERY_MODEL_IAMPOLICY` — Results for GCP bigquery Model iamPolicy objects
- `LW_CFG_GCP_BIGQUERY_TABLE_IAMPOLICY` — Results for GCP bigquery Table iamPolicy objects

### Bigtable Admin

- `LW_CFG_GCP_BIGTABLEADMIN_APPPROFILE` — Results for GCP bigtableadmin AppProfile resource objects
- `LW_CFG_GCP_BIGTABLEADMIN_APPPROFILE_IAMPOLICY` — Results for GCP bigtableadmin AppProfile iamPolicy objects
- `LW_CFG_GCP_BIGTABLEADMIN_BACKUP` — Results for GCP bigtableadmin Backup resource objects
- `LW_CFG_GCP_BIGTABLEADMIN_BACKUP_IAMPOLICY` — Results for GCP bigtableadmin Backup iamPolicy objects
- `LW_CFG_GCP_BIGTABLEADMIN_CLUSTER` — Results for GCP bigtableadmin Cluster resource objects
- `LW_CFG_GCP_BIGTABLEADMIN_CLUSTER_IAMPOLICY` — Results for GCP bigtableadmin Cluster iamPolicy objects
- `LW_CFG_GCP_BIGTABLEADMIN_INSTANCE` — Results for GCP bigtableadmin Instance resource objects
- `LW_CFG_GCP_BIGTABLEADMIN_INSTANCE_IAMPOLICY` — Results for GCP bigtableadmin Instance iamPolicy objects
- `LW_CFG_GCP_BIGTABLEADMIN_TABLE` — Results for GCP bigtableadmin Table resource objects
- `LW_CFG_GCP_BIGTABLEADMIN_TABLE_IAMPOLICY` — Results for GCP bigtableadmin Table iamPolicy objects

### Certificate Authority

- `LW_CFG_GCP_PRIVATECA_CAPOOL` — Results for GCP privateca CaPool resource objects
- `LW_CFG_GCP_PRIVATECA_CAPOOL_IAMPOLICY` — Results for GCP privateca CaPool iamPolicy objects
- `LW_CFG_GCP_PRIVATECA_CERTIFICATE` — Results for GCP privateca Certificate resource objects
- `LW_CFG_GCP_PRIVATECA_CERTIFICATEAUTHORITY` — Results for GCP privateca CertificateAuthority resource objects
- `LW_CFG_GCP_PRIVATECA_CERTIFICATEAUTHORITY_IAMPOLICY` — Results for GCP privateca CertificateAuthority iamPolicy objects
- `LW_CFG_GCP_PRIVATECA_CERTIFICATEREVOCATIONLIST` — Results for GCP privateca CertificateRevocationList resource objects
- `LW_CFG_GCP_PRIVATECA_CERTIFICATEREVOCATIONLIST_IAMPOLICY` — Results for GCP privateca CertificateRevocationList iamPolicy objects
- `LW_CFG_GCP_PRIVATECA_CERTIFICATETEMPLATE` — Results for GCP privateca CertificateTemplate resource objects
- `LW_CFG_GCP_PRIVATECA_CERTIFICATETEMPLATE_IAMPOLICY` — Results for GCP privateca CertificateTemplate iamPolicy objects
- `LW_CFG_GCP_PRIVATECA_CERTIFICATE_IAMPOLICY` — Results for GCP privateca Certificate iamPolicy objects

### Cloud Billing

- `LW_CFG_GCP_CLOUDBILLING_BILLINGACCOUNT` — Results for GCP cloudbilling BillingAccount resource objects
- `LW_CFG_GCP_CLOUDBILLING_BILLINGACCOUNT_IAMPOLICY` — Results for GCP cloudbilling BillingAccount iamPolicy objects
- `LW_CFG_GCP_CLOUDBILLING_PROJECTBILLINGINFO` — Results for GCP cloudbilling ProjectBillingInfo resource objects
- `LW_CFG_GCP_CLOUDBILLING_PROJECTBILLINGINFO_IAMPOLICY` — Results for GCP cloudbilling ProjectBillingInfo iamPolicy objects

### Cloud Functions

- `LW_CFG_GCP_CLOUDFUNCTIONS_CLOUDFUNCTION` — Results for GCP cloudfunctions CloudFunction resource objects
- `LW_CFG_GCP_CLOUDFUNCTIONS_CLOUDFUNCTION_IAMPOLICY` — Results for GCP cloudfunctions CloudFunction iamPolicy objects

### Cloud Key Management

- `LW_CFG_GCP_CLOUDKMS_CRYPTOKEY` — Google Cloud cloudkms CryptoKey resource objects
- `LW_CFG_GCP_CLOUDKMS_CRYPTOKEY_IAMPOLICY` — Results for GCP cloudkms CryptoKey iamPolicy objects
- `LW_CFG_GCP_CLOUDKMS_CRYPTOKEYVERSION` — Results for GCP cloudkms CryptoKeyVersion resource objects
- `LW_CFG_GCP_CLOUDKMS_CRYPTOKEYVERSION_IAMPOLICY` — Results for GCP cloudkms CryptoKeyVersion iamPolicy objects
- `LW_CFG_GCP_CLOUDKMS_EKMCONNECTION` — Results for GCP cloudkms EkmConnection resource objects
- `LW_CFG_GCP_CLOUDKMS_EKMCONNECTION_IAMPOLICY` — Results for GCP cloudkms EkmConnection iamPolicy objects
- `LW_CFG_GCP_CLOUDKMS_IMPORTJOB` — Results for GCP cloudkms ImportJob resource objects
- `LW_CFG_GCP_CLOUDKMS_IMPORTJOB_IAMPOLICY` — Results for GCP cloudkms ImportJob iamPolicy objects
- `LW_CFG_GCP_CLOUDKMS_KEYRING` — Results for GCP cloudkms KeyRing resource objects
- `LW_CFG_GCP_CLOUDKMS_KEYRING_IAMPOLICY` — Results for GCP cloudkms KeyRing iamPolicy objects

### Cloud Resource Manager

- `LW_CFG_GCP_CLOUDRESOURCEMANAGER_FOLDER_IAMPOLICY` — Google Cloud cloudresourcemanager Folder IAMPolicy objects (the corresponding access permissions for cloudresourcemanager Folder IAMPolicy)
- `LW_CFG_GCP_CLOUDRESOURCEMANAGER_ORGANIZATION_IAMPOLICY` — Google Cloud cloudresourcemanager Organization IAMPolicy objects (the corresponding access permissions for cloudresourcemanager Organization IAMPolicy)
- `LW_CFG_GCP_CLOUDRESOURCEMANAGER_PROJECT_IAMPOLICY` — Google Cloud cloudresourcemanager Project IAMPolicy objects (the corresponding access permissions for cloudresourcemanager Project IAMPolicy)
- `LW_CFG_GCP_CLOUDRESOURCEMANAGER_FOLDER` — Results for GCP cloudresourcemanager Folder resource objects
- `LW_CFG_GCP_CLOUDRESOURCEMANAGER_ORGANIZATION` — Results for GCP cloudresourcemanager Organization resource objects
- `LW_CFG_GCP_CLOUDRESOURCEMANAGER_PROJECT` — Results for GCP cloudresourcemanager Project resource objects
- `LW_CFG_GCP_CLOUDRESOURCEMANAGER_TAGBINDING` — Results for GCP cloudresourcemanager TagBinding resource objects
- `LW_CFG_GCP_CLOUDRESOURCEMANAGER_TAGBINDING_IAMPOLICY` — Results for GCP cloudresourcemanager TagBinding iamPolicy objects
- `LW_CFG_GCP_CLOUDRESOURCEMANAGER_TAGKEY` — Results for GCP cloudresourcemanager TagKey resource objects
- `LW_CFG_GCP_CLOUDRESOURCEMANAGER_TAGKEY_IAMPOLICY` — Results for GCP cloudresourcemanager TagKey iamPolicy objects
- `LW_CFG_GCP_CLOUDRESOURCEMANAGER_TAGVALUE` — Results for GCP cloudresourcemanager TagValue resource objects
- `LW_CFG_GCP_CLOUDRESOURCEMANAGER_TAGVALUE_IAMPOLICY` — Results for GCP cloudresourcemanager TagValue iamPolicy objects

### Composer

- `LW_CFG_GCP_COMPOSER_ENVIRONMENT` — Results for GCP composer Environment resource objects
- `LW_CFG_GCP_COMPOSER_ENVIRONMENT_IAMPOLICY` — Results for GCP composer Environment iamPolicy objects

### Compute Engine

- `LW_CFG_GCP_COMPUTE_DISK` — Google Cloud compute Disk resource objects
- `LW_CFG_GCP_COMPUTE_FIREWALL` — Google Cloud compute Firewall resource objects
- `LW_CFG_GCP_COMPUTE_INSTANCE` — Google Cloud compute Instance resource objects
- `LW_CFG_GCP_COMPUTE_NETWORK` — Google Cloud compute Network resource objects
- `LW_CFG_GCP_COMPUTE_SSLPOLICY` — Google Cloud compute SslPolicy resource objects
- `LW_CFG_GCP_COMPUTE_SUBNETWORK` — Google Cloud compute Subnetwork resource objects
- `LW_CFG_GCP_COMPUTE_TARGETHTTPSPROXY` — Google Cloud compute TargetHttpsProxy resource objects
- `LW_CFG_GCP_COMPUTE_TARGETSSLPROXY` — Google Cloud compute TargetSslProxy resource objects
- `LW_CFG_GCP_COMPUTE_ADDRESS` — Results for GCP compute Address resource objects
- `LW_CFG_GCP_COMPUTE_ADDRESS_IAMPOLICY` — Results for GCP compute Address iamPolicy objects
- `LW_CFG_GCP_COMPUTE_AUTOSCALER` — Results for GCP compute Autoscaler resource objects
- `LW_CFG_GCP_COMPUTE_AUTOSCALER_IAMPOLICY` — Results for GCP compute Autoscaler iamPolicy objects
- `LW_CFG_GCP_COMPUTE_BACKENDBUCKET` — Results for GCP compute BackendBucket resource objects
- `LW_CFG_GCP_COMPUTE_BACKENDBUCKET_IAMPOLICY` — Results for GCP compute BackendBucket iamPolicy objects
- `LW_CFG_GCP_COMPUTE_BACKENDSERVICE` — Results for GCP compute BackendService resource objects
- `LW_CFG_GCP_COMPUTE_BACKENDSERVICE_IAMPOLICY` — Results for GCP compute BackendService iamPolicy objects
- `LW_CFG_GCP_COMPUTE_COMMITMENT` — Results for GCP compute Commitment resource objects
- `LW_CFG_GCP_COMPUTE_COMMITMENT_IAMPOLICY` — Results for GCP compute Commitment iamPolicy objects
- `LW_CFG_GCP_COMPUTE_DISK_IAMPOLICY` — Results for GCP compute Disk iamPolicy objects
- `LW_CFG_GCP_COMPUTE_EXTERNALVPNGATEWAY` — Results for GCP compute ExternalVpnGateway resource objects
- `LW_CFG_GCP_COMPUTE_EXTERNALVPNGATEWAY_IAMPOLICY` — Results for GCP compute ExternalVpnGateway iamPolicy objects
- `LW_CFG_GCP_COMPUTE_FIREWALLPOLICY` — Results for GCP compute FirewallPolicy resource objects
- `LW_CFG_GCP_COMPUTE_FIREWALLPOLICY_IAMPOLICY` — Results for GCP compute FirewallPolicy iamPolicy objects
- `LW_CFG_GCP_COMPUTE_FIREWALL_IAMPOLICY` — Results for GCP compute Firewall iamPolicy objects
- `LW_CFG_GCP_COMPUTE_FORWARDINGRULE` — Results for GCP compute ForwardingRule resource objects
- `LW_CFG_GCP_COMPUTE_FORWARDINGRULE_IAMPOLICY` — Results for GCP compute ForwardingRule iamPolicy objects
- `LW_CFG_GCP_COMPUTE_GLOBALADDRESS` — Results for GCP compute GlobalAddress resource objects
- `LW_CFG_GCP_COMPUTE_GLOBALADDRESS_IAMPOLICY` — Results for GCP compute GlobalAddress iamPolicy objects
- `LW_CFG_GCP_COMPUTE_GLOBALFORWARDINGRULE` — Results for GCP compute GlobalForwardingRule resource objects
- `LW_CFG_GCP_COMPUTE_GLOBALFORWARDINGRULE_IAMPOLICY` — Results for GCP compute GlobalForwardingRule iamPolicy objects
- `LW_CFG_GCP_COMPUTE_HEALTHCHECK` — Results for GCP compute HealthCheck resource objects
- `LW_CFG_GCP_COMPUTE_HEALTHCHECK_IAMPOLICY` — Results for GCP compute HealthCheck iamPolicy objects
- `LW_CFG_GCP_COMPUTE_HTTPHEALTHCHECK` — Results for GCP compute HttpHealthCheck resource objects
- `LW_CFG_GCP_COMPUTE_HTTPHEALTHCHECK_IAMPOLICY` — Results for GCP compute HttpHealthCheck iamPolicy objects
- `LW_CFG_GCP_COMPUTE_HTTPSHEALTHCHECK` — Results for GCP compute HttpsHealthCheck resource objects
- `LW_CFG_GCP_COMPUTE_HTTPSHEALTHCHECK_IAMPOLICY` — Results for GCP compute HttpsHealthCheck iamPolicy objects
- `LW_CFG_GCP_COMPUTE_IMAGE` — Results for GCP compute Image resource objects
- `LW_CFG_GCP_COMPUTE_IMAGE_IAMPOLICY` — Results for GCP compute Image iamPolicy objects
- `LW_CFG_GCP_COMPUTE_INSTANCEGROUP` — Results for GCP compute InstanceGroup resource objects
- `LW_CFG_GCP_COMPUTE_INSTANCEGROUPMANAGER` — Results for GCP compute InstanceGroupManager resource objects
- `LW_CFG_GCP_COMPUTE_INSTANCEGROUPMANAGER_IAMPOLICY` — Results for GCP compute InstanceGroupManager iamPolicy objects
- `LW_CFG_GCP_COMPUTE_INSTANCEGROUP_IAMPOLICY` — Results for GCP compute InstanceGroup iamPolicy objects
- `LW_CFG_GCP_COMPUTE_INSTANCETEMPLATE` — Results for GCP compute InstanceTemplate resource objects
- `LW_CFG_GCP_COMPUTE_INSTANCETEMPLATE_IAMPOLICY` — Results for GCP compute InstanceTemplate iamPolicy objects
- `LW_CFG_GCP_COMPUTE_INSTANCE_IAMPOLICY` — Results for GCP compute Instance iamPolicy objects
- `LW_CFG_GCP_COMPUTE_INTERCONNECT` — Results for GCP compute Interconnect resource objects
- `LW_CFG_GCP_COMPUTE_INTERCONNECTATTACHMENT` — Results for GCP compute InterconnectAttachment resource objects
- `LW_CFG_GCP_COMPUTE_INTERCONNECTATTACHMENT_IAMPOLICY` — Results for GCP compute InterconnectAttachment iamPolicy objects
- `LW_CFG_GCP_COMPUTE_INTERCONNECT_IAMPOLICY` — Results for GCP compute Interconnect iamPolicy objects
- `LW_CFG_GCP_COMPUTE_LICENSE` — Results for GCP compute License resource objects
- `LW_CFG_GCP_COMPUTE_LICENSE_IAMPOLICY` — Results for GCP compute License iamPolicy objects
- `LW_CFG_GCP_COMPUTE_NETWORKENDPOINTGROUP` — Results for GCP compute NetworkEndpointGroup resource objects
- `LW_CFG_GCP_COMPUTE_NETWORKENDPOINTGROUP_IAMPOLICY` — Results for GCP compute NetworkEndpointGroup iamPolicy objects
- `LW_CFG_GCP_COMPUTE_NETWORK_IAMPOLICY` — Results for GCP compute Network iamPolicy objects
- `LW_CFG_GCP_COMPUTE_NODEGROUP` — Results for GCP compute NodeGroup resource objects
- `LW_CFG_GCP_COMPUTE_NODEGROUP_IAMPOLICY` — Results for GCP compute NodeGroup iamPolicy objects
- `LW_CFG_GCP_COMPUTE_NODETEMPLATE` — Results for GCP compute NodeTemplate resource objects
- `LW_CFG_GCP_COMPUTE_NODETEMPLATE_IAMPOLICY` — Results for GCP compute NodeTemplate iamPolicy objects
- `LW_CFG_GCP_COMPUTE_PACKETMIRRORING` — Results for GCP compute PacketMirroring resource objects
- `LW_CFG_GCP_COMPUTE_PACKETMIRRORING_IAMPOLICY` — Results for GCP compute PacketMirroring iamPolicy objects
- `LW_CFG_GCP_COMPUTE_PROJECT` — Results for GCP compute Project resource objects
- `LW_CFG_GCP_COMPUTE_PROJECT_IAMPOLICY` — Results for GCP compute Project iamPolicy objects
- `LW_CFG_GCP_COMPUTE_REGIONBACKENDSERVICE` — Results for GCP compute RegionBackendService resource objects
- `LW_CFG_GCP_COMPUTE_REGIONBACKENDSERVICE_IAMPOLICY` — Results for GCP compute RegionBackendService iamPolicy objects
- `LW_CFG_GCP_COMPUTE_REGIONDISK` — Results for GCP compute RegionDisk resource objects
- `LW_CFG_GCP_COMPUTE_REGIONDISK_IAMPOLICY` — Results for GCP compute RegionDisk iamPolicy objects
- `LW_CFG_GCP_COMPUTE_RESERVATION` — Results for GCP compute Reservation resource objects
- `LW_CFG_GCP_COMPUTE_RESERVATION_IAMPOLICY` — Results for GCP compute Reservation iamPolicy objects
- `LW_CFG_GCP_COMPUTE_RESOURCEPOLICY` — Results for GCP compute ResourcePolicy resource objects
- `LW_CFG_GCP_COMPUTE_RESOURCEPOLICY_IAMPOLICY` — Results for GCP compute ResourcePolicy iamPolicy objects
- `LW_CFG_GCP_COMPUTE_ROUTE` — Results for GCP compute Route resource objects
- `LW_CFG_GCP_COMPUTE_ROUTER` — Results for GCP compute Router resource objects
- `LW_CFG_GCP_COMPUTE_ROUTER_IAMPOLICY` — Results for GCP compute Router iamPolicy objects
- `LW_CFG_GCP_COMPUTE_ROUTE_IAMPOLICY` — Results for GCP compute Route iamPolicy objects
- `LW_CFG_GCP_COMPUTE_SECURITYPOLICY` — Results for GCP compute SecurityPolicy resource objects
- `LW_CFG_GCP_COMPUTE_SECURITYPOLICY_IAMPOLICY` — Results for GCP compute SecurityPolicy iamPolicy objects
- `LW_CFG_GCP_COMPUTE_SERVICEATTACHMENT` — Results for GCP compute ServiceAttachment resource objects
- `LW_CFG_GCP_COMPUTE_SERVICEATTACHMENT_IAMPOLICY` — Results for GCP compute ServiceAttachment iamPolicy objects
- `LW_CFG_GCP_COMPUTE_SNAPSHOT` — Results for GCP compute Snapshot resource objects
- `LW_CFG_GCP_COMPUTE_SNAPSHOT_IAMPOLICY` — Results for GCP compute Snapshot iamPolicy objects
- `LW_CFG_GCP_COMPUTE_SSLCERTIFICATE` — Results for GCP compute SslCertificate resource objects
- `LW_CFG_GCP_COMPUTE_SSLCERTIFICATE_IAMPOLICY` — Results for GCP compute SslCertificate iamPolicy objects
- `LW_CFG_GCP_COMPUTE_SSLPOLICY_IAMPOLICY` — Results for GCP compute SslPolicy iamPolicy objects
- `LW_CFG_GCP_COMPUTE_SUBNETWORK_IAMPOLICY` — Results for GCP compute Subnetwork iamPolicy objects
- `LW_CFG_GCP_COMPUTE_TARGETHTTPPROXY` — Results for GCP compute TargetHttpProxy resource objects
- `LW_CFG_GCP_COMPUTE_TARGETHTTPPROXY_IAMPOLICY` — Results for GCP compute TargetHttpProxy iamPolicy objects
- `LW_CFG_GCP_COMPUTE_TARGETHTTPSPROXY_IAMPOLICY` — Results for GCP compute TargetHttpsProxy iamPolicy objects
- `LW_CFG_GCP_COMPUTE_TARGETINSTANCE` — Results for GCP compute TargetInstance resource objects
- `LW_CFG_GCP_COMPUTE_TARGETINSTANCE_IAMPOLICY` — Results for GCP compute TargetInstance iamPolicy objects
- `LW_CFG_GCP_COMPUTE_TARGETPOOL` — Results for GCP compute TargetPool resource objects
- `LW_CFG_GCP_COMPUTE_TARGETPOOL_IAMPOLICY` — Results for GCP compute TargetPool iamPolicy objects
- `LW_CFG_GCP_COMPUTE_TARGETSSLPROXY_IAMPOLICY` — Results for GCP compute TargetSslProxy iamPolicy objects
- `LW_CFG_GCP_COMPUTE_TARGETTCPPROXY` — Results for GCP compute TargetTcpProxy resource objects
- `LW_CFG_GCP_COMPUTE_TARGETTCPPROXY_IAMPOLICY` — Results for GCP compute TargetTcpProxy iamPolicy objects
- `LW_CFG_GCP_COMPUTE_TARGETVPNGATEWAY` — Results for GCP compute TargetVpnGateway resource objects
- `LW_CFG_GCP_COMPUTE_TARGETVPNGATEWAY_IAMPOLICY` — Results for GCP compute TargetVpnGateway iamPolicy objects
- `LW_CFG_GCP_COMPUTE_URLMAP` — Results for GCP compute UrlMap resource objects
- `LW_CFG_GCP_COMPUTE_URLMAP_IAMPOLICY` — Results for GCP compute UrlMap iamPolicy objects
- `LW_CFG_GCP_COMPUTE_VPNGATEWAY` — Results for GCP compute VpnGateway resource objects
- `LW_CFG_GCP_COMPUTE_VPNGATEWAY_IAMPOLICY` — Results for GCP compute VpnGateway iamPolicy objects
- `LW_CFG_GCP_COMPUTE_VPNTUNNEL` — Results for GCP compute VpnTunnel resource objects
- `LW_CFG_GCP_COMPUTE_VPNTUNNEL_IAMPOLICY` — Results for GCP compute VpnTunnel iamPolicy objects

### Container

- `LW_CFG_GCP_CONTAINER_CLUSTER` — Results for GCP container Cluster resource objects
- `LW_CFG_GCP_CONTAINER_CLUSTER_IAMPOLICY` — Results for GCP container Cluster iamPolicy objects
- `LW_CFG_GCP_CONTAINER_NODEPOOL` — Results for GCP container NodePool resource objects
- `LW_CFG_GCP_CONTAINER_NODEPOOL_IAMPOLICY` — Results for GCP container NodePool iamPolicy objects

### Container Registry

- `LW_CFG_GCP_CONTAINERREGISTRY_IMAGE` — Results for GCP containerregistry Image resource objects
- `LW_CFG_GCP_CONTAINERREGISTRY_IMAGE_IAMPOLICY` — Results for GCP containerregistry Image iamPolicy objects

### Data Fusion

- `LW_CFG_GCP_DATAFUSION_INSTANCE` — Results for GCP datafusion Instance resource objects
- `LW_CFG_GCP_DATAFUSION_INSTANCE_IAMPOLICY` — Results for GCP datafusion Instance iamPolicy objects

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
