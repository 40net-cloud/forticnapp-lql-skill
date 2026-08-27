<!-- Generated from FortiCNAPP 26.2 LQL Reference Guide (fetched 2026-08-26). Source:
     https://docs.fortinet.com/document/forticnapp/latest/lql-reference/435177/example-queries -->

# Example Queries

This topic provides example queries that use a variety of datasources. The queries are JSON formatted for readability.

* IAM users with two active access keys
* CloudTrail trails not encrypted with a KMS key
* Default security groups that allow traffic
* Account-level EBS encryption is disabled
* Customer-managed KMS keys with rotation not enabled
* VPCs with flow logging not enabled
* S3 buckets not encrypted at rest
* CloudTrail trails not integrated with CloudWatch logs
* IAM user has inline policy
* EC2 instance created without resource tags
* Event source has specific resource tag value
* Exposed Kubernetes dashboard
* Kubernetes system role modified or deleted
* Kubernetes pod uses nonstandard registry
* Example Queries
* Public IP addresses of EC2 instances

## Running the Example Queries

### Using the Lacework CLI

To try out the samples below with the Lacework CLI, first make sure that you have set up the Lacework CLI.

To run a specific query, click the copy icon at the top right of the query listing below, and paste the contents into a local file, such as `Example_Query.lql`.

You can then pass the file as an argument to the `lacework query run` command to run the query, as follows:

```
lacework query run -f path/to/Example_Query.lql
```

### Using Postman

As an alternative to using the Lacework CLI, you can use an REST client application, such as Postman.

To run a query, first use the `POST /api/v2/Queries` endpoint to add the query to your Lacework instance. First format the query for use by removing the query ID and all line breaks and then including the content within `queryText`. Provide a unique `queryId` and include both fields' content in the request body.

```
  "queryText": "{source {LW_CFG_AWS_IAM_USERS_GET_CREDENTIAL_REPORT} filter {RESOURCE_CONFIG:access_key_1_active = 'true' and RESOURCE_CONFIG:access_key_2_active = 'true'} return distinct {ACCOUNT_ALIAS, ACCOUNT_ID, ARN as RESOURCE_KEY, RESOURCE_REGION, RESOURCE_TYPE, SERVICE, 'IAMUserWithTwoActiveAccessKeys' as COMPLIANCE_FAILURE_REASON}}",
  "queryId": "Example_Global_AWS_Config_UserWithTwoActiveAccessKeys"
```

Then invoke the `POST api/v2/Queries/execute` endpoint, which executes the query and returns its results (without adding it to your Lacework instance). You must first format the query for use by removing the query ID and all line breaks and then including the content within `queryText`. Copy the field's content into the request body and provide start and end times.

```
{
    "query": {
        "queryText": "{source {LW_CFG_AWS_IAM_USERS_GET_CREDENTIAL_REPORT} filter {RESOURCE_CONFIG:access_key_1_active = 'true' and RESOURCE_CONFIG:access_key_2_active = 'true'} return distinct {ACCOUNT_ALIAS, ACCOUNT_ID, ARN as RESOURCE_KEY, RESOURCE_REGION, RESOURCE_TYPE, SERVICE, 'IAMUserWithTwoActiveAccessKeys' as COMPLIANCE_FAILURE_REASON}}"
    },
    "arguments": [
        {"name": "StartTimeRange", "value": "2022-02-10T00:00:00.000Z"},
        {"name": "EndTimeRange", "value": "2022-02-11T00:00:00.000Z"}
    ]
}
```

## IAM users with two active access keys

Find IAM users with two active access keys.

```
#
# https://docs.lacework.net/lql/restricted/lql-query-examples#iam-users-with-two-active-access-keys
# Find IAM users with two active access keys.
#
---
queryId: Example_Global_AWS_Config_UserWithTwoActiveAccessKeys
queryText: |-
 {
     source {
         LW_CFG_AWS_IAM_USERS_GET_CREDENTIAL_REPORT
     }
     filter {
         RESOURCE_CONFIG:access_key_1_active = 'true'
         and RESOURCE_CONFIG:access_key_2_active = 'true'
     }
     return distinct {
         ACCOUNT_ALIAS,
         ACCOUNT_ID,
         ARN as RESOURCE_KEY,
         RESOURCE_REGION,
         RESOURCE_TYPE,
         SERVICE,
         'IAMUserWithTwoActiveAccessKeys' as COMPLIANCE_FAILURE_REASON
     }
 }
```

## CloudTrail trails not encrypted with a KMS key

Find CloudTrail trails not encrypted with a KMS key.

```
#
# https://docs.lacework.net/lql/restricted/lql-query-examples#cloudtrail-trails-not-encrypted-with-a-kms-key
# Find CloudTrail trails not encrypted with a KMS key.
#
---
queryId: Example_Global_AWS_Config_CloudTrailLogsNotEncryptedUsingKMS
queryText: |-
 {
     source {
         LW_CFG_AWS_CLOUDTRAIL
     }
     filter {
         not value_exists(RESOURCE_CONFIG:KmsKeyId)
     }
     return distinct {
         ACCOUNT_ALIAS,
         ACCOUNT_ID,
         ARN as RESOURCE_KEY,
         RESOURCE_REGION,
         RESOURCE_TYPE,
         SERVICE,
         'CloudTrailLogsNotEncrypted' as COMPLIANCE_FAILURE_REASON
     }
 }
```

## Default security groups that allow traffic

Find default security groups that allow traffic.

```
#
# https://docs.lacework.net/lql/restricted/lql-query-examples#default-security-groups-that-allow-traffic
# Find default security groups that allow traffic.
#
---
queryId: Example_Global_AWS_Config_DefaultSecurityGroupAllowsTraffic
queryText: |-
 {
     source {
         LW_CFG_AWS_EC2_SECURITY_GROUPS a,
         array_to_rows(a.RESOURCE_CONFIG:IpPermissions) as (ip_permissions),
         array_to_rows(a.RESOURCE_CONFIG:IpPermissionsEgress) as (ip_permissions_egress)
     }
     filter {
         RESOURCE_CONFIG:GroupName = 'default'
         and (ip_permissions <> '[]'
             or ip_permissions_egress <> '[]')
     }
     return distinct {
         ACCOUNT_ALIAS,
         ACCOUNT_ID,
         ARN as RESOURCE_KEY,
         RESOURCE_REGION,
         RESOURCE_TYPE,
         SERVICE,
         'DefaultSecurityGroupAllowsTraffic' as COMPLIANCE_FAILURE_REASON
     }
 }
```

## Account-level EBS encryption is disabled

Determine if account-level EBS encryption is disabled.

```
#
# https://docs.lacework.net/lql/restricted/lql-query-examples#account-level-ebs-encryption-is-disabled
# Determine if account-level EBS encryption is disabled.
#
---
queryId: Example_Global_AWS_Config_EBSVolumeEncryptionNotEnabledByDefault
queryText: |-
 {
     source {
         LW_CFG_AWS_EC2_EBS_ENCRYPTION_BY_DEFAULT
     }
     filter {
         RESOURCE_CONFIG:EbsEncryptionByDefault = 'false'
     }
     return distinct {
         ACCOUNT_ALIAS,
         ACCOUNT_ID as RESOURCE_KEY,
         RESOURCE_REGION,
         RESOURCE_TYPE,
         SERVICE,
         'EbsEncryptionNotEnabledByDefault' as COMPLIANCE_FAILURE_REASON
     }
 }
```

## Customer-managed KMS keys with rotation not enabled

Find customer-managed KMS keys with rotation not enabled.

```
#
# https://docs.lacework.net/lql/restricted/lql-query-examples#customer-managed-kms-keys-with-rotation-not-enabled
# Find customer-managed KMS keys with rotation not enabled.
#
---
queryId: Example_Global_AWS_Config_KMSKeyRotationDisabled
queryText: |-
 {
     source {
         LW_CFG_AWS_KMS_KEYS keys with(
              LW_CFG_AWS_KMS_KEYS_DESCRIBE_KEY key,
              LW_CFG_AWS_KMS_KEYS_GET_ROTATION_STATUS rotation
         )
     }
     filter {
         key.RESOURCE_CONFIG:KeyMetadata.Enabled = 'true'
         and key.RESOURCE_CONFIG:KeyMetadata.KeyManager = 'CUSTOMER'
         and key.RESOURCE_CONFIG:KeyMetadata.KeySpec = 'SYMMETRIC_DEFAULT'
         and rotation.RESOURCE_CONFIG:KeyRotationEnabled = 'false'
     }
     return distinct {
         key.ACCOUNT_ALIAS,
         key.ACCOUNT_ID,
         key.ARN as RESOURCE_KEY,
         key.RESOURCE_REGION,
         key.RESOURCE_TYPE,
         key.SERVICE,
         'KMSKeyRotationNotEnabled' as COMPLIANCE_FAILURE_REASON
     }
 }
```

## VPCs with flow logging not enabled

Find VPCs with flow logging not enabled.

```
#
# https://docs.lacework.net/lql/restricted/lql-query-examples#vpcs-with-flow-logging-not-enabled
# Find VPCs with flow logging not enabled.
#
---
queryId: Example_Global_AWS_Config_VPCFlowLoggingNotEnabled
queryText: |-
 {
     source {
         LW_CFG_AWS_EC2_VPCS vpc
         with LW_CFG_AWS_EC2_VPC_FLOW_LOGS log
     }
     filter {
         not value_exists(log.RESOURCE_CONFIG)
         or log.RESOURCE_CONFIG:FlowLogStatus <> 'ACTIVE'
     }
     return distinct {
         vpc.ACCOUNT_ALIAS,
         vpc.ACCOUNT_ID,
         vpc.ARN as RESOURCE_KEY,
         vpc.RESOURCE_REGION,
         vpc.RESOURCE_TYPE,
         vpc.SERVICE,
         case when not value_exists(log.RESOURCE_CONFIG) then 'VPCFlowLoggingNotEnabled'
         else 'VPCFlowLoggingNotActive' end as COMPLIANCE_FAILURE_REASON
     }
 }
```

## S3 buckets not encrypted at rest

Find S3 buckets not encrypted at rest.

```
#
# https://docs.lacework.net/lql/restricted/lql-query-examples#s3-buckets-not-encrypted-at-rest
# Find S3 buckets not encrypted at rest.
#
---
queryId: Example_Global_AWS_Config_S3BucketNotEncryptedAtRest
queryText: |-
 {
     source {
         LW_CFG_AWS_S3 bucket
         with LW_CFG_AWS_S3_GET_BUCKET_ENCRYPTION encryption
     }
     filter {
         not value_exists(encryption.RESOURCE_CONFIG)
     }
     return distinct {
         bucket.ACCOUNT_ALIAS,
         bucket.ACCOUNT_ID,
         bucket.ARN as RESOURCE_KEY,
         bucket.RESOURCE_REGION,
         bucket.RESOURCE_TYPE,
         bucket.SERVICE,
         'S3BucketServerSideEncryptionNotEnabled' as COMPLIANCE_FAILURE_REASON
     }
 }
```

## CloudTrail trails not integrated with CloudWatch logs

Find CloudTrail trails not integrated with CloudWatch logs.

```
#
# https://docs.lacework.net/lql/restricted/lql-query-examples#cloudtrail-trails-not-integrated-with-cloudwatch-logs
# Find CloudTrail trails not integrated with CloudWatch logs.
#
---
queryId: Example_Global_AWS_Config_TrailNotIntegratedWithCloudwatchLogs
queryText: |-
 {
     source {
         LW_CFG_AWS_CLOUDTRAIL trail
         with LW_CFG_AWS_CLOUDTRAIL_GET_TRAIL_STATUS status
     }
     filter {
         not value_exists(trail.RESOURCE_CONFIG:CloudWatchLogsLogGroupArn)
         or (value_exists(trail.RESOURCE_CONFIG:CloudWatchLogsLogGroupArn)
         and (not value_exists(status.RESOURCE_CONFIG:LatestCloudWatchLogsDeliveryTime)
         or (value_exists(status.RESOURCE_CONFIG:LatestCloudWatchLogsDeliveryTime)
         and current_timestamp_sec()::number - status.RESOURCE_CONFIG:LatestCloudWatchLogsDeliveryTime::number > 86400)))
     }
     return distinct {
         trail.ACCOUNT_ALIAS,
         trail.ACCOUNT_ID,
         trail.ARN as RESOURCE_KEY,
         trail.RESOURCE_REGION,
         trail.RESOURCE_TYPE,
         trail.SERVICE,
         case when not value_exists(trail.RESOURCE_CONFIG:CloudWatchLogsLogGroupArn) then 'CloudWatchLogsNotIntegrated'
         else 'CloudWatchLogDeliveryTimeNotRecent' end as COMPLIANCE_FAILURE_REASON
     }
 }
```

## IAM user has inline policy

Find IAM users with an inline policy.

```
#
# https://docs.lacework.net/lql/restricted/lql-query-examples#cloudtrail-trails-not-integrated-with-cloudwatch-logs
# Find IAM users with an inline policy.
#
---
queryId: Example_Global_AWS_Config_IAMUserWithInlinePolicy
queryText: |-
 {
     source {
         LW_CFG_AWS_IAM_USERS user
         with LW_CFG_AWS_IAM_USERS_LIST_POLICIES inline
     }
     filter {
         value_exists(inline.RESOURCE_CONFIG)
     }
     return distinct {
         user.ACCOUNT_ALIAS,
         user.ACCOUNT_ID,
         user.ARN as RESOURCE_KEY,
         user.RESOURCE_REGION,
         user.RESOURCE_TYPE,
         user.SERVICE,
         'IAMUserWithInlinePolicy' as COMPLIANCE_FAILURE_REASON
     }
 }
```

## EC2 instance created without resource tags

Find EC2 instances created without tags or with empty tags.

```
#
# https://docs.lacework.net/lql/restricted/lql-query-examples#ec2-instance-created-without-resource-tags
# Find EC2 instances created without tags or with empty tags.
#
---
queryId: Example_Global_AWS_EC2InstanceUntagged
queryText: |-
 {
     source {
         CloudTrailRawEvents
     } 
     filter {
         EVENT_SOURCE = 'ec2.amazonaws.com' and 
         EVENT:requestParameters.tagSpecificationSet is null and 
         ERROR_CODE is null
     } 
     return distinct {
         INSERT_ID,
         INSERT_TIME,
         EVENT_TIME,
         EVENT
     }
 }
```

## Event source has specific resource tag value

Find EC2 instances that have "dev" in any tag.

```
#
# https://docs.lacework.net/lql/restricted/lql-query-examples#event-source-has-specific-resource-tag-value
# Find EC2 instances that have dev in any tag.
#
---
queryId: Example_Global_AWS_EC2InstanceWithDevTag
queryText: |-
 { 
     source {
         CloudTrailRawEvents e,
         array_to_rows(e.EVENT:requestParameters.tagSpecificationSet.items) as (items),
         array_to_rows(items:tags) as (tags)
     } 
     filter {
         EVENT_SOURCE = 'ec2.amazonaws.com' and 
         EVENT:requestParameters.tagSpecificationSet is not null and 
         tags:value rlike '.*dev.*' and 
         ERROR_CODE is null
     } 
     return distinct {
         INSERT_ID,
         INSERT_TIME,
         EVENT_TIME,
         EVENT
     }
 }
```

## Exposed Kubernetes dashboard

Find exposed Kubernetes dashboard by URL. The query checks for exposed dashboards based on three possible URI structures:

1. Resource kind.
2. Resource kind with `?` for options.
3. Resource kind with a single `/` followed by the resource name.

```
#
# https://docs.lacework.net/lql/restricted/lql-query-examples#exposed-kubernetes-dashboard
# Find exposed Kubernetes dashboard by URL.
#
---
queryId: LW_Global_K8s_Activity_LoadBalancerExposedDashboard
queryText: |-
 {
     source {
         LW_ACT_K8S_AUDIT
     }
     filter {
         (EVENT_JSON:requestURI like '/api/v1/namespaces/%/services'
             or EVENT_JSON:requestURI rlike s'/api/v1/namespaces/[^/]*/services[?|/][^/]*$'
         )
         and EVENT_JSON:verb = 'create'
         and EVENT_JSON:requestObject.kind = 'Service'
         and EVENT_JSON:requestObject.spec."type" = 'LoadBalancer'
         and EVENT_JSON:requestObject.spec.selector."k8s-app" = 'kubernetes-dashboard'
         and EVENT_JSON:requestObject.metadata.namespace = 'kube-system'
         and EVENT_JSON:responseStatus.code between 200 and 299
     }
     return distinct {
         USER_ID,
         USER_NAME,
         USER_GROUPS,
         CLOUD_USER,
         EVENT_URI,
         EVENT_NAME,
         EVENT_SOURCE,
         EVENT_OBJECT,
         CLUSTER_TYPE,
         CLUSTER_ID,
         COMMAND
     }
 }
```

## Kubernetes system role modified or deleted

Find logged requests to update or delete the system role. Check for a colon character logged as a literal `%3A`. Also uses rlike to interpret the `%` character literally and s-string formatted string pattern. GKE manages some components internally, so exclude the addon-manager service account.

```
#
# https://docs.lacework.net/lql/restricted/lql-query-examples#kubernetes-system-role-modified-or-deleted
# Find exposed Kubernetes dashboard by URL.
#
---
queryId: LW_Global_K8s_Activity_SystemRoleModifiedOrDeleted
queryText: |-
 {
     source {
         LW_ACT_K8S_AUDIT
     }
     filter {
         (EVENT_JSON:requestURI like '/apis/rbac.authorization.k8s.io/v1/namespaces/%/roles/system:%'
         or EVENT_JSON:requestURI rlike s'/apis/rbac\.authorization\.k8s\.io/v1/namespaces/.*/roles/system%3A.*')
         and (EVENT_JSON:verb = 'patch' or EVENT_JSON:verb = 'delete')
         and EVENT_JSON:responseStatus.code between 200 and 299
         and not (CLUSTER_TYPE = "GKE" and USER_NAME = "system:addon-manager")
     }
     return distinct {
         USER_ID,
         USER_NAME,
         USER_GROUPS,
         CLOUD_USER,
         EVENT_URI,
         EVENT_NAME,
         EVENT_SOURCE,
         EVENT_OBJECT,
         CLUSTER_TYPE,
         CLUSTER_ID,
         COMMAND
     }
 }
```

## Kubernetes pod uses nonstandard registry

Find pods that use nonstandard image registry. The query checks for registry requests based on three possible URI structures:

1. Resource kind.
2. Resource kind with `?` for options.
3. Resource kind with a single `/` followed by the resource name.

```
#
# https://docs.lacework.net/lql/restricted/lql-query-examples#kubernetes-pod-uses-nonstandard-registry
# Find pods that use nonstandard image registry. 
#
---
queryId: LW_Global_K8s_Activity_PodWithNonstandardImageRegistry
queryText: |-
 {
     source {
         LW_ACT_K8S_AUDIT,
         array_to_rows(LW_ACT_K8S_AUDIT.EVENT_JSON:requestObject.spec.containers) as (containers)
     }
     filter {
         (
             EVENT_JSON:requestURI like '/api/v1/namespaces/%/pods'
             or EVENT_JSON:requestURI rlike '/api/v1/namespaces/[^/]*/pods[?|/][^/]*$'
         )
         and EVENT_JSON:responseStatus.code between 200 and 299
         and EVENT_JSON:verb = 'create'
         and EVENT_JSON:requestObject.kind = 'Pod'
         and containers:image like '%.%/%'
         and not (CLUSTER_TYPE = 'AKS' and containers:image like '%.azurecr.io/%')
         and not (CLUSTER_TYPE = 'EKS' and containers:image like '%.ecr.%.amazonaws.com/%')
         and not (CLUSTER_TYPE = 'EKS' and containers:image like '%public.ecr.aws%')
         and not (CLUSTER_TYPE = 'GKE' and containers:image like '%gcr.io/%/%')
         and (
             containers:image not like 'docker.io/%'
             or containers:image not like '%.docker.io/%'
             or containers:image not like '%.ghcr.io/%'
         )
     }
     return distinct {
         USER_ID,
         USER_NAME,
         USER_GROUPS,
         CLOUD_USER,
         EVENT_URI,
         EVENT_NAME,
         EVENT_SOURCE,
         EVENT_OBJECT,
         CLUSTER_TYPE,
         CLUSTER_ID,
         COMMAND
     }
 }
```

## Public IP addresses of EC2 instances

Returns the public IP address of all AWS EC2 instances.

```
queryId: return_IPs
queryText: |-
  {
      source {
          LW_CFG_AWS_EC2_INSTANCES
      }
      filter {
          value_exists(LW_CFG_AWS_EC2_INSTANCES.RESOURCE_CONFIG:PublicIpAddress)
          and LW_CFG_AWS_EC2_INSTANCES.RESOURCE_CONFIG:PublicIpAddress <> ''
      }
      return distinct {
          LW_CFG_AWS_EC2_INSTANCES.*
      }
  }
```
