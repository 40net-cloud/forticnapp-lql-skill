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

### Service Catalog AppRegistry

- `LW_CFG_AWS_SERVICECATALOG_APPREGISTRY_APPLICATIONS` — servicecatalog-appregistry `list-applications`
- `LW_CFG_AWS_SERVICECATALOG_APPREGISTRY_ASSOCIATED_ATTRIBUTE_GROUPS` — servicecatalog-appregistry `list-associated-attribute-groups`
- `LW_CFG_AWS_SERVICECATALOG_APPREGISTRY_ASSOCIATED_RESOURCES` — servicecatalog-appregistry `list-associated-resources`
- `LW_CFG_AWS_SERVICECATALOG_APPREGISTRY_ATTRIBUTE_GROUPS` — servicecatalog-appregistry `list-attribute-groups`
- `LW_CFG_AWS_SERVICECATALOG_APPREGISTRY_ATTRIBUTE_GROUPS_FOR_APPLICATION` — servicecatalog-appregistry `list-attribute-groups-for-application`
- `LW_CFG_AWS_SERVICECATALOG_APPREGISTRY_GET_APPLICATION` — servicecatalog-appregistry `get-application`
- `LW_CFG_AWS_SERVICECATALOG_APPREGISTRY_GET_ASSOCIATED_RESOURCE` — servicecatalog-appregistry `get-associated-resource`
- `LW_CFG_AWS_SERVICECATALOG_APPREGISTRY_GET_ATTRIBUTE_GROUP` — servicecatalog-appregistry `get-attribute-group`

### Simple Email Service version 1 and 2

- `LW_CFG_AWS_SES_ACTIVE_RECEIPT_RULE_SET` — SES `describe-active-receipt-rule-set`
- `LW_CFG_AWS_SES_RECEIPT_FILTERS` — SES `list-receipt-filters`
- `LW_CFG_AWS_SES_RECEIPT_RULE_SETS` — SES `list-receipt-rule-sets`
- `LW_CFG_AWS_SESV2_CONFIGURATION_SETS` — SESv2 `list-configuration-sets`
- `LW_CFG_AWS_SESV2_CONTACTS` — Results from Amazon Simple Email Service 'list-contacts'
- `LW_CFG_AWS_SESV2_CONTACT_LISTS` — Results from Amazon Simple Email Service 'list-contact-lists'
- `LW_CFG_AWS_SESV2_CUSTOM_VERIFICATION_EMAIL_TEMPLATES` — Results from Amazon Simple Email Service 'list-custom-verification-email-templates'
- `LW_CFG_AWS_SESV2_DEDICATED_IP_POOLS` — SESv2 `list-dedicated-ip-pools`
- `LW_CFG_AWS_SESV2_EMAIL_IDENTITIES` — Results from Amazon Simple Email Service 'list-email-identities'
- `LW_CFG_AWS_SESV2_EMAIL_TEMPLATES` — Results from Amazon Simple Email Service 'list-email-templates'
- `LW_CFG_AWS_SESV2_EXPORT_JOBS` — Results from Amazon Simple Email Service 'list-export-jobs'
- `LW_CFG_AWS_SESV2_GET_CONTACT` — Results from Amazon Simple Email Service 'get-contact'
- `LW_CFG_AWS_SESV2_GET_CONFIGURATION_SET` — SESv2 `get-configuration-set`
- `LW_CFG_AWS_SESV2_GET_CONFIGURATION_SET_EVENT_DESTINATIONS` — SESv2 `get-configuration-set-event-destinations`
- `LW_CFG_AWS_SESV2_GET_CONTACT_LIST` — Results from Amazon Simple Email Service 'get-contact-list'
- `LW_CFG_AWS_SESV2_GET_CUSTOM_VERIFICATION_EMAIL_TEMPLATE` — Results from Amazon Simple Email Service 'get-custom-verification-email-template'
- `LW_CFG_AWS_SESV2_GET_EMAIL_IDENTITY` — Results from Amazon Simple Email Service 'get-email-identity'
- `LW_CFG_AWS_SESV2_GET_EMAIL_IDENTITY_POLICIES` — Results from Amazon Simple Email Service 'get-email-identity-policies'
- `LW_CFG_AWS_SESV2_GET_EMAIL_TEMPLATE` — Results from Amazon Simple Email Service 'get-email-template'
- `LW_CFG_AWS_SESV2_GET_EXPORT_JOB` — Results from Amazon Simple Email Service 'get-export-job'
- `LW_CFG_AWS_SESV2_GET_IMPORT_JOB` — Results from Amazon Simple Email Service 'get-import-job'
- `LW_CFG_AWS_SESV2_GET_MULTI_REGION_ENDPOINT` — Results from Amazon Simple Email Service 'get-multi-region-endpoint'
- `LW_CFG_AWS_SESV2_GET_SUPPRESSED_DESTINATION` — Results from Amazon Simple Email Service 'get-suppressed-destination'
- `LW_CFG_AWS_SESV2_IMPORT_JOBS` — Results from Amazon Simple Email Service 'list-import-jobs'
- `LW_CFG_AWS_SESV2_MULTI_REGION_ENDPOINTS` — Results from Amazon Simple Email Service 'list-multi-region-endpoints'
- `LW_CFG_AWS_SESV2_RECOMMENDATIONS` — Results from Amazon Simple Email Service 'list-recommendations'
- `LW_CFG_AWS_SESV2_SUPPRESSED_DESTINATIONS` — Results from Amazon Simple Email Service 'list-suppressed-destinations'

### SNS

- `LW_CFG_AWS_SNS_GET_DATA_PROTECTION_POLICY` — Amazon Simple Notification Service `get-data-protection-policy`
- `LW_CFG_AWS_SNS_GET_SUBSCRIPTION_ATTRIBUTES` — Amazon Simple Notification Service `get-subscription-attributes`
- `LW_CFG_AWS_SNS_GET_TOPIC_ATTRIBUTES` — Amazon Simple Notification Service `get-topic-attributes`
- `LW_CFG_AWS_SNS_PLATFORM_APPLICATIONS` — Amazon Simple Notification Service `list-platform-applications`
- `LW_CFG_AWS_SNS_SUBSCRIPTIONS` — Amazon Simple Notification Service `list-subscriptions`
- `LW_CFG_AWS_SNS_TOPICS` — Amazon Simple Notification Service `list-topics`

### SQS

- `LW_CFG_AWS_SQS_QUEUES` — sqs `list-queues`
- `LW_CFG_AWS_SQS_QUEUE_ATTRIBUTES` — sqs `get-queue-attributes`

### SSM

- `LW_CFG_AWS_SSM_DESCRIBE_DOCUMENT` — Amazon Simple Systems Manager (SSM) `describe-document`
- `LW_CFG_AWS_SSM_DESCRIBE_DOCUMENT_PERMISSION` — Amazon Simple Systems Manager (SSM) `describe-document-permission`
- `LW_CFG_AWS_SSM_DOCUMENTS` — Amazon Simple Systems Manager (SSM) `list-documents`
- `LW_CFG_AWS_SSM_INSTANCE_ASSOCIATIONS_STATUS` — Amazon Simple Systems Manager (SSM) `describe-instance-associations-status`
- `LW_CFG_AWS_SSM_INSTANCE_INFORMATION` — Amazon Simple Systems Manager (SSM) `describe-instance-information`
- `LW_CFG_AWS_SSM_INSTANCE_PATCHES` — Amazon Simple Systems Manager (SSM) `describe-instance-patches`
- `LW_CFG_AWS_SSM_PARAMETERS` — Amazon Simple Systems Manager (SSM) `describe-parameters`
- `LW_CFG_AWS_SSM_GET_CONNECTION_STATUS` — Amazon Simple Systems Manager (SSM) `get-connection-status`
- `LW_CFG_AWS_SSM_SESSIONS` — Amazon Simple Systems Manager (SSM) `describe-sessions`

### SSO

- `LW_CFG_AWS_SSO_ADMIN_ACCOUNTS_FOR_PROVISIONED_PERMISSION_SET` — AWS Single Sign-On Admin `list-accounts-for-provisioned-permission-set`
- `LW_CFG_AWS_SSO_ADMIN_ACCOUNT_ASSIGNMENTS` — AWS Single Sign-On Admin `list-account-assignments`
- `LW_CFG_AWS_SSO_ADMIN_ACCOUNT_ASSIGNMENT_CREATION_STATUS` — AWS Single Sign-On Admin `list-account-assignment-creation-status`
- `LW_CFG_AWS_SSO_ADMIN_ACCOUNT_ASSIGNMENT_DELETION_STATUS` — AWS Single Sign-On Admin `list-account-assignment-deletion-status`
- `LW_CFG_AWS_SSO_ADMIN_CUSTOMER_MANAGED_POLICY_REFERENCES_IN_PERMISSION_SET` — AWS Single Sign-On Admin `list-customer-managed-policy-references-in-permission-set`
- `LW_CFG_AWS_SSO_ADMIN_DESCRIBE_ACCOUNT_ASSIGNMENT_CREATION_STATUS` — AWS Single Sign-On Admin `describe-account-assignment-creation-status`
- `LW_CFG_AWS_SSO_ADMIN_DESCRIBE_ACCOUNT_ASSIGNMENT_DELETION_STATUS` — AWS Single Sign-On Admin `describe-account-assignment-deletion-status`
- `LW_CFG_AWS_SSO_ADMIN_DESCRIBE_INSTANCE_ACCESS_CONTROL_ATTRIBUTE_CONFIGURATION` — AWS Single Sign-On Admin `describe-instance-access-control-attribute-configuration`
- `LW_CFG_AWS_SSO_ADMIN_DESCRIBE_PERMISSION_SET` — AWS Single Sign-On Admin `describe-permission-set`
- `LW_CFG_AWS_SSO_ADMIN_GET_INLINE_POLICY_FOR_PERMISSION_SET` — AWS Single Sign-On Admin `get-inline-policy-for-permission-set`
- `LW_CFG_AWS_SSO_ADMIN_GET_PERMISSIONS_BOUNDARY_FOR_PERMISSION_SET` — AWS Single Sign-On Admin `get-permissions-boundary-for-permission-set`
- `LW_CFG_AWS_SSO_ADMIN_INSTANCES` — AWS Single Sign-On Admin `list-instances`
- `LW_CFG_AWS_SSO_ADMIN_MANAGED_POLICIES_IN_PERMISSION_SET` — AWS Single Sign-On Admin `list-managed-policies-in-permission-set`
- `LW_CFG_AWS_SSO_ADMIN_PERMISSION_SETS` — AWS Single Sign-On Admin `list-permission-sets`
- `LW_CFG_AWS_SSO_ADMIN_PERMISSION_SET_PROVISIONING_STATUS` — AWS Single Sign-On Admin `list-permission-set-provisioning-status`

### SSO Identity Store

- `LW_CFG_AWS_IDENTITYSTORE_GROUPS` — AWS SSO Identity Store `list-groups`
- `LW_CFG_AWS_IDENTITYSTORE_GROUP_MEMBERSHIPS` — AWS SSO Identity Store `list-group-memberships`
- `LW_CFG_AWS_IDENTITYSTORE_GROUP_MEMBERSHIPS_FOR_MEMBER` — AWS SSO Identity Store `list-group-memberships-for-member`
- `LW_CFG_AWS_IDENTITYSTORE_USERS` — AWS SSO Identity Store `list-users`

### Step Functions

- `LW_CFG_AWS_STEPFUNCTIONS_DESCRIBE_STATE_MACHINE` — AWS Step Functions `describe-state-machine`
- `LW_CFG_AWS_STEPFUNCTIONS_STATE_MACHINES` — AWS Step Functions `list-state-machines`

### Transfer Family

- `LW_CFG_AWS_TRANSFER_ACCESSES` — transfer `list-accesses`
- `LW_CFG_AWS_TRANSFER_AGREEMENTS` — transfer `list-agreements`
- `LW_CFG_AWS_TRANSFER_CERTIFICATES` — transfer `list-certificates`
- `LW_CFG_AWS_TRANSFER_CONNECTORS` — transfer `list-connectors`
- `LW_CFG_AWS_TRANSFER_DESCRIBE_ACCESS` — transfer `describe-access`
- `LW_CFG_AWS_TRANSFER_DESCRIBE_AGREEMENT` — transfer `describe-agreement`
- `LW_CFG_AWS_TRANSFER_DESCRIBE_CERTIFICATE` — transfer `describe-certificate`
- `LW_CFG_AWS_TRANSFER_DESCRIBE_CONNECTOR` — transfer `describe-connector`
- `LW_CFG_AWS_TRANSFER_DESCRIBE_EXECUTION` — transfer `describe-execution`
- `LW_CFG_AWS_TRANSFER_DESCRIBE_HOST_KEY` — transfer `describe-host-key`
- `LW_CFG_AWS_TRANSFER_DESCRIBE_PROFILE` — transfer `describe-profile`
- `LW_CFG_AWS_TRANSFER_DESCRIBE_SECURITY_POLICY` — transfer `describe-security-policy`
- `LW_CFG_AWS_TRANSFER_DESCRIBE_SERVER` — transfer `describe-server`
- `LW_CFG_AWS_TRANSFER_DESCRIBE_USER` — transfer `describe-user`
- `LW_CFG_AWS_TRANSFER_DESCRIBE_WEB_APP` — transfer `describe-web-app`
- `LW_CFG_AWS_TRANSFER_DESCRIBE_WEB_APP_CUSTOMIZATION` — transfer `describe-web-app-customization`
- `LW_CFG_AWS_TRANSFER_DESCRIBE_WORKFLOW` — transfer `describe-workflow`
- `LW_CFG_AWS_TRANSFER_EXECUTIONS` — transfer `list-executions`
- `LW_CFG_AWS_TRANSFER_HOST_KEYS` — transfer `list-host-keys`
- `LW_CFG_AWS_TRANSFER_PROFILES` — transfer `list-profiles`
- `LW_CFG_AWS_TRANSFER_SECURITY_POLICIES` — transfer `list-security-policies`
- `LW_CFG_AWS_TRANSFER_SERVERS` — transfer `list-servers`
- `LW_CFG_AWS_TRANSFER_USERS` — transfer `list-users`
- `LW_CFG_AWS_TRANSFER_WEB_APPS` — transfer `list-web-apps`
- `LW_CFG_AWS_TRANSFER_WORKFLOWS` — transfer `list-workflows`

### User Notifications

- `LW_CFG_AWS_NOTIFICATIONS_CHANNELS` — Results from AWS User Notifications 'list-channels'
- `LW_CFG_AWS_NOTIFICATIONS_EVENT_RULES` — Results from AWS User Notifications 'list-event-rules'
- `LW_CFG_AWS_NOTIFICATIONS_GET_EVENT_RULE` — Results from AWS User Notifications 'get-event-rule'
- `LW_CFG_AWS_NOTIFICATIONS_GET_NOTIFICATION_CONFIGURATION` — Results from AWS User Notifications 'get-notification-configuration'
- `LW_CFG_AWS_NOTIFICATIONS_GET_NOTIFICATION_EVENT` — Results from AWS User Notifications 'get-notification-event'
- `LW_CFG_AWS_NOTIFICATIONS_NOTIFICATION_CONFIGURATIONS` — Results from AWS User Notifications 'list-notification-configurations'
- `LW_CFG_AWS_NOTIFICATIONS_NOTIFICATION_EVENTS` — Results from AWS User Notifications 'list-notification-events'
- `LW_CFG_AWS_NOTIFICATIONS_NOTIFICATION_HUBS` — Results from AWS User Notifications 'list-notification-hubs'

### WAF

- `LW_CFG_AWS_WAF_ACTIVATED_RULES_IN_RULE_GROUP` — AWS WAF `list-activated-rules-in-rule-group`
- `LW_CFG_AWS_WAF_BYTE_MATCH_SETS` — AWS WAF `list-byte-match-sets`
- `LW_CFG_AWS_WAF_GEO_MATCH_SETS` — AWS WAF `list-geo-match-sets`
- `LW_CFG_AWS_WAF_GET_BYTE_MATCH_SET` — AWS WAF `get-byte-match-set`
- `LW_CFG_AWS_WAF_GET_GEO_MATCH_SET` — AWS WAF `get-geo-match-set`
- `LW_CFG_AWS_WAF_GET_IP_SET` — AWS WAF `get-ip-set`
- `LW_CFG_AWS_WAF_GET_LOGGING_CONFIGURATION` — AWS WAF `get-logging-configuration`
- `LW_CFG_AWS_WAF_LOGGING_CONFIGURATIONS` — AWS WAF `list-logging-configurations`
- `LW_CFG_AWS_WAF_GET_PERMISSION_POLICY` — AWS WAF `get-permission-policy`
- `LW_CFG_AWS_WAF_GET_RATE_BASED_RULE` — AWS WAF `get-rate-based-rule`
- `LW_CFG_AWS_WAF_GET_RATE_BASED_RULE_MANAGED_KEYS` — AWS WAF `get-rate-based-rule-managed-keys`
- `LW_CFG_AWS_WAF_GET_REGEX_MATCH_SET` — AWS WAF `get-regex-match-set`
- `LW_CFG_AWS_WAF_GET_REGEX_PATTERN_SET` — AWS WAF `get-regex-pattern-set`
- `LW_CFG_AWS_WAF_GET_RULE` — AWS WAF `get-rule`
- `LW_CFG_AWS_WAF_GET_RULE_GROUP` — AWS WAF `get-rule-group`
- `LW_CFG_AWS_WAF_GET_SIZE_CONSTRAINT_SET` — AWS WAF `get-size-constraint-set`
- `LW_CFG_AWS_WAF_GET_SQL_INJECTION_MATCH_SET` — AWS WAF `get-sql-injection-match-set`
- `LW_CFG_AWS_WAF_GET_WEB_ACL` — AWS WAF `get-web-acl`
- `LW_CFG_AWS_WAF_GET_XSS_MATCH_SET` — AWS WAF `get-xss-match-set`
- `LW_CFG_AWS_WAF_IP_SETS` — waf `list-ip-sets`
- `LW_CFG_AWS_WAF_RATE_BASED_RULES` — AWS WAF `list-rate-based-rules`
- `LW_CFG_AWS_WAF_REGEX_MATCH_SETS` — AWS WAF `list-regex-match-sets`
- `LW_CFG_AWS_WAF_REGEX_PATTERN_SETS` — waf `list-regex-pattern-sets`
- `LW_CFG_AWS_WAF_RULES` — AWS WAF `list-rules`
- `LW_CFG_AWS_WAF_RULE_GROUPS` — AWS WAF `list-rule-groups`
- `LW_CFG_AWS_WAF_SIZE_CONSTRAINT_SETS` — AWS WAF `list-size-constraint-sets`
- `LW_CFG_AWS_WAF_SQL_INJECTION_MATCH_SETS` — AWS WAF `list-sql-injection-match-sets`
- `LW_CFG_AWS_WAF_WEB_ACLS` — AWS WAF `list-web-acls`
- `LW_CFG_AWS_WAF_XSS_MATCH_SETS` — AWS WAF `list-xss-match-sets`

### WAF Regional

- `LW_CFG_AWS_WAF_REGIONAL_ACTIVATED_RULES_IN_RULE_GROUP` — Results from AWS WAF Regional 'list-activated-rules-in-rule-group'
- `LW_CFG_AWS_WAF_REGIONAL_BYTE_MATCH_SETS` — Results from AWS WAF Regional 'list-byte-match-sets'
- `LW_CFG_AWS_WAF_REGIONAL_GEO_MATCH_SETS` — Results from AWS WAF Regional 'list-geo-match-sets'
- `LW_CFG_AWS_WAF_REGIONAL_GET_BYTE_MATCH_SET` — Results from AWS WAF Regional 'get-byte-match-set'
- `LW_CFG_AWS_WAF_REGIONAL_GET_GEO_MATCH_SET` — Results from AWS WAF Regional 'get-geo-match-set'
- `LW_CFG_AWS_WAF_REGIONAL_GET_IP_SET` — Results from AWS WAF Regional 'get-ip-set'
- `LW_CFG_AWS_WAF_REGIONAL_GET_LOGGING_CONFIGURATION` — Results from AWS WAF Regional 'get-logging-configuration'
- `LW_CFG_AWS_WAF_REGIONAL_GET_PERMISSION_POLICY` — Results from AWS WAF Regional 'get-permission-policy'
- `LW_CFG_AWS_WAF_REGIONAL_GET_RATE_BASED_RULE` — Results from AWS WAF Regional 'get-rate-based-rule'
- `LW_CFG_AWS_WAF_REGIONAL_GET_REGEX_MATCH_SET` — Results from AWS WAF Regional 'get-regex-match-set'
- `LW_CFG_AWS_WAF_REGIONAL_GET_REGEX_PATTERN_SET` — Results from AWS WAF Regional 'get-regex-pattern-set'
- `LW_CFG_AWS_WAF_REGIONAL_GET_RULE` — AWS WAF Regional `get-rule`
- `LW_CFG_AWS_WAF_REGIONAL_GET_RULE_GROUP` — AWS WAF Regional `get-rule-group`
- `LW_CFG_AWS_WAF_REGIONAL_GET_SIZE_CONSTRAINT_SET` — Results from AWS WAF Regional 'get-size-constraint-set'
- `LW_CFG_AWS_WAF_REGIONAL_GET_SQL_INJECTION_MATCH_SET` — Results from AWS WAF Regional 'get-sql-injection-match-set'
- `LW_CFG_AWS_WAF_REGIONAL_GET_WEB_ACL` — AWS WAF Regional `get-web-acl`
- `LW_CFG_AWS_WAF_REGIONAL_GET_XSS_MATCH_SET` — Results from AWS WAF Regional 'get-xss-match-set'
- `LW_CFG_AWS_WAF_REGIONAL_IP_SETS` — Results from AWS WAF Regional 'list-ip-sets'
- `LW_CFG_AWS_WAF_REGIONAL_RATE_BASED_RULES` — Results from AWS WAF Regional 'list-rate-based-rules'
- `LW_CFG_AWS_WAF_REGIONAL_REGEX_MATCH_SETS` — Results from AWS WAF Regional 'list-regex-match-sets'
- `LW_CFG_AWS_WAF_REGIONAL_REGEX_PATTERN_SETS` — Results from AWS WAF Regional 'list-regex-pattern-sets'
- `LW_CFG_AWS_WAF_REGIONAL_RESOURCES_FOR_WEB_ACL` — AWS WAF Regional `list-resources-for-web-acl`
- `LW_CFG_AWS_WAF_REGIONAL_RULE_GROUPS` — AWS WAF Regional `list-rule-groups`
- `LW_CFG_AWS_WAF_REGIONAL_RULES` — AWS WAF Regional `list-rules`
- `LW_CFG_AWS_WAF_REGIONAL_SIZE_CONSTRAINT_SETS` — Results from AWS WAF Regional 'list-size-constraint-sets'
- `LW_CFG_AWS_WAF_REGIONAL_SQL_INJECTION_MATCH_SETS` — Results from AWS WAF Regional 'list-sql-injection-match-sets'
- `LW_CFG_AWS_WAF_REGIONAL_WEB_ACLS` — AWS WAF Regional `list-web-acls`
- `LW_CFG_AWS_WAF_REGIONAL_XSS_MATCH_SETS` — Results from AWS WAF Regional 'list-xss-match-sets'

### WAF V2

- `LW_CFG_AWS_WAFV2_GET_LOGGING_CONFIGURATION` — wafv2 `get-logging-configuration`
- `LW_CFG_AWS_WAFV2_GET_WEB_ACL` — wafv2 `get-web-acl`
- `LW_CFG_AWS_WAFV2_IP_SETS` — wafv2 `list-ip-sets`
- `LW_CFG_AWS_WAFV2_LIST_RESOURCES_FOR_WEB_ACL` — wafv2 `list-resources-for-web-acl`
- `LW_CFG_AWS_WAFV2_REGEX_PATTERN_SETS` — wafv2 `list-regex-pattern-sets`
- `LW_CFG_AWS_WAFV2_RULE_GROUPS` — wafv2 `list-rule-groups`
- `LW_CFG_AWS_WAFV2_WEB_ACLS` — wafv2 `list-web-acls`

### WorkSpaces

- `LW_CFG_AWS_WORKSPACES_DESCRIBE_WORKSPACES` — AWS Workspaces `describe-workspaces`
- `LW_CFG_AWS_WORKSPACES_WORKSPACES` — Results from Amazon WorkSpaces 'describe-workspaces'
