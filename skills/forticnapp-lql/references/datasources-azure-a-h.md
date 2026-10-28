<!-- Generated from FortiCNAPP 26.2 LQL Reference Guide (fetched 2026-10-28). Source:
     https://docs.fortinet.com/document/forticnapp/latest/lql-reference/771173/datasource-metadata -->

# Datasource Metadata

## Azure Configuration Datasources

### Azure Resource Graph Configuration Datasources

All Azure Resource Graph configuration datasources listed in this section have the same metadata available.

- `BATCH_START_TIME` (TIMESTAMP) — Beginning of time interval
- `BATCH_END_TIME` (TIMESTAMP) — End of time interval
- `QUERY_START_TIME` (TIMESTAMP) — Start time of query for this resource
- `QUERY_END_TIME` (TIMESTAMP) — End time of query for this resource
- `URN` (STRING) — URN of the resource.  This is a unique ID for the resource across all tenants/subscriptions.
- `API_KEY` (STRING) — Key describing the API used to fetch data for this resource
- `SERVICE` (STRING) — Service this resource belongs to
- `TENANT_ID` (STRING) — Azure Tenant ID
- `TENANT_NAME` (STRING) — Azure Tenant Name
- `SUBSCRIPTION_ID` (STRING) — Subscription ID
- `SUBSCRIPTION_NAME` (STRING) — Subscription Name
- `RESOURCE_GROUP` (STRING) — Group of this resource
- `RESOURCE_TYPE` (STRING) — Type of this resource
- `RESOURCE_ID` (STRING) — Identifier for this resource
- `RESOURCE_REGION` (STRING) — Region this resource belongs to
- `RESOURCE_CONFIG` (JSON) — JSON definition of this resource
- `RESOURCE_TAGS` (JSON) — Tags associated with this resource

### Azure Active Directory Configuration Datasources

All Azure Active Directory configuration datasources listed in this section have the same metadata available.

- `URN` (String) — URN of the resource
- `SERVICE` (String) — Service this resource belongs to
- `RESOURCE_TYPE` (String) — Type of this resource
- `RESOURCE_REGION` (String) — Region this resource belongs to
- `RESOURCE_CONFIG` (JSON) — JSON definition of this resource
- `RESOURCE_TAGS` (JSON) — Tags associated with this resource
- `RESOURCE_TYPE_VERSION` (String) — The Azure Cloud Solution Provider version of this resource
- `KEYS` (JSON) — Keys describing the tenant of this resource

> **Note:** For Users resource, FortiCNAPP ingests only the following attributes:   * `id` * `displayName` * `userPrincipalName` * `userType` * `passwordPolicies` * `onPremisesExtensionAttributes`   For Members resource, FortiCNAPP ingests only the following attributes:   * `id` * `displayName`

### AAD

- `LW_CFG_AZURE_AAD_DOMAINSERVICES` — `microsoft.aad/domainservices`  resource objects

### Active Directory

- `LW_CFG_AZURE_AZUREACTIVEDIRECTORY_B2CDIRECTORIES` — `microsoft.azureactivedirectory/b2cdirectories`  resource objects
- `LW_CFG_AZURE_AZUREACTIVEDIRECTORY_GUESTUSAGES` — `microsoft.azureactivedirectory/guestusages`  resource objects

### Administrative Unit

- `LW_CFG_AZURE_ADMINISTRATIVEUNIT` — Azure Administrative Unit resource objects

### Advisor

- `LW_CFG_AZURE_ADVISOR_CONFIGURATIONS` — Results for microsoft.advisor/configurations resource objects

### Alerts Management

- `LW_CFG_AZURE_ALERTSMANAGEMENT_ACTIONRULES` — `microsoft.alertsmanagement/actionrules`  resource objects
- `LW_CFG_AZURE_ALERTSMANAGEMENT_PROMETHEUSRULEGROUPS` — `microsoft.alertsmanagement/prometheusrulegroups`  resource objects
- `LW_CFG_AZURE_ALERTSMANAGEMENT_SMARTDETECTORALERTRULES` — `microsoft.alertsmanagement/smartdetectoralertrules`  resource objects

### All

- `LW_CFG_AZURE_ALL` — Results from all Azure config data

### Analysis Services

- `LW_CFG_AZURE_ANALYSISSERVICES_SERVERS` — `microsoft.analysisservices/servers`  resource objects

### API Management

- `LW_CFG_AZURE_APIMANAGEMENT_SERVICE` — `microsoft.apimanagement/service`  resource objects

### App

- `LW_CFG_AZURE_APP_CONTAINERAPPS` — `microsoft.app/containerapps`  resource objects
- `LW_CFG_AZURE_APP_MANAGEDENVIRONMENTS` — `microsoft.app/managedenvironments`  resource objects
- `LW_CFG_AZURE_APP_MANAGEDENVIRONMENTS_CERTIFICATES` — `microsoft.app/managedenvironments/certificates`  resource objects

### App Configuration

- `LW_CFG_AZURE_APPCONFIGURATION_CONFIGURATIONSTORES` — `microsoft.appconfiguration/configurationstores`  resource objects

### App Platform

- `LW_CFG_AZURE_APPPLATFORM_SPRING` — `microsoft.appplatform/spring`  resource objects

### App Role Assignment

- `LW_CFG_AZURE_APPROLEASSIGNMENT` — Azure App Role Assignment resource objects

### Application

- `LW_CFG_AZURE_APPLICATION` — Results for application resource objects

### ARC Data

- `LW_CFG_AZURE_AZUREARCDATA_SQLSERVERINSTANCES` — `microsoft.azurearcdata/sqlserverinstances`  resource objects

### Attestation

- `LW_CFG_AZURE_ATTESTATION_ATTESTATIONPROVIDERS` — `microsoft.attestation/attestationproviders`  resource objects

### Authorization

- `LW_CFG_AZURE_AUTHORIZATION_ROLEASSIGNMENTS` — `microsoft.authorization/roleassignments`  resource objects
- `LW_CFG_AZURE_AUTHORIZATION_ROLEDEFINITIONS` — `microsoft.authorization/roledefinitions`  resource objects
- `LW_CFG_AZURE_AUTHORIZATION_DENYASSIGNMENTS` — Results for microsoft.authorization/denyassignments resource objects

### Auto Manage

- `LW_CFG_AZURE_AUTOMANAGE_CONFIGURATIONPROFILES` — `microsoft.automanage/configurationprofiles`  resource objects

### Automation

- `LW_CFG_AZURE_AUTOMATION_AUTOMATIONACCOUNTS` — `microsoft.automation/automationaccounts`  resource objects
- `LW_CFG_AZURE_AUTOMATION_AUTOMATIONACCOUNTS_CONFIGURATIONS` — `microsoft.automation/automationaccounts/configurations`  resource objects
- `LW_CFG_AZURE_AUTOMATION_AUTOMATIONACCOUNTS_RUNBOOKS` — `microsoft.automation/automationaccounts/runbooks`  resource objects

### AVS

- `LW_CFG_AZURE_AVS_PRIVATECLOUDS` — `microsoft.avs/privateclouds`  resource objects

### Bare Metal

- `LW_CFG_AZURE_BAREMETAL_CONSOLECONNECTIONS` — `microsoft.baremetal/consoleconnections`  resource objects

### Batch

- `LW_CFG_AZURE_BATCH_BATCHACCOUNTS` — `microsoft.batch/batchaccounts`  resource objects

### Bing

- `LW_CFG_AZURE_BING_ACCOUNTS` — `microsoft.bing/accounts`  resource objects

### Bot Service

- `LW_CFG_AZURE_BOTSERVICE_BOTSERVICES` — `microsoft.botservice/botservices`  resource objects

### Cache

- `LW_CFG_AZURE_CACHE_REDIS` — `microsoft.cache/redis`  resource objects
- `LW_CFG_AZURE_CACHE_REDISENTERPRISE` — `microsoft.cache/redisenterprise`  resource objects

### CDN

- `LW_CFG_AZURE_CDN_PROFILES` — `microsoft.cdn/profiles`  resource objects
- `LW_CFG_AZURE_CDN_PROFILES_AFDENDPOINTS` — `microsoft.cdn/profiles/afdendpoints`  resource objects
- `LW_CFG_AZURE_CDN_PROFILES_CUSTOMDOMAINS` — Results for  `microsoft.cdn/profiles/customdomains`  resource objects
- `LW_CFG_AZURE_CDN_PROFILES_ENDPOINTS` — `microsoft.cdn/profiles/endpoints`  resource objects
- `LW_CFG_AZURE_CDN_PROFILES_ORIGINGROUPS` — `microsoft.cdn/profiles/origingroups`  resource objects

### Certificate Registration

- `LW_CFG_AZURE_CERTIFICATEREGISTRATION_CERTIFICATEORDERS` — `microsoft.certificateregistration/certificateorders`  resource objects

### Chaos

- `LW_CFG_AZURE_CHAOS_EXPERIMENTS` — Results for microsoft.chaos/experiments resource objects

### Classic Compute

- `LW_CFG_AZURE_CLASSICCOMPUTE_DOMAINNAMES` — `microsoft.classiccompute/domainnames`  resource objects
- `LW_CFG_AZURE_CLASSICCOMPUTE_VIRTUALMACHINES` — `microsoft.classiccompute/virtualmachines`  resource objects

### Classic Network

- `LW_CFG_AZURE_CLASSICNETWORK_NETWORKSECURITYGROUPS` — `microsoft.classicnetwork/networksecuritygroups`  resource objects
- `LW_CFG_AZURE_CLASSICNETWORK_RESERVEDIPS` — `microsoft.classicnetwork/reservedips`  resource objects
- `LW_CFG_AZURE_CLASSICNETWORK_VIRTUALNETWORKS` — `microsoft.classicnetwork/virtualnetworks`  resource objects

### Classic Storage

- `LW_CFG_AZURE_CLASSICSTORAGE_STORAGEACCOUNTS` — `microsoft.classicstorage/storageaccounts`  resource objects

### Code Signing

- `LW_CFG_AZURE_CODESIGNING_CODESIGNINGACCOUNTS` — `microsoft.codesigning/codesigningaccounts`  resource objects

### Cognitive Services

- `LW_CFG_AZURE_COGNITIVESERVICES_ACCOUNTS` — `microsoft.cognitiveservices/accounts`  resource objects

### Communication

- `LW_CFG_AZURE_COMMUNICATION_COMMUNICATIONSERVICES` — Results for microsoft.communication/communicationservices resource objects

### Compute

- `LW_CFG_AZURE_COMPUTE_AVAILABILITYSETS` — `microsoft.compute/availabilitysets`  resource objects
- `LW_CFG_AZURE_COMPUTE_CAPACITYRESERVATIONGROUPS` — `microsoft.compute/capacityreservationgroups`  resource objects
- `LW_CFG_AZURE_COMPUTE_CAPACITYRESERVATIONGROUPS_CAPACITYRESERVATIONS` — `microsoft.compute/capacityreservationgroups/ capacityreservations`  resource objects
- `LW_CFG_AZURE_COMPUTE_CAPACITYRESERVATIONS` — `microsoft.compute/capacityreservations`  resource objects
- `LW_CFG_AZURE_COMPUTE_CLOUDSERVICES` — `microsoft.compute/cloudservices`  resource objects
- `LW_CFG_AZURE_COMPUTE_DISKACCESSES` — `microsoft.compute/diskaccesses`  resource objects
- `LW_CFG_AZURE_COMPUTE_DISKENCRYPTIONSETS` — `microsoft.compute/diskencryptionsets`  resource objects
- `LW_CFG_AZURE_COMPUTE_DISKS` — `microsoft.compute/disks`  resource objects
- `LW_CFG_AZURE_COMPUTE_GALLERIES` — `microsoft.compute/galleries`  resource objects
- `LW_CFG_AZURE_COMPUTE_GALLERIES_APPLICATIONS` — `microsoft.compute/galleries/applications`  resource objects
- `LW_CFG_AZURE_COMPUTE_GALLERIES_APPLICATIONS_VERSIONS` — `microsoft.compute/galleries/ applications/versions`  resource objects
- `LW_CFG_AZURE_COMPUTE_GALLERIES_IMAGES` — `microsoft.compute/galleries/images`  resource objects
- `LW_CFG_AZURE_COMPUTE_GALLERIES_IMAGES_VERSIONS` — `microsoft.compute/galleries/images/versions`  resource objects
- `LW_CFG_AZURE_COMPUTE_HOSTGROUPS` — `microsoft.compute/hostgroups`  resource objects
- `LW_CFG_AZURE_COMPUTE_HOSTGROUPS_HOSTS` — `microsoft.compute/hostgroups/hosts`  resource objects
- `LW_CFG_AZURE_COMPUTE_IMAGES` — `microsoft.compute/images`  resource objects
- `LW_CFG_AZURE_COMPUTE_PROXIMITYPLACEMENTGROUPS` — `microsoft.compute/proximityplacementgroups`  resource objects
- `LW_CFG_AZURE_COMPUTE_RESTOREPOINTCOLLECTIONS` — `microsoft.compute/restorepointcollections`  resource objects
- `LW_CFG_AZURE_COMPUTE_SHAREDVMEXTENSIONS` — `microsoft.compute/sharedvmextensions`  resource objects
- `LW_CFG_AZURE_COMPUTE_SHAREDVMEXTENSIONS_VERSIONS` — `microsoft.compute/sharedvmextensions/versions`  resource objects
- `LW_CFG_AZURE_COMPUTE_SHAREDVMIMAGES` — `microsoft.compute/sharedvmimages`  resource objects
- `LW_CFG_AZURE_COMPUTE_SHAREDVMIMAGES_VERSIONS` — `microsoft.compute/sharedvmimages/versions`  resource objects
- `LW_CFG_AZURE_COMPUTE_SNAPSHOTS` — `microsoft.compute/snapshots`  resource objects
- `LW_CFG_AZURE_COMPUTE_SSHPUBLICKEYS` — `microsoft.compute/sshpublickeys`  resource objects
- `LW_CFG_AZURE_COMPUTE_SWIFTLETS` — `microsoft.compute/swiftlets`  resource objects
- `LW_CFG_AZURE_COMPUTE_VIRTUALMACHINES` — `microsoft.compute/virtualmachines`  resource objects
- `LW_CFG_AZURE_COMPUTE_VIRTUALMACHINESCALESETS` — `microsoft.compute/virtualmachinescalesets`  resource objects
- `LW_CFG_AZURE_COMPUTE_VIRTUALMACHINESCALESETS_VIRTUALMACHINES` — `microsoft.compute/virtualmachinescalesets/ virtualmachines`  resource objects
- `LW_CFG_AZURE_COMPUTE_VIRTUALMACHINESCALESETS_VIRTUALMACHINES_NETWORKINTERFACES_IPCONFIGURATIONS_PUBLICIPADDRESSES` — `microsoft.compute/virtualmachinescalesets/ virtualmachines/networkinterfaces/ ipconfigurations/publicipaddresses`  resource objects
- `LW_CFG_AZURE_COMPUTE_VIRTUALMACHINES_EXTENSIONS` — `microsoft.compute/virtualmachines/extensions`  resource objects
- `LW_CFG_AZURE_COMPUTE_VIRTUALMACHINES_RUNCOMMANDS` — `microsoft.compute/virtualmachines/runcommands`  resource objects

### Confidential Ledger

- `LW_CFG_AZURE_CONFIDENTIALLEDGER_LEDGERS` — `microsoft.confidentialledger/ledgers`  resource objects

### Confluent

- `LW_CFG_AZURE_CONFLUENT_ORGANIZATIONS` — `microsoft.confluent/organizations`  resource objects

### Connected VMware vSphere

- `LW_CFG_AZURE_CONNECTEDVMWAREVSPHERE_CLUSTERS` — `microsoft.connectedvmwarevsphere/clusters`  resource objects
- `LW_CFG_AZURE_CONNECTEDVMWAREVSPHERE_DATASTORES` — `microsoft.connectedvmwarevsphere/datastores`  resource objects
- `LW_CFG_AZURE_CONNECTEDVMWAREVSPHERE_VCENTERS` — `microsoft.connectedvmwarevsphere/vcenters`  resource objects
- `LW_CFG_AZURE_CONNECTEDVMWAREVSPHERE_VIRTUALMACHINETEMPLATES` — `microsoft.connectedvmwarevsphere/ virtualmachinetemplates`  resource objects
- `LW_CFG_AZURE_CONNECTEDVMWAREVSPHERE_HOSTS` — Results for microsoft.connectedvmwarevsphere/hosts resource objects
- `LW_CFG_AZURE_CONNECTEDVMWAREVSPHERE_VIRTUALNETWORKS` — Results for microsoft.connectedvmwarevsphere/virtualnetworks resource objects

### Container Instance

- `LW_CFG_AZURE_CONTAINERINSTANCE_CONTAINERGROUPS` — `microsoft.containerinstance/containergroups`  resource objects

### Container Registry

- `LW_CFG_AZURE_CONTAINERREGISTRY_REGISTRIES` — `microsoft.containerregistry/registries`  resource objects
- `LW_CFG_AZURE_CONTAINERREGISTRY_REGISTRIES_AGENTPOOLS` — `microsoft.containerregistry/registries/agentpools`  resource objects
- `LW_CFG_AZURE_CONTAINERREGISTRY_REGISTRIES_BUILDTASKS` — `microsoft.containerregistry/registries/buildtasks`  resource objects
- `LW_CFG_AZURE_CONTAINERREGISTRY_REGISTRIES_REPLICATIONS` — `microsoft.containerregistry/registries/replications`  resource objects
- `LW_CFG_AZURE_CONTAINERREGISTRY_REGISTRIES_TASKRUNS` — `microsoft.containerregistry/registries/taskruns`  resource objects
- `LW_CFG_AZURE_CONTAINERREGISTRY_REGISTRIES_TASKS` — `microsoft.containerregistry/registries/tasks`  resource objects
- `LW_CFG_AZURE_CONTAINERREGISTRY_REGISTRIES_WEBHOOKS` — `microsoft.containerregistry/registries/webhooks`  resource objects

### Container Service

- `LW_CFG_AZURE_CONTAINERSERVICE_CONTAINERSERVICES` — `microsoft.containerservice/containerservices`  resource objects
- `LW_CFG_AZURE_CONTAINERSERVICE_MANAGEDCLUSTERS` — `microsoft.containerservice/managedclusters`  resource objects
- `LW_CFG_AZURE_CONTAINERSERVICE_OPENSHIFTMANAGEDCLUSTERS` — `microsoft.containerservice/openshiftmanagedclusters`  resource objects
- `LW_CFG_AZURE_CONTAINERSERVICE_SNAPSHOTS` — `microsoft.containerservice/snapshots`  resource objects

### Cost Management

- `LW_CFG_AZURE_COSTMANAGEMENT_ALERTS` — Results for microsoft.costmanagement/alerts resource objects
- `LW_CFG_AZURE_COSTMANAGEMENT_BUDGETS` — Results for microsoft.costmanagement/budgets resource objects
- `LW_CFG_AZURE_COSTMANAGEMENT_EXPORTS` — Results for microsoft.costmanagement/exports resource objects

### Custom Providers

- `LW_CFG_AZURE_CUSTOMPROVIDERS_RESOURCEPROVIDERS` — `microsoft.customproviders/resourceproviders`  resource objects

### Dashboard

- `LW_CFG_AZURE_DASHBOARD_GRAFANA` — `microsoft.dashboard/grafana`  resource objects

### Data Box Edge

- `LW_CFG_AZURE_DATABOXEDGE_DATABOXEDGEDEVICES` — `microsoft.databoxedge/databoxedgedevices`  resource objects

### Data Bricks

- `LW_CFG_AZURE_DATABRICKS_WORKSPACES` — Results for  `microsoft.databricks/workspaces` resource objects
- `LW_CFG_AZURE_DATABRICKS_WORKSPACES_PRIVATEENDPOINTCONNECTIONS` — Results for  `microsoft.databricks/workspaces/ privateendpointconnections`  resource objects

### Data Factory

- `LW_CFG_AZURE_DATAFACTORY_FACTORIES` — `microsoft.datafactory/factories`  resource objects

### Data Migration

- `LW_CFG_AZURE_DATAMIGRATION_SERVICES` — `microsoft.datamigration/services`  resource objects
- `LW_CFG_AZURE_DATAMIGRATION_SERVICES_PROJECTS` — `microsoft.datamigration/services/projects`  resource objects
- `LW_CFG_AZURE_DATAMIGRATION_SQLMIGRATIONSERVICES` — `microsoft.datamigration/sqlmigrationservices`  resource objects

### Data Protection

- `LW_CFG_AZURE_DATAPROTECTION_BACKUPVAULTS` — `microsoft.dataprotection/backupvaults`  resource objects
- `LW_CFG_AZURE_DATAPROTECTION_RESOURCEGUARDS` — `microsoft.dataprotection/resourceguards`  resource objects

### Data Replication

- `LW_CFG_AZURE_DATAREPLICATION_REPLICATIONFABRICS` — `microsoft.datareplication/replicationfabrics`  resource objects
- `LW_CFG_AZURE_DATAREPLICATION_REPLICATIONVAULTS` — `microsoft.datareplication/replicationvaults`  resource objects

### Databox

- `LW_CFG_AZURE_DATABOX_JOBS` — `microsoft.databox/jobs`  resource objects

### Datadog

- `LW_CFG_AZURE_DATADOG_MONITORS` — `microsoft.datadog/monitors`  resource objects

### Datashare

- `LW_CFG_AZURE_DATASHARE_ACCOUNTS` — `microsoft.datashare/accounts`  resource objects

### DB for MariaDB

- `LW_CFG_AZURE_DBFORMARIADB_SERVERS` — `microsoft.dbformariadb/servers`  resource objects

### DB for MySQL

- `LW_CFG_AZURE_DBFORMYSQL_FLEXIBLESERVERS` — `microsoft.dbformysql/flexibleservers`  resource objects
- `LW_CFG_AZURE_DBFORMYSQL_FLEXIBLESERVERS_CONFIGURATIONS` — `microsoft.dbformysql/flexibleservers/configurations`  resource objects
- `LW_CFG_AZURE_DBFORMYSQL_FLEXIBLESERVERS_FIREWALLRULES` — `microsoft.dbformysql/flexibleservers/firewallrules`  resource objects
- `LW_CFG_AZURE_DBFORMYSQL_SERVERS` — `microsoft.dbformysql/servers`  resource objects
- `LW_CFG_AZURE_DBFORMYSQL_SERVERS_FIREWALLRULES` — `microsoft.dbformysql/servers/firewallrules`  resource objects

### DB for PostgreSQL

- `LW_CFG_AZURE_DBFORPOSTGRESQL_FLEXIBLESERVERS` — `microsoft.dbforpostgresql/flexibleservers`  resource objects
- `LW_CFG_AZURE_DBFORPOSTGRESQL_FLEXIBLESERVERS_CONFIGURATIONS` — `microsoft.dbforpostgresql/flexibleservers/configurations`  resource objects
- `LW_CFG_AZURE_DBFORPOSTGRESQL_FLEXIBLESERVERS_FIREWALLRULES` — `microsoft.dbforpostgresql/flexibleservers/firewallrules`  resource objects
- `LW_CFG_AZURE_DBFORPOSTGRESQL_SERVERGROUPS` — `microsoft.dbforpostgresql/servergroups`  resource objects
- `LW_CFG_AZURE_DBFORPOSTGRESQL_SERVERGROUPSV2` — `microsoft.dbforpostgresql/servergroupsv2`  resource objects
- `LW_CFG_AZURE_DBFORPOSTGRESQL_SERVERS` — `microsoft.dbforpostgresql/servers`  resource objects
- `LW_CFG_AZURE_DBFORPOSTGRESQL_SERVERSV2` — `microsoft.dbforpostgresql/serversv2`  resource objects
- `LW_CFG_AZURE_DBFORPOSTGRESQL_SERVERS_CONFIGURATIONS` — `microsoft.dbforpostgresql/servers/configurations`  resource objects
- `LW_CFG_AZURE_DBFORPOSTGRESQL_SERVERS_FIREWALLRULES` — `microsoft.dbforpostgresql/servers/firewallrules`  resource objects
- `LW_CFG_AZURE_DBFORPOSTGRESQL_SINGLESERVERS` — `microsoft.dbforpostgresql/singleservers`  resource objects

### Desktop Virtualization

- `LW_CFG_AZURE_DESKTOPVIRTUALIZATION_APPLICATIONGROUPS` — `microsoft.desktopvirtualization/applicationgroups`  resource objects
- `LW_CFG_AZURE_DESKTOPVIRTUALIZATION_HOSTPOOLS` — `microsoft.desktopvirtualization/hostpools`  resource objects
- `LW_CFG_AZURE_DESKTOPVIRTUALIZATION_SCALINGPLANS` — `microsoft.desktopvirtualization/scalingplans`  resource objects
- `LW_CFG_AZURE_DESKTOPVIRTUALIZATION_WORKSPACES` — `microsoft.desktopvirtualization/workspaces`  resource objects

### Device Update

- `LW_CFG_AZURE_DEVICEUPDATE_ACCOUNTS` — `microsoft.deviceupdate/accounts`  resource objects
- `LW_CFG_AZURE_DEVICEUPDATE_ACCOUNTS_INSTANCES` — `microsoft.deviceupdate/accounts/instances`  resource objects

### Devices

- `LW_CFG_AZURE_DEVICES_IOTHUBS` — `microsoft.devices/iothubs`  resource objects
- `LW_CFG_AZURE_DEVICES_PROVISIONINGSERVICES` — `microsoft.devices/provisioningservices`  resource objects

### Devops

- `LW_CFG_AZURE_DEVOPS_PIPELINES` — `microsoft.devops/pipelines`  resource objects

### DevTest Lab

- `LW_CFG_AZURE_DEVTESTLAB_LABS` — `microsoft.devtestlab/labs`  resource objects
- `LW_CFG_AZURE_DEVTESTLAB_LABS_VIRTUALMACHINES` — `microsoft.devtestlab/labs/virtualmachines`  resource objects
- `LW_CFG_AZURE_DEVTESTLAB_SCHEDULES` — `microsoft.devtestlab/schedules`  resource objects

### Digital Twins

- `LW_CFG_AZURE_DIGITALTWINS_DIGITALTWINSINSTANCES` — Results for microsoft.digitaltwins/digitaltwinsinstances resource objects

### Directory Role

- `LW_CFG_AZURE_DIRECTORYROLE` — Azure Directory Role resource objects

### DocumentDB

- `LW_CFG_AZURE_DOCUMENTDB_CASSANDRACLUSTERS` — `microsoft.documentdb/cassandraclusters`  resource objects
- `LW_CFG_AZURE_DOCUMENTDB_DATABASEACCOUNTS` — `microsoft.documentdb/databaseaccounts`  resource objects
- `LW_CFG_AZURE_DOCUMENTDB_DATABASEACCOUNTS_PRIVATEENDPOINTCONNECTIONS` — Results for  `microsoft.documentdb/databaseaccounts/privateendpointconnections` resource objects

### DocumentDB (CosmoDB)

- `LW_CFG_AZURE_COSMOSDB_ACCOUNTS` — `microsoft.documentdb/databaseaccounts`  resource objects

### Domain

- `LW_CFG_AZURE_DOMAIN` — Azure Domain resource objects

### DomainRegistration

- `LW_CFG_AZURE_DOMAINREGISTRATION_DOMAINS` — `microsoft.domainregistration/domains`  resource objects

### Dynatrace observability

| LW_CFG_AZURE_DYNATRACE.OBSERVABILITY_MONITORS | Results for dynatrace.observability/monitors resource objects |

### Edge Order

- `LW_CFG_AZURE_EDGEORDER_ADDRESSES` — `microsoft.edgeorder/addresses`  resource objects
- `LW_CFG_AZURE_EDGEORDER_ORDERITEMS` — Results for microsoft.edgeorder/orderitems resource objects

### Elastic

- `LW_CFG_AZURE_ELASTIC_MONITORS` — `microsoft.elastic/monitors`  resource objects

### ElasticSan

- `LW_CFG_AZURE_ELASTICSAN_ELASTICSANS` — `microsoft.elasticsan/elasticsans`  resource objects
- `LW_CFG_AZURE_ELASTICSAN_ELASTICSANS_VOLUMEGROUPS` — `microsoft.elasticsan/elasticsans/volumegroups`  resource objects

### Event Grid

- `LW_CFG_AZURE_EVENTGRID_DOMAINS` — `microsoft.eventgrid/domains`  resource objects
- `LW_CFG_AZURE_EVENTGRID_PARTNERTOPICS` — `microsoft.eventgrid/partnertopics`  resource objects
- `LW_CFG_AZURE_EVENTGRID_SYSTEMTOPICS` — `microsoft.eventgrid/systemtopics`  resource objects
- `LW_CFG_AZURE_EVENTGRID_TOPICS` — `microsoft.eventgrid/topics`  resource objects
- `LW_CFG_AZURE_EVENTGRID_PARTNERREGISTRATIONS` — Results for microsoft.eventgrid/partnerregistrations resource objects

### Event Hub

- `LW_CFG_AZURE_EVENTHUB_NAMESPACES` — `microsoft.eventhub/namespaces`  resource objects
- `LW_CFG_AZURE_EVENTHUB_CLUSTERS` — Results for microsoft.eventhub/clusters resource objects

### Extended Location

- `LW_CFG_AZURE_EXTENDEDLOCATION_CUSTOMLOCATIONS` — `microsoft.extendedlocation/customlocations`  resource objects

### Group

- `LW_CFG_AZURE_GROUP` — Azure Group resource objects

### Group Member

- `LW_CFG_AZURE_GROUP_MEMBER` — Azure Group Member resource objects

### Group Owner

- `LW_CFG_AZURE_GROUP_OWNER` — Azure Group Owner resource objects

### Hardware Security Modules

- `LW_CFG_AZURE_HARDWARESECURITYMODULES_DEDICATEDHSMS` — Results for microsoft.hardwaresecuritymodules/dedicatedhsms resource objects

### HD Insight

- `LW_CFG_AZURE_HDINSIGHT_CLUSTERS` — `microsoft.hdinsight/clusters`  resource objects

### Healthcare APIs

- `LW_CFG_AZURE_HEALTHCAREAPIS_WORKSPACES` — `microsoft.healthcareapis/workspaces`  resource objects
- `LW_CFG_AZURE_HEALTHCAREAPIS_WORKSPACES_DICOMSERVICES` — `microsoft.healthcareapis/workspaces/dicomservices`  resource objects
- `LW_CFG_AZURE_HEALTHCAREAPIS_WORKSPACES_FHIRSERVICES` — `microsoft.healthcareapis/workspaces/fhirservices`  resource objects

### Hybrid Compute

- `LW_CFG_AZURE_HYBRIDCOMPUTE_MACHINES` — `microsoft.hybridcompute/machines`  resource objects
- `LW_CFG_AZURE_HYBRIDCOMPUTE_MACHINES_EXTENSIONS` — `microsoft.hybridcompute/machines/extensions`  resource objects
- `LW_CFG_AZURE_HYBRIDCOMPUTE_PRIVATELINKSCOPES` — `microsoft.hybridcompute/privatelinkscopes`  resource objects

### Hybrid Network

- `LW_CFG_AZURE_HYBRIDNETWORK_DEVICES` — Results for microsoft.hybridnetwork/devices resource objects
- `LW_CFG_AZURE_HYBRIDNETWORK_PUBLISHERS` — Results for microsoft.hybridnetwork/publishers resource objects
