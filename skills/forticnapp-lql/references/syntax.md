<!-- Generated from FortiCNAPP 26.2 LQL Reference Guide (fetched 2026-10-28). Source:
     https://docs.fortinet.com/document/forticnapp/latest/lql-reference/598361/lql-overview -->

# LQL Overview

The Lacework Query Language (LQL) is an SQL-like query language for specifying the selection, filtering, and manipulation of data. Queries let you interactively request information from curated datasources. Queries have a defined structure for authoring detections.

LQL enables you to find non-compliant resources or suspicious activity by querying data ingested from cloud providers, Kubernetes, CloudTrail activity logs, and the Lacework agent. Then you can associate queries with policies, which contain rich reporting metadata.

> **Note:** For information on available datasources, see Datasource Metadata.

## Example Query

The following comes from Lacework's implementation of a query:

```
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

The query is delimited by `{ }` and contains three sections:

* `source` is the data you are querying (the datasources where the query looks for data). The example's `source` is the `LW_CFG_AWS_EC2_EBS_ENCRYPTION_BY_DEFAULT` datasource. LQL queries can specify other datasources and connect multiple datasources, so you can configure custom policies to target the necessary datasources.
* `filter` specifies the data you are looking for (i.e. the records of interest). The example's `filter` specifies the records available in `LW_CFG_AWS_EC2_EBS_ENCRYPTION_BY_DEFAULT` for those whose resource config for `EbsEncryptionByDefault = 'false'`.
* `return` is the information you need to return (i.e. the fields the query exposes). The example's `return` lists several fields. Because there may be unwanted duplicates among result records when Lacework composes them from just a small number of columns, the query includes the `distinct` modifier. This behaves like an SQL `SELECT DISTINCT`. Each returned column in this case is a field that is present in the query, but results can be composed by manipulating strings, dates, JSON, and numbers as well.

The resulting data is depicted as a table. The table's columns are named based on the columns selected. If desired, you could *alias* them to other names as well.

For more LQL query examples, see Example Queries. You can also learn more about using LQL in custom policies in Create Policies with the Lacework API and Create Policies with the Lacework CLI.

## Data Types

LQL processes and produces typed data. The data types currently supported or handled are:

* String, identified in LQL by `String`
* Timestamp, identified in LQL by `Timestamp`
* Number, identified in LQL by `Number`
* JSON, identified in LQL by `Json`
* Boolean
* Null

These identifiers are case-insensitive within LQL. For example, you can write `STRING` or `string`.

Though Boolean is a data type processed by LQL, it cannot be returned from a datasource.

In processing, data may be *coerced* into another type. Coercion means that the system performs the conversion on your behalf, without you needing to specify a conversion. A `null` identifier can be coerced to be used as another type. In general, a value from JSON can be automatically coerced into a value of one of the other types if it is the correct kind of JSON value. (A JSON number can be automatically coerced into a number, a JSON string value into a string, etc.)

## Syntax and Semantics

### General Layout

LQL is syntax-oriented. Whitespace has no meaning other than to separate symbols. This means you can use an outline format, as depicted in the first example, or put the entire query on a single line.

### Character limit

LQL queries have a maximum character limit of 72,000 characters.

### Case Sensitivity

Keywords in LQL are case-insensitive. For example, `FILTER` and `filter` mean the same thing.

### Reserved Keywords

The following keywords are reserved. Attempting to use them as names in your own queries causes an error. If these words appear in JSON paths within queries, be sure to enclose them in double quotes.

* EXPR
* JOIN
* LIMIT
* OUTER
* PARAMINFO
* PROPERTIES
* SELECT
* SQL
* TYPE
* VARIANT
* WHERE

### Identifiers

Identifiers in LQL start with a letter and can contain letters, digits, and the underscore character. Two examples are `LW_CFG_AWS_EC2_EBS_ENCRYPTION_BY_DEFAULT` and `ACCOUNT_ALIAS`.

> **Note:** LQL identifiers are case-sensitive. That is, `ACCOUNT_ALIAS` and `account_alias` are two different identifiers, and a column that is named with one of them cannot be accessed by the other.

### Comments

`--` and `//` start a single line comment. Text between `--` or `//` and the end of the line is ignored.

`/*` starts a multiline comment and `*/` ends a multiline comment. The text between `/*` and `*/` is ignored.

### Strings

You can express strings in LQL in either s-string or double-quoted string format.

> **Note:** The use of the legacy string format, single-quoted strings, is supported but discouraged.

#### S-string

The s-string format begin with an *s* character followed by the single-quoted string.

This type of string does not support escape codes; all characters are treated literally. The string is delimited by single-quote characters, `'`. Single quotes are expressed using a double delimiter `''`.

For example, `s'iam.amazonaws.com'` encodes the literal string `iam.amazonaws.com`, and `s'That''s amazing'` encodes `That's amazing`.

#### Double-quoted strings

Double-quoted strings support escape sequences, for example, `"Hello\nWorld"`

Supported escape sequences for double-quotes strings are as follows:

| Escape Sequence | Hex interpretation | Character |
| --- | --- | --- |
| `\"` | 0x22 | Double quote |
| `\\` | 0x5c | Backslash |
| `\b` | 0x08 | Backspace |
| `\f` | 0x0c | Form Feed |
| `\n` | 0x0a | Line feed |
| `\r` | 0x0d | Carriage return |
| `\t` | 0x09 | Horizontal tab |
| `\uHHHH` |  | Unicode (each H represents a hexadecimal digit) |

As shown, you can express double-quotes within a string by escaping them: `\"`. Unrecognized escape sequences produce an error at compile time.

### Numbers

Literal numbers in LQL are either integral or decimal.

### Boolean Values

The symbols `true` and `false` represent their Boolean logic counterparts.

### Null

The symbol `null` represents the absence of a known value. You can return it explicitly from various functions such as `CASE` and `COALESCE`. As with SQL, you will test for something being null with `is null` rather than `= null`.

`Null` occurs both in columns of data and in JSON objects. It is important to note that `null` for functions and data columns are treated differently than a JSON `null` (as in `{"ERROR_CODE": null}`). Therefore, `null` and `"JSON null"` are different things. There is no symbol in LQL for a JSON `null`. For more information, see documentation on the `is null` and `is JSON null` comparisons and the `key_exists` function.

## Referring to Data

All datasources that are sources for LQL, and all datasources produced by LQL, have named columns (referred to as *fields*).

Every datasource is a namespace for its columns. If you write a query that refers to the `LW_CFG_AWS_EC2_EBS_ENCRYPTION_BY_DEFAULT` datasource, you can refer to its ACCOUNT_ID field as either `ACCOUNT_ID` or `LW_CFG_AWS_EC2_EBS_ENCRYPTION_BY_DEFAULT.ACCOUNT_ID`. If the source datasource is aliased, you can refer to a data column *qualified* by its alias (for example, `MyAlias.ACCOUNT_ID`). For more information, see Source Clause Details.

### Referring to JSON Fields

LQL provides simple JSON field access directly in the syntax. JSON field access works only on datasource fields of type JSON.

* *field* `:` *json_path*

The `:` operator references elements within a JSON *object*. The *json_path* is a `.`-separated sequence of JSON keys. For example, given an EVENT field of type JSON: `EVENT:requestParameters` refers to the `requestParameters` field of the JSON object held in `EVENT`, and `EVENT:requestParameters.ipPermissions` refers to the `ipPermissions` field of that object.

Because field names in JSON may not be legal identifiers in LQL, they can be enclosed in double-quotes (for example, `"`). The above could be written as `EVENT:"requestParameters"."ipPermissions"` as well. An example of using these for illegal JSON identifiers would be `EVENT:"RESOURCE_TAG"."aws:cloudformation:stack-name"`, as the string `aws:cloudformation:stack-name` is not a legal LQL identifier.

Because JSON has a free-form structure, any element within a field's JSON object structure is itself of type JSON. The `requestParameters` is a nested object in the example above. To force LQL to treat the result as a particular type, use the `::` type-cast operator.
For example, `EVENT:eval_guid::String` retrieves the `eval_guid` field and casts it to a string.

Working with a JSON array in an expression is not currently supported. You can expand JSON arrays to rows for filtering and projecting purposes in the `source` clause. For more information, see Source Clause Details.

### Data Type Casting Support

| FROM_TYPE | TO_TYPE | Notes |
| --- | --- | --- |
| Boolean | JSON | Supported |
| Boolean | Number | Unsupported |
| Boolean | String | Unsupported Use a CASE expression to convert, such as `CASE when IS_ARRAY(VOLUME_MAP) then 'True' else 'False' end as ARRY_BOOL`. |
| Boolean | Timestamp | Unsupported |
| JSON | Boolean | Supported |
| JSON | Number | Supported |
| JSON | String | Supported |
| JSON | Timestamp | Supported |
| Number | Boolean | Supported |
| Number | JSON | Supported |
| Number | String | Supported |
| Number | Timestamp | Supported The provided numbers are interpreted as epoch seconds. |
| String | Boolean | Supported |
| String | JSON | Supported |
| String | Number | Supported |
| String | Timestamp | Supported The string is converted based on its contents: A string in a standard datetime format such as ISO 8601 is converted according to standard rules. A string containing a string of digits is interpreted as a stringified epoch number - if it contains 13 digits, it is interpreted as epoch milliseconds and if it contains 10 or fewer digits it is interpreted as epoch seconds. |
| Timestamp | Boolean | Unsupported |
| Timestamp | JSON | Supported |
| Timestamp | Number | Unsupported |
| Timestamp | String | Supported Stringified as a textual date format (not as a stringified epoch milliseconds/seconds number). The specific format may be subject to change over time. |

## Source Clause Details

### Description

The `source` clause specifies the source data for further manipulating. It specifies a table-like set of tuples.

The source clause can refer to a datasource directly or by an alias. For example, the following refers to the source without aliasing:

```
source { LW_CFG_AWS_EC2_EBS_ENCRYPTION_BY_DEFAULT }
```

You can then access its columns by an unqualified name, such as `ACCOUNT_ID` or a qualified name such as `LW_CFG_AWS_EC2_EBS_ENCRYPTION_BY_DEFAULT`.

However, you can provide an alias for the source, as in the following example:

```
source { LW_CFG_AWS_EC2_EBS_ENCRYPTION_BY_DEFAULT a }
```

In this case, you can refer to a qualified field reference using the `a.ACCOUNT_ID` syntax instead.

### Joining Multiple Datasources

You can connect the data of two or more datasources in an LQL query using the `WITH ... ON` construct. For detailed information, see Connecting Multiple Datasources in Queries.

### Expanding JSON Arrays into Rows

You can expand JSON fields that contain an array into individual rows, with a row representing each item in the array. For example:

```
 {
     source {
         LW_CFG_AWS_EC2_SECURITY_GROUPS a,
         array_to_rows(a.RESOURCE_CONFIG:IpPermissions) ip_permissions,
         array_to_rows(a.RESOURCE_CONFIG:IpPermissionsEgress) ip_permissions_egress
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

In the above example, the array referenced by `a.RESOURCE_CONFIG:IpPermissions` is expanded into rows, and the values of that array are exposed in a column named `ip_permissions`. The array referenced by `a.RESOURCE_CONFIG:IpPermissionsEgress` is expanded into rows, and the values of that array are exposed in a column named `ip_permissions_egress`. Both the `ip_permissions` and `ip_permissions_egress` columns are available in the source for filtering and projecting.

In general, the `array_to_rows` and `array_to_rows_non_empty` functions operate on a JSON array derived from a source named earlier in the `source` clause. Expanding does two things:

1. It expands the set of rows returned by the source. For each row of the datasource where the JSON array comes from, its array of `n` elements causes expansion to `n` rows. (An array of three elements in a row results in three rows, an array of four elements results in four rows, etc.)
2. It creates a logical column in the source section. The `colAlias` is the name of this column (this is why `colAlias` is required).

The `colAlias` name is in the namespace of all columns produced from the `source` clause, so if its name matches the name of any other column, it must be given a `dtName` name. The `dtName` must be unique within all of the source names/aliases.

The logical column that results from flattening is an JSON entity (object, string, number, boolean, null). It can be used like any other JSON column: returned, used as a source for path expressions, and so on.

For example, consider the following input records:

*Table A*

| ID | OBJECT |
| --- | --- |
| 1 | `{"servicePerms" : [{"service": "web", "access": "root"}, {"service", "smtp", "access" : "mail"}]}` |
| 2 | `{"servicePerms" : [{"service": "cron", "access": "root"}]}` |

The following `source` clause:

`source { A, array_to_rows(A:OBJECT.servicePerms) SERVICE_PERMS }`

results in `A` being expanded to the following set of records:

| ID | OBJECT | SERVICE_PERMS |
| --- | --- | --- |
| 1 | `{"servicePerms" : [{"service": "web", "access": "root"}, {"service", "smtp"}, {"access" : "mail"}]}` | `{"service": "web", "access": "root"}` |
| 1 | `{"servicePerms" : [{"service": "web", "access": "root"}, {"service", "smtp"}, {"access" : "mail"}]}` | `{"service", "smtp", "access" : "mail"}` |
| 2 | `{"servicePerms" : [{"service": "cron", "access": "root"}]}` | `{"service": "cron", "access": "root"}` |

#### `array_to_rows` vs `array_to_rows_non_empty`

Expanding works on JSON arrays derived from a datasource. The expression that produces the array may produce NULL (normal or JSON null) instead.

* `array_to_rows_non_empty`: When the expression produces NULL, the row is eliminated from the output. (This is similar to an inner join lacking a matching tuple.)
* `array_to_rows`: When the expression produces NULL, a null value is returned for the field value, `colALias` in this case. (This is similar to a SQL outer join in the presence of a missing match).

When the query includes one or more `ARRAY_TO_ROWS` source functions, the query might result in many records for each source record. See Limitations On Queries in Policy Evaluation for restrictions that apply to such queries when used in LQL policies.

#### Chained Expansion

An array that is extracted from the result of expansion can be itself expanded. You can use this to expand nested relationships.

#### Branched Expansion

Expansion can be applied multiple times to a named source. The effect is to produce, per source record, a cartesian product of records from each expansion of that table. For example, if one expansion expands one record to three, and another expansion of that same source record expands that one record to four, the result of applying both of those expansions produces twelve tuples.

## `filter` Clause Details

### Description

The `filter` clause specifies a boolean expression that filters the source records. You can use any valid expression here, as long as the result type of it is boolean.

## `return` Clause Details

### Description

The `return` clause specifies the columns to return from the query.

Each column in a result has a name, so that it can be identified later. All column names defined or resulting from a `return` clause must be unique.

The name for a column is inferred if the column is a simple reference to a column from the source, such as `EVENT` or `CloudTrailRawEvents.EVENT_ID`. References that are the result of expressions, such as `EVENT:eventTime` or `coalesce(ERROR_CODE, 0)`, must be aliased, as with `EVENT:eventTime AS eventTime` and `coalesce(ERROR_CODE, 0) as errorCode`. You can alias any column reference to another name.

A field with a JPath reference is named by default with the field name, not with the name of the last step in the JPath. For example, in the following, the name of the column returned is `SomeJsonField`, not `objKey`:

```
{
    source {
        MySource
    }
    return {
        MySource.SomeJsonField:objKey
    }
}
```

### Returning Distinct Records With `return distinct`

Similar to an SQL query, you may need to reduce a set of records that come from the source to only the unique or distinct ones. For example, you used `array_to_rows` to create multiple records, and then filtered those records based on some criterion, but now you want to return only the unexpanded set of records that matched the filter. Adding the `distinct` keyword causes the resulting records to be deduplicated.

### Returning All Columns of a Datasource With `.*`

Similar to an SQL query, all columns of a named datasource can be returned by using the `.*` wildcard. For example, the following returns all columns from `LW_CFG_AWS_EC2_SECURITY_GROUPS`:

```
return {
  LW_CFG_AWS_EC2_SECURITY_GROUPS.*
}
```

## Connecting Multiple Datasources in Queries

You can connect the data of two or more datasources in an LQL query using the `WITH ... ON` construct. For example, the following query uses data of the `LW_HE_FILES` datasource with its related `LW_HE_MACHINES` data:

```
Sample_LQL {
    source {
        LW_HE_FILES files with LW_HE_MACHINES machines
    }
    filter {
        ENDS_WITH (FILE_NAME, 'exe') AND OS like '%Linux%'
    }
    return {
        PATH,
        HOST_NAME
    }
}
```

In the example query, the `FILE_NAME` and `PATH` attributes are from `LW_HE_FILES`, and the `OS` and `HOST_NAME` attributes are from `LW_HE_MACHINES`.

The behavior of `WITH` is to select records from the source on the left side with any matching records from sources on the right. All values for the right side's source's fields will be NULL if there is no match in the right side. (If you are familiar with SQL, this is equivalent to a "left outer join" between them.)

Lacework knows which datasources connect to each other and how they connect. The connections available from each datasource to other datasources are provided with the datasource through the metadata APIs.

### Named and Default Paths

Every defined connection from one datasource to another has a name. If a connection is considered to be the default connection, it has the name `(default)`. If two or more connections from one datasource to another exist, each connection has its own name.

To use the name, use the `ON` keyword. The following example uses the `(default)` name in the `source` clause. The connection's name is in single-quotes just like a literal string.

```
source {
    LW_HE_FILES with LW_HE_MACHINES on '(default)'
}
```

### Connecting Three or More Datasources

Your query may be accessing the data of one source with the data of another source, and can also connect the data of that other source with one that is connected to it. Or, your query can access the data of one source with that of two related datasources. You can chain and branch the connections as described in this section.

#### Chaining Connections

For example, the following `source` clause connects `LW_HA_FILE_CHANGES` records with their `LW_HE_FILES` records, and `LW_HE_FILES` records with their `LW_HE_MACHINES` records. This creates a chain of `LW_HA_FILE_CHANGES → LW_HE_FILES → LW_HE_MACHINES`.

```
source {
    LW_HA_FILE_CHANGES with LW_HE_FILES with LW_HE_MACHINES
}
```

You can use parentheses to group the connections for clarity. For example:

```
    LW_HA_FILE_CHANGES with (LW_HE_FILES with LW_HE_MACHINES)
```

Note that they chain from right to left. The following is *not* correct. The reason is that the left side of `WITH` must be a single datasource.

```
    // Will be rejected
    (LW_HA_FILE_CHANGES with LW_HE_FILES) with LW_HE_MACHINES
```

When you chain multiple steps, using grouping parentheses can help keep the connections clear. For example, both of the following are correct and mean the same thing, but one is easier to follow:

```
    LW_HA_FILE_CHANGES
            with LW_HE_FILES with LW_HE_MACHINES on '(default)'
            on '(default)'

    LW_HA_FILE_CHANGES
            with (LW_HE_FILES with LW_HE_MACHINES on '(default)')
            on '(default)'
```

#### Forked Connection Paths

The previous examples showed retrieving from three datasources using a chain of connections. Because `LW_HA_FILE_CHANGES` connects directly to `LW_HE_MACHINES` as well as `LW_HE_FILES`, you could use a branching connection as well:

```
source {
    LW_HA_FILE_CHANGES with (
        LW_HE_FILES,
        LW_HE_MACHINES
    )
}
```

In branching connections, the query brings back all combinations of the target datasources' records per record of the left-side source. You can picture the branches as `LW_HA_FILE_CHANGES → (combinations of LW_HE_FILES and LW_HE_MACHINES)`.

Consider a query for machines data with their related files and process data that filters for Linux machines running processes whose executables are links ending in `.exe`:

```
query {
    source {
        LW_HE_MACHINES machines with (
            LW_HE_FILES files,
            LW_HE_PROCESSES processes
        )
    }
    filter {
        machines.OS like ('%Linux%')
        AND files.IS_LINK <> 0
        AND ENDS_WITH(processes.EXE_PATH, '.exe')
     }
    return distinct {
        machines.MID,
        machines.HOSTNAME,
        machines.TAGS
    }
}
```

This filters across all combinations of files for a machine and processes for that same machine, and returns just the machines that meet the condition.

Branching connections also use named connections. You could write the above `source` clause as:

```
    source {
        LW_HE_MACHINES machines with (
            LW_HE_FILES files on '(default)',
            LW_HE_PROCESSES processes on '(default)'
        )
    }
```

### Connections and Data Cardinality

The metadata associated with each connection includes whether the relationship produces at most one record, or many records. In the metadata for each datasource's connections to other sources, these are designated by the following:

| Code | Meaning |
| --- | --- |
| `ONE` | Relationship leads to at most one record |
| `MANY` | Relationship leads to many records |

## Limitations on Queries in Policy Evaluation

The first (or root) datasource among your connected datasources corresponds to the type of data the policy is for. If the source specification is `LW_HE_MACHINES with LW_HE_PROCESSES`, the root datasource is `LW_HE_MACHINES`, and policies using this query are policies about machines.

LQL policies assume that each result represents a single violating resource. If the datasource connections create many results for each root source's records, misleading results may occur. Therefore, the following validations take place on queries being used in policies:

* If the query uses only connections with a cardinality of `ONE`, and does not use any `ARRAY_TO_ROWS` source functions, any data from the datasources can be returned in the result.
* If the query uses any connections with a cardinality of `MANY`, and/or if the query uses any `ARRAY_TO_ROWS` source functions, the query must obey the following:
  + The query must return `distinct` results, using `return distinct`.
  + The query can return result columns derived only from the root datasource and/or datasources whose connection to the root is `ONE`. The query cannot return results derived from the datasources connected to the root by `MANY`, nor can it return results derived from `ARRAY_TO_ROWS`.
    There are no limitations on data used in the `filter` clause, regardless.

## Regular Expression Syntax

LQL operators RLIKE and RLIKE ANY can match patterns against a string expression. Pattern matching syntax for these operators adhere to POSIX® extended regular expression syntax.

The following list includes notable features of the Lacework's POSIX® support:

* *<period> (`.`)* - Match any single character.
* *<plus-sign> (`+`)* - Match one or more consecutive occurrences of the preceding character or pattern.
* *<asterisk> (`*`)* - Match zero or more consecutive occurrences of the preceding character or pattern.
* *<question-mark> (`?`)* - Match zero or one consecutive occurrences of the preceding character or pattern.
* *Anchoring <circumflex> (`^`)* - Anchors the pattern to the beginning of a string, when used as the first character. Use a <circumflex> (`^`) as the first character in a bracket expression to indicate a non-matching list expression.
* *Anchoring <dollar-sign> (`$`)* - Anchors the pattern to the end of a string, when used as the last character.
* *Bracket expression <square brackets> (`[]`)* - Matches a specific set of characters defined within the brackets; bracket expressions may include ordinary characters, collating elements, collating symbols, equivalence classes, character classes, or range expressions. Use a <circumflex> (`^`) as the first character in a bracket expression to indicate a non-matching list expression.
* *Grouping <parenthesis> (`()`)* - Matches multiple characters or patterns defined within the parenthesis.
* *Alternation <vertical-line> (`|`)* - An "OR" separator. Matches either string or pattern, before or after the vertical-line.
