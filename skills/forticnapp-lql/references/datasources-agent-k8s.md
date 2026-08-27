<!-- Generated from FortiCNAPP 26.2 LQL Reference Guide (fetched 2026-08-26). Source:
     https://docs.fortinet.com/document/forticnapp/latest/lql-reference/771173/datasource-metadata -->

# Datasource Metadata

## Workload Security Datasources

### LW_HA_CONNECTION_SUMMARY

Summary of connections

- `BATCH_START_TIME` (Timestamp) — Beginning of time interval
- `BATCH_END_TIME` (Timestamp) — End of time interval
- `SRC_ENTITY_TYPE` (String) — Type of entity initiating the connection
- `SRC_ENTITY_ID` (JSON) — Identifier for entity initiating the connection
- `DST_ENTITY_TYPE` (String) — Type of entity accepting the connection
- `DST_ENTITY_ID` (JSON) — Identifier for entity accepting the connection
- `SRC_IN_BYTES` (Number) — Bytes received by entity initiating the connection
- `SRC_OUT_BYTES` (Number) — Bytes sent by entity initiating the connection
- `DST_IN_BYTES` (Number) — Bytes received by entity accepting the connection
- `DST_OUT_BYTES` (Number) — Bytes sent by entity accepting the connection
- `ENDPOINT_DETAILS` (JSON) — Array of endpoint information (IPs, ports, protocol) for individual connections between entities
- `NUM_CONNS` (Number) — Total number of connections between source and destination entities

### LW_HA_DNS_REQUESTS

DNS Request information

- `BATCH_START_TIME` (Timestamp) — Beginning of time interval
- `BATCH_END_TIME` (Timestamp) — End of time interval
- `RECORD_CREATED_TIME` (Timestamp) — Record creation time
- `MID` (Number) — Machine identifier reporting the activity
- `SRV_IP_ADDR` (String) — IP address of DNS Server
- `HOSTNAME` (String) — Hostname that is being looked up
- `HOST_IP_ADDR` (String) — Resolved IP address of hostname
- `TTL` (Number) — Time to live for name resolution
- `PKTLEN` (Number) — Length of response packet

### LW_HA_FILE_CHANGES

Details about file changes

- `BATCH_START_TIME` (Timestamp) — Beginning of time interval
- `BATCH_END_TIME` (Timestamp) — End of time interval
- `ACTIVITY_START_TIME` (Timestamp) — Start Time for activity occurring
- `ACTIVITY_END_TIME` (Timestamp) — End Time for activity occurring
- `MID` (Number) — Machine identifier where the file resides
- `PATH` (String) — File path
- `ACTIVITY` (String) — Type of activity that occurred
- `FILEDATA_HASH` (String) — Hash key of file contents
- `LAST_MODIFIED_TIME` (Timestamp) — Last modified time of file
- `SIZE` (Number) — Size of file

### LW_HA_SSH_LOGINS

Details about SSH logins from authentication logs

- `BATCH_START_TIME` (TIMESTAMP) — Beginning of time interval
- `BATCH_END_TIME` (TIMESTAMP) — End of time interval
- `BATCH_ID` (STRING) — Identifier of insertion batch from agent. Useful for matching possibly related records.
- `RECORD_CREATED_TIME` (TIMESTAMP) — Record creation time
- `LOGIN_TIME` (Timestamp) — Time user login occurred
- `MID` (NUMBER) — Machine identifier
- `USERNAME` (String) — Username of the user logging in
- `IP_ADDR` (String) — IP address from which activity originated
- `HOSTNAME` (String) — Hostname for the Machine where the detected key was found
- `SSH_KEY_TYPE` (String) — Type of SSH key
- `FINGERPRINT_OPENSSH_MD5` (String) — OpenSSH MD5 fingerprint format
- `FINGERPRINT_OPENSSH_SHA256` (String) — OpenSSH SHA256 fingerprint format

### LW_HA_SYSCALLS_EXEC

System call `exec` activity

- `BATCH_START_TIME` (TIMESTAMP) — Beginning of time interval
- `BATCH_END_TIME` (TIMESTAMP) — End of time interval
- `BATCH_ID` (STRING) — Identifier of insertion batch from agent. Useful for matching possibly related records.
- `RECORD_CREATED_TIME` (TIMESTAMP) — Record creation time
- `MID` (NUMBER) — Machine identifier
- `EXE_PATH` (STRING) — Executable path that was launched
- `PID` (NUMBER) — Identifier of the process that performed the syscall
- `PID_HASH` (NUMBER) — Process hash of the process that performed the syscall
- `PPID` (NUMBER) — Parent process identifier assigned by OS
- `PPID_HASH` (NUMBER) — Unique identifier for parent process
- `CMDLINE` (STRING) — Full command line for the execution call
- `UID` (NUMBER) — User identifier of process
- `GID` (Number) — Group identifier of process
- `COUNT` (Number) — Number of repeated operations represented by this record
- `OS` (STRING) — Operating system

### LW_HA_SYSCALLS_FILE

System call `file` activity

- `BATCH_START_TIME` (TIMESTAMP) — Beginning of time interval
- `BATCH_END_TIME` (TIMESTAMP) — End of time interval
- `BATCH_ID` (STRING) — Identifier of insertion batch from agent. Useful for matching possibly related records.
- `RECORD_CREATED_TIME` (TIMESTAMP) — Record creation time
- `MID` (NUMBER) — Machine identifier
- `TARGET_TYPE` (STRING) — Type of the TARGET_PATH value ('file' or 'directory')
- `TARGET_OP` (STRING) — Operation performed on the target
- `TARGET_PATH` (STRING) — Path affected by the operation
- `WATCH_PATH` (STRING) — Path being monitored for activity
- `PID` (NUMBER) — Identifier of the process that performed the syscall
- `PID_HASH` (NUMBER) — Process hash of the process that performed the syscall
- `PPID` (NUMBER) — Parent process identifier assigned by OS
- `PPID_HASH` (NUMBER) — Unique identifier for parent process
- `UID` (NUMBER) — User identifier of process
- `GID` (Number) — Group identifier of process
- `COUNT` (Number) — Number of repeated operations represented by this record
- `OS` (STRING) — Operating system

### LW_HA_USER_LOGINS

Details about user logins

- `BATCH_START_TIME` (Timestamp) — Beginning of time interval
- `BATCH_END_TIME` (Timestamp) — End of time interval
- `RECORD_CREATED_TIME` (Timestamp) — Record creation time
- `LOGIN_TIME` (Timestamp) — Time user login occurred
- `LOGOFF_TIME` (Timestamp) — Time user logoff occurred (NULL for TYPE = 'LOGIN')
- `EVENT_TYPE` (String) — Type of event ('LOGIN' or 'LOGOFF')
- `MID` (Number) — Machine identifier reporting the activity
- `USERNAME` (String) — Username of the user logging in or off
- `HOSTNAME` (String) — Hostname from which activity originated (or IP address if hostname is unknown)
- `IP_ADDR` (String) — IP address from which activity originated
- `TTY` (String) — Terminal into which user login occurred
- `UID` (Number) — Identifier of user
- `GID` (Number) — Group identifier of user

### LW_HA_WIN_REGISTRY

Windows registry activity

- `BATCH_START_TIME` (TIMESTAMP) — Beginning of time interval
- `BATCH_END_TIME` (TIMESTAMP) — End of time interval
- `MID` (NUMBER) — Machine identifier
- `KEY_PATH` (STRING) — Registry key path
- `VALUE_NAME` (STRING) — Registry value name
- `VALUE_DATA` (STRING) — Registry value data
- `VALUE_DATA_TYPE` (STRING) — Registry value data type: string, multi-string, binaru, int64
- `OLD_NAME` (STRING) — Previous registry key path (when operation is RENAME_KEY)
- `MODIFIED_TIME` (TIMESTAMP) — Timestamp of the activity
- `OPERATION` (STRING) — Registry modifying operation: CREATE_KEY, RENAME_KEY, DELETE_KEY, DELETE_VALUE, SET_VALUE
- `PID` (NUMBER) — PID of the process that performed the operation
- `PID_HASH` (NUMBER) — PID hash of the process that performed the operation
- `EXE_PATH` (STRING) — Executable path associated with registry activity
- `USERNAME` (STRING) — Username associated with the registry activity
- `HOSTNAME` (STRING) — Hostname associated with the registry activity

### LW_HE_ACCESS_SSH_AUTHORIZED_KEYS

Public SSH key entries in `authorized_keys` files from agentless disk scanning

- `BATCH_START_TIME` (Timestamp) — Beginning of time interval
- `BATCH_END_TIME` (Timestamp) — End of time interval
- `BATCH_ID` (String) — Id of insertion batch from the scanner. Useful for matching possibly related records.
- `RECORD_CREATED_TIME` (Timestamp) — Record creation time
- `MID` (Number) — Machine ID
- `HOSTNAME` (String) — Hostname for the Machine where the detected key was found
- `IS_IN_CONTAINER` (String) — Whether the detected key was known to be from a container image, NULL if unknown
- `CONTAINER_KEY` (JSON) — Container image and layer from which the detected key originated if known
- `FILE_PATH` (String) — File path for the detected key
- `FILE_PERMISSIONS` (Number) — File permissions mask
- `FILE_CREATED_TIME` (Timestamp) — Created time of file
- `FILE_MODIFIED_TIME` (Timestamp) — Last modified time of file
- `FILE_ACCESSED_TIME` (Timestamp) — Last access time of file
- `OWNER_UID` (Timestamp) — File owner user ID
- `OWNER_GID` (Timestamp) — File owner group ID
- `SSH_KEY_TYPE` (String) — Type of SSH key
- `FINGERPRINT_OPENSSH_MD5` (String) — OpenSSH MD5 fingerprint format
- `FINGERPRINT_OPENSSH_SHA256` (String) — OpenSSH SHA256 fingerprint format
- `FINGERPRINT_RSA_MD5` (String) — RSA MD5 fingerprint format

### LW_HE_ALL_PROCESSES

Details about all processes reported on by the agent

- `BATCH_START_TIME` (Timestamp) — Beginning of time interval
- `BATCH_END_TIME` (Timestamp) — End of time interval
- `PROCESS_START_TIME` (Timestamp) — Time the process started
- `EXE_PATH` (String) — Path of the executable the process is running
- `CMDLINE` (String) — Full command line used to start the process
- `OS` (String) — Operating system
- `MID` (Number) — Machine ID on which the process was running
- `PID_HASH` (Number) — Unique identifier for process
- `PID` (Number) — Process ID assigned by OS
- `PPID_HASH` (Number) — Unique identifier for parent process
- `PPID` (Number) — Parent process ID assigned by OS
- `IS_IN_CONTAINER` (String) — Whether the process is running inside container, NULL if unknown
- `CONTAINER_ID` (String) — Unique identifier for container
- `RECORD_CREATED_TIME` (Timestamp) — Record creation time
- `PROCESS_SOURCE` (JSON) — Type of process either SYSCALL or DIRECT

### LW_HE_CONTAINERS

Details about each host container

- `BATCH_START_TIME` (Timestamp) — Beginning of time interval
- `BATCH_END_TIME` (Timestamp) — End of time interval
- `RECORD_CREATED_TIME` (Timestamp) — Record creation time
- `CONTAINER_START_TIME` (Timestamp) — Time the container started
- `MID` (Number) — Machine identifier of the container
- `CONTAINER_ID` (String) — Unique identifier for container
- `CONTAINER_TYPE` (String) — Type of container
- `IMAGE_ID` (String) — ID of the machine image this container is using
- `CONTAINER_NAME` (String) — Name of the container
- `PRIVILEGED` (Number) — Indicates whether the container is privileged. (1 = privileged, 0 = not privileged)
- `NETWORK_MODE` (String) — Mode the network is running in
- `PID_MODE` (String) — Mode for process iDs
- `IPV4` (String) — 4-byte IP address
- `IPV6` (String) — 6-byte IP address
- `LISTEN_PORT_MAP` (JSON) — Mappings for listening ports
- `VOLUME_MAP` (JSON) — Filesystem volume map
- `REPO` (String) — Repository this container came from
- `TAG` (String) — Tag for the container
- `PROPS_LABEL` (JSON) — Container labels
- `PROPS_ENV` (JSON) — Container environment settings

### LW_HE_FILES

Details about files on hosts

- `BATCH_START_TIME` (Timestamp) — Beginning of time interval
- `BATCH_END_TIME` (Timestamp) — End of time interval
- `RECORD_CREATED_TIME` (Timestamp) — Record creation time
- `MID` (Number) — Machine identifier where the file resides
- `PATH` (String) — File path
- `FILE_NAME` (String) — Name of the file (last part of PATH)
- `INODE` (Number) — Inode of file
- `FILE_TYPE` (String) — Mime type of file
- `IS_LINK` (Number) — Is the file a symbolic link?
- `LINK_DEST_PATH` (String) — Symbolic link target
- `LINK_ABS_DEST_PATH` (String) — Absolute path of symbolic link target
- `OWNER_UID` (Number) — Identifier of user that owns file
- `OWNER_USERNAME` (String) — Name of user that owns file
- `OWNER_GID` (Number) — Identifier of group that owns file
- `METADATA_HASH` (String) — Hash key of file metadata
- `FILEDATA_HASH` (String) — Hash key of file contents
- `SIZE` (Number) — File size in bytes
- `BLOCK_SIZE` (Number) — Size in bytes of a single block for this file
- `BLOCK_COUNT` (Number) — File size in blocks
- `FILE_ACCESSED_TIME` (Timestamp) — Last access time of file
- `FILE_MODIFIED_TIME` (Timestamp) — Last modified time of file
- `FILE_CREATED_TIME` (Timestamp) — Created time of file
- `FILE_PERMISSIONS` (Number) — File permissions mask
- `HARD_LINK_COUNT` (Number) — Count of hard links to this file

### LW_HE_IMAGES

Details about images found on machines

- `BATCH_START_TIME` (Timestamp) — Beginning of time interval
- `BATCH_END_TIME` (Timestamp) — End of time interval
- `RECORD_CREATED_TIME` (Timestamp) — Record creation time
- `IMAGE_CREATED_TIME` (Timestamp) — Time the image was created
- `MID` (Number) — Machine identifier where image was located
- `IMAGE_ID` (String) — Unique identifier for image
- `CONTAINER_TYPE` (String) — Type of container for the image
- `AUTHOR` (String) — Author of the image
- `REPO` (String) — Repository the image came from
- `TAG` (String) — Tag for the image
- `SIZE` (Number) — Size of the image in bytes
- `VIRTUAL_SIZE` (Number) — Size of the image in virtual memory
- `IMAGE_VERSION` (String) — Version identifier for the image
- `ACTIVE_COUNT` (Number) — Number of containers running on this image

### LW_HE_MACHINES

Details about each host machine

- `BATCH_START_TIME` (Timestamp) — Beginning of time interval
- `BATCH_END_TIME` (Timestamp) — End of time interval
- `RECORD_CREATED_TIME` (Timestamp) — Record creation time
- `MID` (Number) — Lacework machine ID
- `HOSTNAME` (String) — Machine provided hostname
- `DOMAIN` (String) — Domain machine belongs to
- `KERNEL` (String) — Name of the kernel
- `KERNEL_RELEASE` (String) — Kernel release version
- `KERNEL_VERSION` (String) — Kernel detailed version
- `OS` (String) — OS name
- `OS_VERSION` (String) — OS version
- `OS_DESC` (String) — OS description
- `CPU_INFO` (JSON) — CPU information
- `MEMORY_INFO` (JSON) — Memory information
- `MACHINE_ID` (JSON) — Machine identifier
- `LAST_BOOT_TIME` (Timestamp) — Last timestamp from machine starting
- `LAST_BOOT_REASON` (String) — Reason the machine last rebooted
- `DEFAULT_ROUTER` (String) — Default router information
- `TAGS` (JSON) — Machine provided tag information
- `KERNEL_ARGS` (String) — Arguments used for kernel
- `ROUTE` (JSON) — Route information

### LW_HE_PACKAGES

Details about each package

- `BATCH_START_TIME` (Timestamp) — Beginning of time interval
- `BATCH_END_TIME` (Timestamp) — End of time interval
- `RECORD_CREATED_TIME` (Timestamp) — Record creation time
- `MID` (Number) — Lacework machine ID
- `IS_IN_CONTAINER` (String) — Whether the package is from a container image
- `CONTAINER_KEY` (JSON) — Container image and layer from which the package originated
- `PACKAGE_NAME` (String) — Package name
- `PACKAGE_ARCH` (String) — Package architecture
- `PACKAGE_VERSION` (String) — Package version
- `VERSION_FORMAT` (String) — Type of package
- `NAMESPACE` (String) — Package namespace
- `SOURCE_FILE` (String) — File containing package metadata
- `ACTIVE` (String) — Package active, inactive, or unknown
- `CAA` (String) — Active package detection (Code Aware Agent) enabled: true, false, or unknown

### LW_HE_PROCESSES

Details about each host process

- `BATCH_START_TIME` (Timestamp) — Beginning of time interval
- `BATCH_END_TIME` (Timestamp) — End of time interval
- `RECORD_CREATED_TIME` (Timestamp) — Record creation time
- `PROCESS_START_TIME` (Timestamp) — Time the process started
- `MID` (Number) — Machine ID on which the process was running
- `PID_HASH` (Number) — Unique identifier for process
- `PID` (String) — Process ID assigned by OS
- `PPID_HASH` (Number) — Unique identifier for parent process
- `PPID` (Number) — Parent process ID assigned by OS
- `PGID` (Number) — Process Group ID assigned by OS
- `SID` (Number) — Session ID assigned by OS
- `USERNAME` (String) — Name of the user that started the process
- `EUSERNAME` (String) — Effective username currently in use for the process
- `EXE_PATH` (String) — Path of the executable used to start the process
- `CMDLINE` (String) — Full command line used to start the process
- `CWD` (String) — Initial working directory of the process
- `ROOT` (String) — Root of filesystem
- `OS` (String) — Operating system

### LW_HE_SECRETS_ALL

Secrets detected by various scanning tools

- `BATCH_START_TIME` (Timestamp) — Beginning of time interval
- `BATCH_END_TIME` (Timestamp) — End of time interval
- `BATCH_ID` (String) — Id of insertion batch from the scanner. Useful for matching possibly related records.
- `RECORD_CREATED_TIME` (Timestamp) — Record creation time
- `MID` (Number) — Machine ID
- `HOSTNAME` (String) — Hostname for the Machine where the detected key was found
- `IS_IN_CONTAINER` (String) — Whether the detected key was known to be from a container image, NULL if unknown
- `CONTAINER_KEY` (JSON) — Container image and layer from which the detected key originated if known
- `FILE_PATH` (String) — File path for the detected key
- `SECRET_TYPE` (String) — Type of detected secret
- `SECRET_METADATA` (JSON) — Metadata about the detected secret

### LW_HE_SECRETS_SSH_PRIVATE_KEYS

Instances of detected SSH private keys from agentless disk scanning

- `BATCH_START_TIME` (Timestamp) — Beginning of time interval
- `BATCH_END_TIME` (Timestamp) — End of time interval
- `BATCH_ID` (String) — Id of insertion batch from the scanner. Useful for matching possibly related records.
- `RECORD_CREATED_TIME` (Timestamp) — Record creation time
- `MID` (Number) — Machine ID
- `HOSTNAME` (String) — Hostname for the Machine where the detected key was found
- `IS_IN_CONTAINER` (String) — Whether the detected key was known to be from a container image, NULL if unknown
- `CONTAINER_KEY` (JSON) — Container image and layer from which the detected key originated if known
- `FILE_PATH` (String) — File path for the detected key
- `FILE_PERMISSIONS` (Number) — File permissions mask
- `FILE_CREATED_TIME` (Timestamp) — Created time of file
- `FILE_MODIFIED_TIME` (Timestamp) — Last modified time of file
- `FILE_ACCESSED_TIME` (Timestamp) — Last access time of file
- `OWNER_UID` (Timestamp) — File owner user Id
- `OWNER_GID` (Timestamp) — File owner group Id
- `SSH_KEY_TYPE` (String) — Type of SSH key
- `FINGERPRINT_OPENSSH_MD5` (String) — OpenSSH MD5 fingerprint format
- `FINGERPRINT_OPENSSH_SHA256` (String) — OpenSSH SHA256 fingerprint format
- `FINGERPRINT_RSA_MD5` (String) — RSA MD5 fingerprint format
- `FINGERPRINT_PKCS8_SHA1` (String) — PKCS8 fingerprint format

### LW_HE_SYSCALLS_PROCESSES

Details about processes involved in system calls

- `BATCH_START_TIME` (TIMESTAMP) — Beginning of time interval
- `BATCH_END_TIME` (TIMESTAMP) — End of time interval
- `BATCH_ID` (STRING) — Identifier of insertion batch from agent. Useful for matching possibly related records.
- `RECORD_CREATED_TIME` (TIMESTAMP) — Record creation time
- `PROCESS_START_TIME` (TIMESTAMP) — Time the process started
- `MID` (NUMBER) — Machine identifier on which the process was running
- `PID_HASH` (NUMBER) — Unique identifier for process
- `PID` (NUMBER) — Process ID assigned by OS
- `PPID_HASH` (NUMBER) — Unique identifier for parent process
- `PPID` (NUMBER) — Parent process identifier assigned by OS
- `UID` (NUMBER) — User identifier of process
- `GID` (Number) — Group identifier of process
- `EXE_PATH` (STRING) — Path of the executable the process is running
- `CMDLINE` (STRING) — Full command line used to start the process
- `PEXE_PATH` (STRING) — Path of the executable the parent process is running
- `OS` (STRING) — Operating system

### LW_HE_USERS

Details about users associated with hosts

- `BATCH_START_TIME` (Timestamp) — Beginning of time interval
- `BATCH_END_TIME` (Timestamp) — End of time interval
- `RECORD_CREATED_TIME` (Timestamp) — Record creation time
- `MID` (Number) — Machine identifier on which user was found
- `USERNAME` (String) — Username identifying the user
- `PRIMARY_GROUP_NAME` (String) — Primary group user belongs to
- `OTHER_GROUP_NAMES` (JSON) — Array of other groups for user
- `HOME_DIR` (String) — Home directory of user


## Attack Path Analysis Datasources

Query the following datasources for information about Attack Path Analysis.

### LW_APA_ATTACK_PATHS

Details about cloud resource attack paths

- `RECORD_CREATED_TIME` (Timestamp) — Record creation time
- `PATH_ID` (String) — Path ID
- `PROVIDER_TYPE` (String) — Cloud or service domain provider
- `DOMAIN_ID` (String) — Domain identifier within the provider type
- `METRICS` (JSON) — Path metrics
| Path | JSON | Path elements |
- `TARGETS` (JSON) — Path targets

### LW_APA_EXPOSURE_PATHS

Details about cloud resource exposure paths

- `RECORD_CREATED_TIME` (Timestamp) — Record creation time
- `PATH_ID` (String) — Path ID
- `PATH_TYPE` (String) — Path type
- `PROVIDER_TYPE` (String) — Cloud or service domain provider
- `DOMAIN_ID` (String) — Domain identifier within the provider type
- `METRICS` (JSON) — Path metrics
- `TARGET_ID` (String) — Target ID
- `TARGET_TYPE` (String) — Target type
- `TARGET_TAGS` (JSON) — Target resource tags


## Cloud Entitlement Datasources

### LW_CE_ENTITLEMENTS

Details about cloud entitlements associated with identities

- `RECORD_CREATED_TIME` (Timestamp) — Record creation time
- `PRINCIPAL_ID` (String) — Identity principal ID
- `PROVIDER_TYPE` (String) — Cloud or service domain provider
- `DOMAIN_ID` (String) — Domain identifier within the provider type
- `SERVICE` (JSON) — Service name
- `RESOURCE_TYPE` (String) — Resource type
- `RESOURCE_ID` (String) — Resource identifier
- `POLICY_ID` (String) — Policy identifier
- `ACTION` (String) — Action
- `LAST_USED_TIME` (Timestamp) — Last used time

### LW_CE_IDENTITIES

Details about cloud identities

- `RECORD_CREATED_TIME` (Timestamp) — Record creation time
- `PRINCIPAL_ID` (String) — Identity principal ID
- `PROVIDER_TYPE` (String) — Cloud or service domain provider
- `DOMAIN_ID` (String) — Domain identifier within the provider type
- `NAME` (JSON) — Friendly name for the identity
- `LAST_USED_TIME` (Timestamp) — Last used time
- `CREATED_TIME` (Timestamp) — Created time
- `METRICS` (JSON) — Metrics data from computed entitlements and configuration
- `TAGS` (JSON) — Tags
- `ACCESS_KEYS` (JSON) — Access key summaries

### LW_CE_LINKED_IDENTITIES

Details about cloud linked identities

- `RECORD_CREATED_TIME` (Timestamp) — Record creation time
- `PRINCIPAL_ID` (String) — Identity principal ID
- `NAME` (JSON) — Friendly name for the identity
- `LINKED_PRINCIPAL_ID` (String) — Linked identity principal ID
- `LINKED_NAME` (JSON) — Friendly name for the linked identity
- `RELATION_TYPE` (String) — Type of linked relationship

### LW_CE_REMEDIATIONS

Details about cloud identity remediations

- `RECORD_CREATED_TIME` (Timestamp) — Record creation time
- `REMEDIATION_KEYS` (JSON) — Identity principal ID
- `REMEDIATION_TYPE` (String) — Type of remediation
- `METRICS` (JSON) — Metrics data from computed remediation effect
