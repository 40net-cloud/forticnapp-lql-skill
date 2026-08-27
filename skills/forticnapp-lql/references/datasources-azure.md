<!-- Generated from FortiCNAPP 26.2 LQL Reference Guide (fetched 2026-08-26). Source:
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

### Insights

- `LW_CFG_AZURE_INSIGHTS_ACTIONGROUPS` — `microsoft.insights/actiongroups`  resource objects
- `LW_CFG_AZURE_INSIGHTS_ACTIVITYLOGALERTS` — `microsoft.insights/activitylogalerts`  resource objects
- `LW_CFG_AZURE_INSIGHTS_ALERTRULES` — `microsoft.insights/alertrules`  resource objects
- `LW_CFG_AZURE_INSIGHTS_AUTOSCALESETTINGS` — `microsoft.insights/autoscalesettings`  resource objects
- `LW_CFG_AZURE_INSIGHTS_COMPONENTS` — `microsoft.insights/components`  resource objects
- `LW_CFG_AZURE_INSIGHTS_DATACOLLECTIONENDPOINTS` — `microsoft.insights/datacollectionendpoints`  resource objects
- `LW_CFG_AZURE_INSIGHTS_DATACOLLECTIONRULES` — `microsoft.insights/datacollectionrules`  resource objects
- `LW_CFG_AZURE_INSIGHTS_DIAGNOSTICSETTINGS` — `microsoft.insights/diagnosticsettings`  resource objects
- `LW_CFG_AZURE_INSIGHTS_GUESTDIAGNOSTICSETTINGS` — `microsoft.insights/guestdiagnosticsettings`  resource objects
- `LW_CFG_AZURE_INSIGHTS_METRICALERTS` — `microsoft.insights/metricalerts`  resource objects
- `LW_CFG_AZURE_INSIGHTS_NOTIFICATIONGROUPS` — `microsoft.insights/notificationgroups`  resource objects
- `LW_CFG_AZURE_INSIGHTS_NOTIFICATIONRULES` — `microsoft.insights/notificationrules`  resource objects
- `LW_CFG_AZURE_INSIGHTS_PRIVATELINKSCOPES` — `microsoft.insights/privatelinkscopes`  resource objects
- `LW_CFG_AZURE_INSIGHTS_QUERYPACKS` — `microsoft.insights/querypacks`  resource objects
- `LW_CFG_AZURE_INSIGHTS_SCHEDULEDQUERYRULES` — `microsoft.insights/scheduledqueryrules`  resource objects
- `LW_CFG_AZURE_INSIGHTS_WEBTESTS` — `microsoft.insights/webtests`  resource objects
- `LW_CFG_AZURE_INSIGHTS_WORKBOOKS` — `microsoft.insights/workbooks`  resource objects
- `LW_CFG_AZURE_INSIGHTS_WORKBOOKTEMPLATES` — `microsoft.insights/workbooktemplates`  resource objects

### IoT Central

- `LW_CFG_AZURE_IOTCENTRAL_IOTAPPS` — Results for microsoft.iotcentral/iotapps resource objects

### Keyvault

- `LW_CFG_AZURE_KEYVAULT_HSMPOOLS` — `microsoft.keyvault/hsmpools`  resource objects
- `LW_CFG_AZURE_KEYVAULT_MANAGEDHSMS` — `microsoft.keyvault/managedhsms`  resource objects
- `LW_CFG_AZURE_KEYVAULT_VAULTS` — `microsoft.keyvault/vaults`  resource objects
- `LW_CFG_AZURE_KEYVAULT_VAULTS_KEYS` — `microsoft.keyvault/vaults/keys`  resource objects
- `LW_CFG_AZURE_KEYVAULT_VAULTS_PRIVATEENDPOINTCONNECTIONS` — Results for  `microsoft.keyvault/vaults/privateendpointconnections`  resource objects
- `LW_CFG_AZURE_KEYVAULT_VAULTS_SECRETS` — `microsoft.keyvault/vaults/secrets`  resource objects

### Kubernetes

- `LW_CFG_AZURE_KUBERNETES_CONNECTEDCLUSTERS` — `microsoft.kubernetes/connectedclusters`  resource objects

### Kubernetes Clusters

- `LW_CFG_AZURE_KUBERNETESCLUSTERS` — Results for kubernetesClusters resource objects

### Kubernetes Configuration

- `LW_CFG_AZURE_KUBERNETESCONFIGURATION_EXTENSIONS` — Results for microsoft.kubernetesconfiguration/extensions resource objects
- `LW_CFG_AZURE_KUBERNETESCONFIGURATION_FLUXCONFIGURATIONS` — Results for microsoft.kubernetesconfiguration/fluxconfigurations resource objects
- `LW_CFG_AZURE_KUBERNETESCONFIGURATION_PRIVATELINKSCOPES` — Results for microsoft.kubernetesconfiguration/privatelinkscopes resource objects

### Kusto

- `LW_CFG_AZURE_KUSTO_CLUSTERS` — `microsoft.kusto/clusters`  resource objects

### Lab Services

- `LW_CFG_AZURE_LABSERVICES_LABPLANS` — `microsoft.labservices/labplans`  resource objects
- `LW_CFG_AZURE_LABSERVICES_LABS` — `microsoft.labservices/labs`  resource objects

### Loadtest Service

- `LW_CFG_AZURE_LOADTESTSERVICE_LOADTESTS` — `microsoft.loadtestservice/loadtests`  resource objects

### Location

- `LW_CFG_AZURE_LOCATION` — Results for location resource objects

### Logic

- `LW_CFG_AZURE_LOGIC_INTEGRATIONACCOUNTS` — `microsoft.logic/integrationaccounts`  resource objects
- `LW_CFG_AZURE_LOGIC_WORKFLOWS` — `microsoft.logic/workflows`  resource objects

### Machine Learning Services

- `LW_CFG_AZURE_MACHINELEARNINGSERVICES_WORKSPACES` — `microsoft.machinelearningservices/workspaces`  resource objects
- `LW_CFG_AZURE_MACHINELEARNINGSERVICES_WORKSPACES_BATCHENDPOINTS` — `microsoft.machinelearningservices/workspaces/ batchendpoints`  resource objects
- `LW_CFG_AZURE_MACHINELEARNINGSERVICES_WORKSPACES_BATCHENDPOINTS_DEPLOYMENTS` — `microsoft.machinelearningservices/workspaces/ batchendpoints/deployments`  resource objects
- `LW_CFG_AZURE_MACHINELEARNINGSERVICES_WORKSPACES_ONLINEENDPOINTS` — `microsoft.machinelearningservices/workspaces/ onlineendpoints`  resource objects
- `LW_CFG_AZURE_MACHINELEARNINGSERVICES_WORKSPACES_ONLINEENDPOINTS_DEPLOYMENTS` — `microsoft.machinelearningservices/workspaces/ onlineendpoints/deployments`  resource objects

### Maintenance

- `LW_CFG_AZURE_MAINTENANCE_MAINTENANCECONFIGURATIONS` — `microsoft.maintenance/maintenanceconfigurations`  resource objects

### Managed Identity

- `LW_CFG_AZURE_MANAGEDIDENTITY_USERASSIGNEDIDENTITIES` — `microsoft.managedidentity/userassignedidentities`  resource objects

### Maps

- `LW_CFG_AZURE_MAPS_ACCOUNTS` — `microsoft.maps/accounts`  resource objects

### Media

- `LW_CFG_AZURE_MEDIA_MEDIASERVICES` — `microsoft.media/mediaservices`  resource objects
- `LW_CFG_AZURE_MEDIA_MEDIASERVICES_LIVEEVENTS` — `microsoft.media/mediaservices/liveevents`  resource objects
- `LW_CFG_AZURE_MEDIA_MEDIASERVICES_STREAMINGENDPOINTS` — `microsoft.media/mediaservices/streamingendpoints`  resource objects

### Migrate

- `LW_CFG_AZURE_MIGRATE_ASSESSMENTPROJECTS` — `microsoft.migrate/assessmentprojects`  resource objects
- `LW_CFG_AZURE_MIGRATE_MIGRATEPROJECTS` — `microsoft.migrate/migrateprojects`  resource objects
- `LW_CFG_AZURE_MIGRATE_MOVECOLLECTIONS` — `microsoft.migrate/movecollections`  resource objects

### Monitor

- `LW_CFG_AZURE_MONITOR_ACCOUNTS` — `microsoft.monitor/accounts`  resource objects

### NetApp

- `LW_CFG_AZURE_NETAPP_NETAPPACCOUNTS` — `microsoft.netapp/netappaccounts`  resource objects
- `LW_CFG_AZURE_NETAPP_NETAPPACCOUNTS_BACKUPPOLICIES` — `microsoft.netapp/netappaccounts/backuppolicies`  resource objects
- `LW_CFG_AZURE_NETAPP_NETAPPACCOUNTS_CAPACITYPOOLS` — `microsoft.netapp/netappaccounts/capacitypools`  resource objects
- `LW_CFG_AZURE_NETAPP_NETAPPACCOUNTS_CAPACITYPOOLS_VOLUMES` — `microsoft.netapp/netappaccounts/capacitypools/volumes`  resource objects
- `LW_CFG_AZURE_NETAPP_NETAPPACCOUNTS_SNAPSHOTPOLICIES` — `microsoft.netapp/netappaccounts/snapshotpolicies`  resource objects

### Network

- `LW_CFG_AZURE_NETWORK_APPLICATIONGATEWAYS` — `microsoft.network/applicationgateways`  resource objects
- `LW_CFG_AZURE_NETWORK_APPLICATIONGATEWAYWEBAPPLICATIONFIREWALLPOLICIES` — `microsoft.network/applicationgateway webapplicationfirewallpolicies`  resource objects
- `LW_CFG_AZURE_NETWORK_APPLICATIONSECURITYGROUPS` — `microsoft.network/applicationsecuritygroups`  resource objects
- `LW_CFG_AZURE_NETWORK_AZUREFIREWALLS` — `microsoft.network/azurefirewalls`  resource objects
- `LW_CFG_AZURE_NETWORK_BASTIONHOSTS` — `microsoft.network/bastionhosts`  resource objects
- `LW_CFG_AZURE_NETWORK_CONNECTIONS` — `microsoft.network/connections`  resource objects
- `LW_CFG_AZURE_NETWORK_CUSTOMIPPREFIXES` — `microsoft.network/customipprefixes`  resource objects
- `LW_CFG_AZURE_NETWORK_DDOSCUSTOMPOLICIES` — `microsoft.network/ddoscustompolicies`  resource objects
- `LW_CFG_AZURE_NETWORK_DDOSPROTECTIONPLANS` — `microsoft.network/ddosprotectionplans`  resource objects
- `LW_CFG_AZURE_NETWORK_DNSFORWARDINGRULESETS` — `microsoft.network/dnsforwardingrulesets`  resource objects
- `LW_CFG_AZURE_NETWORK_DNSRESOLVERS` — `microsoft.network/dnsresolvers`  resource objects
- `LW_CFG_AZURE_NETWORK_DNSRESOLVERS_INBOUNDENDPOINTS` — `microsoft.network/dnsresolvers/inboundendpoints`  resource objects
- `LW_CFG_AZURE_NETWORK_DNSRESOLVERS_OUTBOUNDENDPOINTS` — `microsoft.network/dnsresolvers/outboundendpoints`  resource objects
- `LW_CFG_AZURE_NETWORK_DNSZONES` — `microsoft.network/dnszones`  resource objects
- `LW_CFG_AZURE_NETWORK_DSCPCONFIGURATIONS` — `microsoft.network/dscpconfigurations`  resource objects
- `LW_CFG_AZURE_NETWORK_EXPRESSROUTECIRCUITS` — `microsoft.network/expressroutecircuits`  resource objects
- `LW_CFG_AZURE_NETWORK_EXPRESSROUTECROSSCONNECTIONS` — `microsoft.network/expressroutecrossconnections`  resource objects
- `LW_CFG_AZURE_NETWORK_EXPRESSROUTEGATEWAYS` — `microsoft.network/expressroutegateways`  resource objects
- `LW_CFG_AZURE_NETWORK_EXPRESSROUTEPORTS` — `microsoft.network/expressrouteports`  resource objects
- `LW_CFG_AZURE_NETWORK_FIREWALLPOLICIES` — `microsoft.network/firewallpolicies`  resource objects
- `LW_CFG_AZURE_NETWORK_FIREWALLPOLICIES_RULEGROUPS` — `microsoft.network/firewallpolicies/rulegroups`  resource objects
- `LW_CFG_AZURE_NETWORK_FRONTDOORS` — `microsoft.network/frontdoors`  resource objects
- `LW_CFG_AZURE_NETWORK_FRONTDOORWEBAPPLICATIONFIREWALLPOLICIES` — `microsoft.network/ frontdoorwebapplicationfirewallpolicies`  resource objects
- `LW_CFG_AZURE_NETWORK_IPALLOCATIONS` — `microsoft.network/ipallocations`  resource objects
- `LW_CFG_AZURE_NETWORK_IPGROUPS` — `microsoft.network/ipgroups`  resource objects
- `LW_CFG_AZURE_NETWORK_LOADBALANCERS` — `microsoft.network/loadbalancers`  resource objects
- `LW_CFG_AZURE_NETWORK_LOCALNETWORKGATEWAYS` — `microsoft.network/localnetworkgateways`  resource objects
- `LW_CFG_AZURE_NETWORK_MASTERCUSTOMIPPREFIXES` — `microsoft.network/mastercustomipprefixes`  resource objects
- `LW_CFG_AZURE_NETWORK_NATGATEWAYS` — `microsoft.network/natgateways`  resource objects
- `LW_CFG_AZURE_NETWORK_NETWORKEXPERIMENTPROFILES` — `microsoft.network/networkexperimentprofiles`  resource objects
- `LW_CFG_AZURE_NETWORK_NETWORKINTENTPOLICIES` — `microsoft.network/networkintentpolicies`  resource objects
- `LW_CFG_AZURE_NETWORK_NETWORKINTERFACES` — `microsoft.network/networkinterfaces`  resource objects
- `LW_CFG_AZURE_NETWORK_NETWORKMANAGERS` — `microsoft.network/networkmanagers`  resource objects
- `LW_CFG_AZURE_NETWORK_NETWORKPROFILES` — `microsoft.network/networkprofiles`  resource objects
- `LW_CFG_AZURE_NETWORK_NETWORKSECURITYGROUPS` — `microsoft.network/networksecuritygroups`  resource objects
- `LW_CFG_AZURE_NETWORK_NETWORKSECURITYPERIMETERS` — `microsoft.network/networksecurityperimeters`  resource objects
- `LW_CFG_AZURE_NETWORK_NETWORKVIRTUALAPPLIANCES` — `microsoft.network/networkvirtualappliances`  resource objects
- `LW_CFG_AZURE_NETWORK_NETWORKWATCHERS` — `microsoft.network/networkwatchers`  resource objects
- `LW_CFG_AZURE_NETWORK_NETWORKWATCHERS_CONNECTIONMONITORS` — `microsoft.network/networkwatchers/connectionmonitors`  resource objects
- `LW_CFG_AZURE_NETWORK_NETWORKWATCHERS_FLOWLOGS` — `microsoft.network/networkwatchers/flowlogs`  resource objects
- `LW_CFG_AZURE_NETWORK_NETWORKWATCHERS_LENSES` — `microsoft.network/networkwatchers/lenses`  resource objects
- `LW_CFG_AZURE_NETWORK_NETWORKWATCHERS_PINGMESHES` — `microsoft.network/networkwatchers/pingmeshes`  resource objects
- `LW_CFG_AZURE_NETWORK_P2SVPNGATEWAYS` — `microsoft.network/p2svpngateways`  resource objects
- `LW_CFG_AZURE_NETWORK_PRIVATEDNSZONES` — `microsoft.network/privatednszones`  resource objects
- `LW_CFG_AZURE_NETWORK_PRIVATEDNSZONES_VIRTUALNETWORKLINKS` — `microsoft.network/privatednszones/virtualnetworklinks`  resource objects
- `LW_CFG_AZURE_NETWORK_PRIVATEENDPOINTREDIRECTMAPS` — `microsoft.network/privateendpointredirectmaps`  resource objects
- `LW_CFG_AZURE_NETWORK_PRIVATEENDPOINTS` — `microsoft.network/privateendpoints`  resource objects
- `LW_CFG_AZURE_NETWORK_PRIVATELINKSERVICES` — `microsoft.network/privatelinkservices`  resource objects
- `LW_CFG_AZURE_NETWORK_PUBLICIPADDRESSES` — `microsoft.network/publicipaddresses`  resource objects
- `LW_CFG_AZURE_NETWORK_PUBLICIPPREFIXES` — `microsoft.network/publicipprefixes`  resource objects
- `LW_CFG_AZURE_NETWORK_ROUTEFILTERS` — `microsoft.network/routefilters`  resource objects
- `LW_CFG_AZURE_NETWORK_ROUTETABLES` — `microsoft.network/routetables`  resource objects
- `LW_CFG_AZURE_NETWORK_SAMPLERESOURCES` — `microsoft.network/sampleresources`  resource objects
- `LW_CFG_AZURE_NETWORK_SECURITYPARTNERPROVIDERS` — `microsoft.network/securitypartnerproviders`  resource objects
- `LW_CFG_AZURE_NETWORK_SERVICEENDPOINTPOLICIES` — `microsoft.network/serviceendpointpolicies`  resource objects
- `LW_CFG_AZURE_NETWORK_TRAFFICMANAGERPROFILES` — `microsoft.network/trafficmanagerprofiles`  resource objects
- `LW_CFG_AZURE_NETWORK_VIRTUALHUBS` — `microsoft.network/virtualhubs`  resource objects
- `LW_CFG_AZURE_NETWORK_VIRTUALHUBS_BGPCONNECTIONS` — `microsoft.network/virtualhubs/bgpconnections`  resource objects
- `LW_CFG_AZURE_NETWORK_VIRTUALHUBS_IPCONFIGURATIONS` — `microsoft.network/virtualhubs/ipconfigurations`  resource objects
- `LW_CFG_AZURE_NETWORK_VIRTUALNETWORKGATEWAYS` — `microsoft.network/virtualnetworkgateways`  resource objects
- `LW_CFG_AZURE_NETWORK_VIRTUALNETWORKS` — `microsoft.network/virtualnetworks`  resource objects
- `LW_CFG_AZURE_NETWORK_VIRTUALNETWORKTAPS` — `microsoft.network/virtualnetworktaps`  resource objects
- `LW_CFG_AZURE_NETWORK_VIRTUALROUTERS` — `microsoft.network/virtualrouters`  resource objects
- `LW_CFG_AZURE_NETWORK_VIRTUALWANS` — `microsoft.network/virtualwans`  resource objects
- `LW_CFG_AZURE_NETWORK_VPNGATEWAYS` — `microsoft.network/vpngateways`  resource objects
- `LW_CFG_AZURE_NETWORK_VPNSERVERCONFIGURATIONS` — `microsoft.network/vpnserverconfigurations`  resource objects
- `LW_CFG_AZURE_NETWORK_VPNSITES` — `microsoft.network/vpnsites`  resource objects

### Network Function

- `LW_CFG_AZURE_NETWORKFUNCTION_AZURETRAFFICCOLLECTORS` — `microsoft.networkfunction/azuretrafficcollectors`  resource objects

### Nginx nginxplus

| LW_CFG_AZURE_NGINX.NGINXPLUS_NGINXDEPLOYMENTS | Results for nginx.nginxplus/nginxdeployments resource objects |

### Notification Hubs

- `LW_CFG_AZURE_NOTIFICATIONHUBS_NAMESPACES` — `microsoft.notificationhubs/namespaces`  resource objects
- `LW_CFG_AZURE_NOTIFICATIONHUBS_NAMESPACES_NOTIFICATIONHUBS` — `microsoft.notificationhubs/namespaces/notificationhubs`  resource objects

### OffAzure

- `LW_CFG_AZURE_OFFAZURE_HYPERVSITES` — `microsoft.offazure/hypervsites`  resource objects
- `LW_CFG_AZURE_OFFAZURE_IMPORTSITES` — `microsoft.offazure/importsites`  resource objects
- `LW_CFG_AZURE_OFFAZURE_MASTERSITES` — `microsoft.offazure/mastersites`  resource objects
- `LW_CFG_AZURE_OFFAZURE_SERVERSITES` — `microsoft.offazure/serversites`  resource objects
- `LW_CFG_AZURE_OFFAZURE_VMWARESITES` — `microsoft.offazure/vmwaresites`  resource objects

### Operational Insights

- `LW_CFG_AZURE_OPERATIONALINSIGHTS_CLUSTERS` — Results for  `microsoft.operationalinsights/clusters`  resource objects
- `LW_CFG_AZURE_OPERATIONALINSIGHTS_QUERYPACKS` — `microsoft.operationalinsights/querypacks`  resource objects
- `LW_CFG_AZURE_OPERATIONALINSIGHTS_WORKSPACES` — `microsoft.operationalinsights/workspaces`  resource objects

### Operations Management

- `LW_CFG_AZURE_OPERATIONSMANAGEMENT_SOLUTIONS` — `microsoft.operationsmanagement/solutions`  resource objects

### Organization

- `LW_CFG_AZURE_ORGANIZATION` — Azure Organization resource objects

### Peering

- `LW_CFG_AZURE_PEERING_PEERINGS` — Results for microsoft.peering/peerings resource objects
- `LW_CFG_AZURE_PEERING_PEERINGSERVICES` — Results for microsoft.peering/peeringservices resource objects

### Physical

- `LW_CFG_AZURE_LOCATION_PHYSICAL` — Results for physical location resource objects

### Policy Insights

- `LW_CFG_AZURE_POLICYINSIGHTS_ATTESTATIONS` — Results for microsoft.policyinsights/attestations resource objects
- `LW_CFG_AZURE_POLICYINSIGHTS_REMEDIATIONS` — Results for microsoft.policyinsights/remediations resource objects

### Portal

- `LW_CFG_AZURE_PORTAL_DASHBOARDS` — `microsoft.portal/dashboards`  resource objects

### Power BI

- `LW_CFG_AZURE_POWERBI_WORKSPACECOLLECTIONS` — `microsoft.powerbi/workspacecollections`  resource objects
- `LW_CFG_AZURE_POWERBI_PRIVATELINKSERVICESFORPOWERBI` — Results for microsoft.powerbi/privatelinkservicesforpowerbi resource objects

### Power BI Dedicated

- `LW_CFG_AZURE_POWERBIDEDICATED_AUTOSCALEVCORES` — `microsoft.powerbidedicated/autoscalevcores`  resource objects
- `LW_CFG_AZURE_POWERBIDEDICATED_CAPACITIES` — `microsoft.powerbidedicated/capacities`  resource objects

### Power Platform

- `LW_CFG_AZURE_POWERPLATFORM_ACCOUNTS` — `microsoft.powerplatform/accounts`  resource objects
- `LW_CFG_AZURE_POWERPLATFORM_ENTERPRISEPOLICIES` — `microsoft.powerplatform/enterprisepolicies`  resource objects

### Purview

- `LW_CFG_AZURE_PURVIEW_ACCOUNTS` — `microsoft.purview/accounts`  resource objects

### Quantum

- `LW_CFG_AZURE_QUANTUM_WORKSPACES` — Results for microsoft.quantum/workspaces resource objects

### Recovery Services

- `LW_CFG_AZURE_RECOVERYSERVICES_VAULTS` — `microsoft.recoveryservices/vaults`  resource objects
- `LW_CFG_AZURE_RECOVERYSERVICES_VAULTS_BACKUPENCRYPTIONCONFIGS` — Results for `microsoft.recoveryservices/vaults/ backupencryptionconfigs`  resource objects
- `LW_CFG_AZURE_RECOVERYSERVICES_VAULTS_BACKUPSTORAGECONFIG` — `microsoft.recoveryservices/vaults/ backupstorageconfig`  resource objects
- `LW_CFG_AZURE_RECOVERYSERVICES_VAULTS_REPLICATIONFABRICS` — `microsoft.recoveryservices/vaults/ replicationfabrics`  resource objects
- `LW_CFG_AZURE_RECOVERYSERVICES_VAULTS_REPLICATIONFABRICS_REPLICATIONPROTECTIONCONTAINERS` — `microsoft.recoveryservices/vaults/ replicationfabrics/ replicationprotectioncontainers`  resource objects
- `LW_CFG_AZURE_RECOVERYSERVICES_VAULTS_REPLICATIONFABRICS_REPLICATIONPROTECTIONCONTAINERS_REPLICATIONPROTECTEDITEMS` — `microsoft.recoveryservices/vaults/ replicationfabrics/ replicationprotectioncontainers/ replicationprotecteditems`  resource objects
- `LW_CFG_AZURE_RECOVERYSERVICES_VAULTS_REPLICATIONFABRICS_REPLICATIONPROTECTIONCONTAINERS_REPLICATIONPROTECTIONCONTAINERMAPPINGS` — `microsoft.recoveryservices/vaults/ replicationfabrics/ replicationprotectioncontainers/ replicationprotectioncontainermappings`  resource objects
- `LW_CFG_AZURE_RECOVERYSERVICES_VAULTS_REPLICATIONFABRICS_REPLICATIONRECOVERYSERVICESPROVIDERS` — `microsoft.recoveryservices/vaults/ replicationfabrics/ replicationrecoveryservicesproviders`  resource objects

### Red Hat Open Shift

- `LW_CFG_AZURE_REDHATOPENSHIFT_OPENSHIFTCLUSTERS` — Results for microsoft.redhatopenshift/openshiftclusters resource objects

### Relay

- `LW_CFG_AZURE_RELAY_NAMESPACES` — `microsoft.relay/namespaces`  resource objects

### Resource Connector

- `LW_CFG_AZURE_RESOURCECONNECTOR_APPLIANCES` — `microsoft.resourceconnector/appliances`  resource objects

### Resource Graph

- `LW_CFG_AZURE_RESOURCEGRAPH_QUERIES` — `microsoft.resourcegraph/queries`  resource objects

### Resources

- `LW_CFG_AZURE_RESOURCES_DEPLOYMENTSCRIPTS` — `microsoft.resources/deploymentscripts`  resource objects
- `LW_CFG_AZURE_RESOURCES_SUBSCRIPTIONS` — `microsoft.resources/subscriptions`  resource objects
- `LW_CFG_AZURE_RESOURCES_TEMPLATESPECS` — `microsoft.resources/templatespecs`  resource objects
- `LW_CFG_AZURE_RESOURCES_TEMPLATESPECS_VERSIONS` — `microsoft.resources/templatespecs/versions`  resource objects
- `LW_CFG_AZURE_RESOURCES_RESOURCEGROUPS` — Results for microsoft.resources/resourcegroups resource objects

### SaaS

- `LW_CFG_AZURE_SAAS_RESOURCES` — `microsoft.saas/resources`  resource objects

### SCVMM

- `LW_CFG_AZURE_SCVMM_CLOUDS` — `microsoft.scvmm/clouds`  resource objects
- `LW_CFG_AZURE_SCVMM_VIRTUALMACHINETEMPLATES` — `microsoft.scvmm/virtualmachinetemplates`  resource objects
- `LW_CFG_AZURE_SCVMM_VIRTUALNETWORKS` — `microsoft.scvmm/virtualnetworks`  resource objects
- `LW_CFG_AZURE_SCVMM_VMMSERVERS` — `microsoft.scvmm/vmmservers`  resource objects

### Search

- `LW_CFG_AZURE_SEARCH_SEARCHSERVICES` — `microsoft.search/searchservices`  resource objects

### Security

- `LW_CFG_AZURE_SECURITY_ASSIGNMENTS` — `microsoft.security/assignments`  resource objects
- `LW_CFG_AZURE_SECURITY_AUTOMATIONS` — `microsoft.security/automations`  resource objects
- `LW_CFG_AZURE_SECURITY_CUSTOMASSESSMENTAUTOMATIONS` — `microsoft.security/customassessmentautomations`  resource objects
- `LW_CFG_AZURE_SECURITY_CUSTOMENTITYSTOREASSIGNMENTS` — `microsoft.security/customentitystoreassignments`  resource objects
- `LW_CFG_AZURE_SECURITY_DATASCANNERS` — `microsoft.security/datascanners`  resource objects
- `LW_CFG_AZURE_SECURITY_IOTSECURITYSOLUTIONS` — `microsoft.security/iotsecuritysolutions`  resource objects
- `LW_CFG_AZURE_SECURITY_PRICINGS` — `microsoft.security/pricings`  resource objects
- `LW_CFG_AZURE_SECURITY_SECURITYCONNECTORS` — `microsoft.security/securityconnectors`  resource objects
- `LW_CFG_AZURE_SECURITY_SECURITYCONTACTS` — Results for  `microsoft.security/securitycontacts` resource objects
- `LW_CFG_AZURE_SECURITY_STANDARDS` — `microsoft.security/standards`  resource objects

### Security Detonation

- `LW_CFG_AZURE_SECURITYDETONATION_CHAMBERS` — `microsoft.securitydetonation/chambers`  resource objects

### Security DevOps

- `LW_CFG_AZURE_SECURITYDEVOPS_GITHUBCONNECTORS` — `microsoft.securitydevops/githubconnectors`  resource objects

### Service Bus

- `LW_CFG_AZURE_SERVICEBUS_NAMESPACES` — `microsoft.servicebus/namespaces`  resource objects

### Service Fabric

- `LW_CFG_AZURE_SERVICEFABRIC_CLUSTERS` — `microsoft.servicefabric/clusters`  resource objects

### Service Fabric Mesh

- `LW_CFG_AZURE_SERVICEFABRICMESH_APPLICATIONS` — Results for microsoft.servicefabricmesh/applications resource objects
- `LW_CFG_AZURE_SERVICEFABRICMESH_GATEWAYS` — Results for microsoft.servicefabricmesh/gateways resource objects
- `LW_CFG_AZURE_SERVICEFABRICMESH_NETWORKS` — Results for microsoft.servicefabricmesh/networks resource objects
- `LW_CFG_AZURE_SERVICEFABRIC_MANAGEDCLUSTERS` — Results for microsoft.servicefabric/managedclusters resource objects

### Service Principal

- `LW_CFG_AZURE_SERVICEPRINCIPAL` — Azure Service Principal resource objects

### Services Hub

- `LW_CFG_AZURE_SERVICESHUB_CONNECTORS` — `microsoft.serviceshub/connectors`  resource objects

### Signalr Service

- `LW_CFG_AZURE_SIGNALRSERVICE_SIGNALR` — `microsoft.signalrservice/signalr`  resource objects
- `LW_CFG_AZURE_SIGNALRSERVICE_WEBPUBSUB` — `microsoft.signalrservice/webpubsub`  resource objects

### Solutions

- `LW_CFG_AZURE_SOLUTIONS_APPLICATIONDEFINITIONS` — `microsoft.solutions/applicationdefinitions`  resource objects
- `LW_CFG_AZURE_SOLUTIONS_APPLICATIONS` — `microsoft.solutions/applications`  resource objects

### SQL

- `LW_CFG_AZURE_SQL_INSTANCEPOOLS` — `microsoft.sql/instancepools`  resource objects
- `LW_CFG_AZURE_SQL_MANAGEDINSTANCES` — `microsoft.sql/managedinstances`  resource objects
- `LW_CFG_AZURE_SQL_MANAGEDINSTANCES_DATABASES` — `microsoft.sql/managedinstances/databases`  resource objects
- `LW_CFG_AZURE_SQL_SERVERS` — `microsoft.sql/servers`  resource objects
- `LW_CFG_AZURE_SQL_SERVERS_ADMINISTRATORS` — `microsoft.sql/servers/administrators`  resource objects
- `LW_CFG_AZURE_SQL_SERVERS_ADVANCEDTHREATPROTECTIONSETTINGS` — `microsoft.sql/servers/ advancedthreatprotectionsettings`  resource objects
- `LW_CFG_AZURE_SQL_SERVERS_DATABASES` — `microsoft.sql/servers/databases`  resource objects
- `LW_CFG_AZURE_SQL_SERVERS_DATABASES_TRANSPARENTDATAENCRYPTION` — `microsoft.sql/servers/databases/ transparentdataencryption`  resource objects
- `LW_CFG_AZURE_SQL_SERVERS_ELASTICPOOLS` — `microsoft.sql/servers/elasticpools`  resource objects
- `LW_CFG_AZURE_SQL_SERVERS_ENCRYPTIONPROTECTOR` — `microsoft.sql/servers/encryptionprotector`  resource objects
- `LW_CFG_AZURE_SQL_SERVERS_FIREWALLRULES` — `microsoft.sql/servers/firewallrules`  resource objects
- `LW_CFG_AZURE_SQL_SERVERS_JOBACCOUNTS` — `microsoft.sql/servers/jobaccounts`  resource objects
- `LW_CFG_AZURE_SQL_SERVERS_JOBAGENTS` — `microsoft.sql/servers/jobagents`  resource objects
- `LW_CFG_AZURE_SQL_SERVERS_VULNERABILITY_ASSESSMENTS` — `microsoft.sql/servers/vulnerabilityassessments`  resource objects
- `LW_CFG_AZURE_SQL_VIRTUALCLUSTERS` — `microsoft.sql/virtualclusters`  resource objects

### SQL Virtual Machine

- `LW_CFG_AZURE_SQLVIRTUALMACHINE_SQLVIRTUALMACHINEGROUPS` — `microsoft.sqlvirtualmachine/ sqlvirtualmachinegroups`  resource objects
- `LW_CFG_AZURE_SQLVIRTUALMACHINE_SQLVIRTUALMACHINES` — `microsoft.sqlvirtualmachine/s qlvirtualmachines`  resource objects

### SQL VM

- `LW_CFG_AZURE_SQLVM_DWVM` — `microsoft.sqlvm/dwvm`  resource objects

### Stack

- `LW_CFG_AZURE_AZURESTACK_LINKEDSUBSCRIPTIONS` — Results for microsoft.azurestack/linkedsubscriptions resource objects
- `LW_CFG_AZURE_AZURESTACK_REGISTRATIONS` — Results for microsoft.azurestack/registrations resource objects

### Stack HCI

- `LW_CFG_AZURE_AZURESTACKHCI_CLUSTERS` — `microsoft.azurestackhci/clusters`  resource objects
- `LW_CFG_AZURE_AZURESTACKHCI_VIRTUALNETWORKS` — `microsoft.azurestackhci/virtualnetworks`  resource objects
- `LW_CFG_AZURE_AZURESTACKHCI_NETWORKINTERFACES` — Results for microsoft.azurestackhci/networkinterfaces resource objects
- `LW_CFG_AZURE_AZURESTACKHCI_VIRTUALHARDDISKS` — Results for microsoft.azurestackhci/virtualharddisks resource objects

### Storage

- `LW_CFG_AZURE_STORAGE_DATAMOVERS` — `microsoft.storage/datamovers`  resource objects
- `LW_CFG_AZURE_STORAGE_STORAGEACCOUNTS` — `microsoft.storage/storageaccounts`  resource objects
- `LW_CFG_AZURE_STORAGE_STORAGEACCOUNTS_BLOBSERVICES` — Results for  `microsoft.storage/storageaccounts/blobservices`  resource objects
- `LW_CFG_AZURE_STORAGE_STORAGEACCOUNTS_BLOBSERVICES_CONTAINERS` — Results for  `microsoft.storage/storageaccounts/blobservices/containers`  resource objects
- `LW_CFG_AZURE_STORAGE_STORAGEACCOUNTS_FILESERVICES` — Results for  `microsoft.storage/storageaccounts/fileservices` resource objects
- `LW_CFG_AZURE_STORAGE_STORAGEACCOUNTS_FILESERVICES_SHARES` — Results for  `microsoft.storage/storageaccounts/fileservices/shares`  resource objects
- `LW_CFG_AZURE_STORAGE_STORAGEACCOUNTS_BLOBSERVICES_CONTAINERS_IMMUTABILITYPOLICIES` — Results for microsoft.storage/storageaccounts/blobservices/containers/immutabilitypolicies resource objects

### Storage Cache

- `LW_CFG_AZURE_STORAGECACHE_AMLFILESYSTEMS` — `microsoft.storagecache/amlfilesystems`  resource objects
- `LW_CFG_AZURE_STORAGECACHE_CACHES` — `microsoft.storagecache/caches`  resource objects

### Storage Pool

- `LW_CFG_AZURE_STORAGEPOOL_DISKPOOLS` — `microsoft.storagepool/diskpools`  resource objects

### Storage Sync

- `LW_CFG_AZURE_STORAGESYNC_STORAGESYNCSERVICES` — `microsoft.storagesync/storagesyncservices`  resource objects
- `LW_CFG_AZURE_STORAGESYNC_STORAGESYNCSERVICES_PRIVATEENDPOINTCONNECTIONS` — Results for microsoft.storagesync/storagesyncservices/privateendpointconnections resource objects
- `LW_CFG_AZURE_STORAGESYNC_STORAGESYNCSERVICES_REGISTEREDSERVERS` — Results for microsoft.storagesync/storagesyncservices/registeredservers resource objects

### Storage Sync Dev

- `LW_CFG_AZURE_STORAGESYNCDEV_STORAGESYNCSERVICES` — `microsoft.storagesyncdev/storagesyncservices`  resource objects

### Storage Sync Int

- `LW_CFG_AZURE_STORAGESYNCINT_STORAGESYNCSERVICES` — `microsoft.storagesyncint/storagesyncservices`  resource objects

### Stream Analytics

- `LW_CFG_AZURE_STREAMANALYTICS_CLUSTERS` — `microsoft.streamanalytics/clusters`  resource objects
- `LW_CFG_AZURE_STREAMANALYTICS_STREAMINGJOBS` — `microsoft.streamanalytics/streamingjobs`  resource objects

### Synapse

- `LW_CFG_AZURE_SYNAPSE_PRIVATELINKHUBS` — `microsoft.synapse/privatelinkhubs`  resource objects
- `LW_CFG_AZURE_SYNAPSE_WORKSPACES` — `microsoft.synapse/workspaces`  resource objects
- `LW_CFG_AZURE_SYNAPSE_WORKSPACES_BIGDATAPOOLS` — `microsoft.synapse/workspaces/bigdatapools`  resource objects
- `LW_CFG_AZURE_SYNAPSE_WORKSPACES_EVENTSTREAMS` — `microsoft.synapse/workspaces/eventstreams`  resource objects
- `LW_CFG_AZURE_SYNAPSE_WORKSPACES_KUSTOPOOLS` — `microsoft.synapse/workspaces/kustopools`  resource objects
- `LW_CFG_AZURE_SYNAPSE_WORKSPACES_SQLDATABASES` — `microsoft.synapse/workspaces/sqldatabases`  resource objects
- `LW_CFG_AZURE_SYNAPSE_WORKSPACES_SQLPOOLS` — `microsoft.synapse/workspaces/sqlpools`  resource objects

### User

- `LW_CFG_AZURE_USER` — Azure User resource objects

### Video Indexer

- `LW_CFG_AZURE_VIDEOINDEXER_ACCOUNTS` — `microsoft.videoindexer/accounts`  resource objects

### Virtual Machine Images

- `LW_CFG_AZURE_VIRTUALMACHINEIMAGES_IMAGETEMPLATES` — `microsoft.virtualmachineimages/imagetemplates`  resource objects

### Visual Studio

- `LW_CFG_AZURE_VISUALSTUDIO_ACCOUNT` — `microsoft.visualstudio/account`  resource objects

### Web

- `LW_CFG_AZURE_WEB_APIMANAGEMENTACCOUNTS` — `microsoft.web/apimanagementaccounts`  resource objects
- `LW_CFG_AZURE_WEB_APIMANAGEMENTACCOUNTS_APIS` — `microsoft.web/apimanagementaccounts/apis`  resource objects
- `LW_CFG_AZURE_WEB_CERTIFICATES` — `microsoft.web/certificates`  resource objects
- `LW_CFG_AZURE_WEB_CONNECTIONGATEWAYS` — `microsoft.web/connectiongateways`  resource objects
- `LW_CFG_AZURE_WEB_CONNECTIONS` — `microsoft.web/connections`  resource objects
- `LW_CFG_AZURE_WEB_CONTAINERAPPS` — `microsoft.web/containerapps`  resource objects
- `LW_CFG_AZURE_WEB_CUSTOMAPIS` — `microsoft.web/customapis`  resource objects
- `LW_CFG_AZURE_WEB_HOSTINGENVIRONMENTS` — `microsoft.web/hostingenvironments`  resource objects
- `LW_CFG_AZURE_WEB_KUBEENVIRONMENTS` — `microsoft.web/kubeenvironments`  resource objects
- `LW_CFG_AZURE_WEB_SERVERFARMS` — `microsoft.web/serverfarms`  resource objects
- `LW_CFG_AZURE_WEB_SITES` — `microsoft.web/sites`  resource objects
- `LW_CFG_AZURE_WEB_SITES_CONFIG` — `microsoft.web/sites/config`  resource objects
- `LW_CFG_AZURE_WEB_SITES_PREMIERADDONS` — `microsoft.web/sites/premieraddons`  resource objects
- `LW_CFG_AZURE_WEB_SITES_SLOTS` — `microsoft.web/sites/slots`  resource objects
- `LW_CFG_AZURE_WEB_STATICSITES` — `microsoft.web/staticsites`  resource objects
- `LW_CFG_AZURE_WEB_WORKERAPPS` — `microsoft.web/workerapps`  resource objects

### Workloads

- `LW_CFG_AZURE_WORKLOADS_SAPVIRTUALINSTANCES` — Results for microsoft.workloads/sapvirtualinstances resource objects
- `LW_CFG_AZURE_WORKLOADS_SAPVIRTUALINSTANCES_APPLICATIONINSTANCES` — Results for microsoft.workloads/sapvirtualinstances/applicationinstances resource objects
- `LW_CFG_AZURE_WORKLOADS_SAPVIRTUALINSTANCES_CENTRALINSTANCES` — Results for microsoft.workloads/sapvirtualinstances/centralinstances resource objects
- `LW_CFG_AZURE_WORKLOADS_SAPVIRTUALINSTANCES_DATABASEINSTANCES` — Results for microsoft.workloads/sapvirtualinstances/databaseinstances resource objects
