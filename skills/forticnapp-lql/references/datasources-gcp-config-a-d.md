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
