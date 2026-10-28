<!-- Generated from FortiCNAPP 26.2 LQL Reference Guide (fetched 2026-10-28). Source:
     https://docs.fortinet.com/document/forticnapp/latest/lql-reference/842922/query-types -->

# Query Types

## Single Datasource

Filter and return results from a single datasource.

The example returns CloudTrail trails that do not have log file validation enabled.

```
 {
     source {
         LW_CFG_AWS_CLOUDTRAIL
     }
     filter {
         RESOURCE_CONFIG:LogFileValidationEnabled = 'false'
     }
     return distinct {
         ACCOUNT_ALIAS,
         ACCOUNT_ID,
         ARN as RESOURCE_KEY,
         RESOURCE_REGION,
         RESOURCE_TYPE,
         SERVICE,
         'CloudTrailLogFileValidationNotEnabled' as COMPLIANCE_FAILURE_REASON
     }
 }
```

## Join

Join two or more datasources.

The example returns IAM users that have inline policies.

```
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

## Semi-join (in / not in)

Locate results that are or are not in the results of a sub-query.

The example returns accounts that do not have any role with the AWSSupportAccess policy attached.

```
 {
     source {
         LW_CFG_AWS_ACCOUNTS
     }
     filter {
         not (ACCOUNT_ID in {
             source {
                 LW_CFG_AWS_IAM_ROLES_LIST_ATTACHED_POLICIES
             }
             filter {
                 RESOURCE_CONFIG:PolicyName = 'AWSSupportAccess'
             }
             return distinct {
                 ACCOUNT_ID
             }
         })
     }
     return distinct {
         ACCOUNT_ALIAS,
         ACCOUNT_ID,
         ACCOUNT_ID as RESOURCE_KEY,
         RESOURCE_REGION,
         RESOURCE_TYPE,
         SERVICE,
         'SupportRoleNotCreated' as COMPLIANCE_FAILURE_REASON
     }
 }
```
