<!-- Generated from FortiCNAPP 26.2 LQL Reference Guide (fetched 2026-10-28). Source:
     https://docs.fortinet.com/document/forticnapp/latest/lql-reference/754354/lql-operators -->

# LQL Operators

LQL uses conventional SQL notation for arithmetic, comparisons, and logical operations.

### Arithmetic

* The following operators have the ordinary meanings and precedence for arithmetic:
  `+` `-` `*` `/`
* The `%` operator represents the modulus operation.
* The `-` operator also can be used for unary negation. For example, `-x` returns the negative for whatever value `x` has.

LQL follows SQL semantics for arithmetic; if either input to an arithmetic operation is null, the result is null.

### Grouping Parentheses

Parentheses (`(` and `)`) are used to clearly group expressions and subexpressions, and to establish order of operations. For example, `(x + y) * z` adds `x` and `y` together and then multiplies their sum by `z`. `x + y * z` will multiply `y` and `z` together,
then add their product to `x`.

### Comparison

You can compare numbers, strings, and timestamps.

#### Comparison Operators

LQL follows SQL semantics for comparisons; if either input to a comparison operation is null, the result is null, not true or false.

The following comparison operators have their ordinary meanings: `<` `<=` `>` `>=` `=` `<>`. The
`<>` operator means "not-equals".

#### IN, NOT IN

To test if something is equal to some value out of a collection of values, use the `IN (...)` operator, as in the following form:

`IN (` *list of literal values* `)`, `NOT IN (` *list of literal values* `)`

For example, `EVENT_SOURCE in ('A1', 'B2')` results in true if `EVENT_SOURCE` has either the string value of `A1` or `B2`. All values in the list of literals must be of the same type, and neither `null` nor of JSON type.

To test if something is *not* in a list of possibilities, use `NOT IN`. For example, `STATUS NOT IN (401, 403)`.

#### BETWEEN

The `BETWEEN` operator is shorthand for `(` *something* `>=` *low_bound* `AND` *something* `<=` *high_bound* `)`.

Use this comparison in the following form:

*something* `BETWEEN` *low_bound* `AND` *high_bound*

`BETWEEN` works with numbers, timestamps, and strings. All arguments must be coercible to numbers or coercible to timestamps.

#### LIKE

Similar to SQL `LIKE`, this operator tests if the string on the left matches the pattern on the right in a case-sensitive manner, in the following form:

*something* `LIKE` *pattern*

Within the pattern, the `%` character is a wildcard meaning "any characters". The `_` character is a wildcard that means "any single character". The entire left string is compared with the pattern, so if you want to match a substring and it could be anywhere in the left string, start and end the pattern with `%`. For example, `EVENT_SOURCE LIKE '%aws.com'` matches any string that ends with `aws.com`.

#### ILIKE

Similar to SQL `ILIKE`, this operator tests if the string on the left matches the pattern on the right in a case-insensitive manner, in the following form:

*something* `ILIKE` *pattern*

The wildcard semantics for `LIKE` apply to `ILIKE` as well.

#### RLIKE

Similar to SQL `RLIKE`, this operator tests if the string on the left matches the pattern on the right. The pattern is written using POSIX extended regular expressions, in the following form:

*something* `RLIKE` *pattern*

The entire left string is compared with the pattern, so if you want to match a substring and it could be anywhere in the left string, start and end the pattern with `.*`. For example, `EVENT_SOURCE RLIKE '.*\.amazonaws\.com'` matches any string that ends with `.amazonaws.com`.

For more information on regular expression support with RLIKE, see Regular Expression Syntax.

#### LIKE ANY

Checks in a case-sensitive manner whether a string on the left matches any pattern specified on the right, in the following form:

*something* `LIKE ANY` (*pattern_0*, *pattern_1*, ..., *pattern_n*)

This is logically equivalent to *something* `LIKE` *pattern_0* `OR` *something* `LIKE` *pattern_1* ... `OR` *something* `LIKE` *pattern_n*.

#### ILIKE ANY

Checks in a case-insensitive manner whether a string on the left matches any pattern specified on the right, in the following form:

*something* `ILIKE ANY` (*pattern_0*, *pattern_1*, ..., *pattern_n*)

This is logically equivalent to *something* `ILIKE` *pattern_0* `OR` *something* `ILIKE` *pattern_1* ... `OR` *something* `ILIKE` *pattern_n*.

#### RLIKE ANY

Checks whether a pattern on the left matches any pattern specified on the right. The patterns may be POSIX-extended regular expressions.

Use this comparison operator in the following form:

*something* `RLIKE ANY` (*pattern_0*, *pattern_1*, ..., *pattern_n*)

This is logically equivalent to *something* `RLIKE` *pattern_0* `OR` *something* `RLIKE` *pattern_1* ... `OR` *something* `RLIKE` *pattern_n*.

For more information on regular expression support with RLIKE ANY, see Regular Expression Syntax.

#### Comparing with standard null

The `IS NULL` and `IS NOT NULL` comparisons test whether a value from a non-JSON column or function is or is not null. Similar to SQL, you do not compare anything as being equal to null. For example, `ERROR_CODE is null` tests whether `ERROR_CODE` has a null.

Use this comparison operator in the following form:

*something* `IS NULL`, *something* `IS NOT NULL`

#### Comparing with JSON null

The `IS JSON NULL` and `IS NOT JSON NULL` comparisons test whether a JSON value is "JSON null". For example, `RESOURCE_CONFIG:SecondaryServer is json null` tests whether the JSON object in the `RESOURCE_CONFIG` column has a `null` set for its `"SecondaryServer"` field, that is, matching `{ "SecondaryServer": null }`. If the key `"SecondaryServer"` is not present in the JSON object, `is json null` results in `null` itself, not false.

Use this comparison operator in the following form:

*something* `IS JSON NULL`, *something* `IS NOT JSON NULL`

### Logical

The following operations have their standard logical meanings: `AND` `OR` `NOT`

`AND` has higher precedence than `OR`; `A AND B OR C` returns true if `A` and `B` are both true, or if `C` is true. `NOT` has higher precedence than `AND`; `NOT A AND B` returns true if `A` is false and `B` is true.

If either input to a logical operation is null, the result is null.

### Conditional

#### `CASE` `WHEN` `THEN` `ELSE` `END`

* `CASE WHEN test THEN value ...`
* `CASE value WHEN value THEN value ...`

The `CASE` construct follows SQL syntax. All `THEN` clauses, and the `ELSE` clause if provided, must return the same datatype or a datatype that can be coerced to a common data type.

### Type Conversion

#### *something* `::` *as_type*

The `::` operator converts a data value into a specific data type. For example, `COUNT_OBJECTS::String` converts the numeric count into a string, and `'2021-06-03T00:47:33Z'::Timestamp` creates a timestamp value for a specific time.

### Set

Set operators include `UNION` and `UNION ALL`.

`UNION` and `UNION ALL` combine the results of two or more select statements. `UNION` eliminates duplicates, while `UNION ALL` does not.

The syntax format is:

```
union {{
  source {...}
  filter {...}
  return {...}
},
...
, {
  source {...}
  filter {...}
  return {...}
}}
```

The data sources combined by the `UNION` operator must be identical, as illustrated by the following example:

```
  union {{
      source {
          LW_CFG_AWS_IAM_USERS_GET_CREDENTIAL_REPORT
      }
      filter {
          RESOURCE_CONFIG:access_key_1_active = 'true'
          and diff_days(case when RESOURCE_CONFIG:access_key_1_last_rotated = 'N/A' then null
          else to_timestamp(RESOURCE_CONFIG:access_key_1_last_rotated::string) end, sec_to_timestamp(current_timestamp_sec())) > 30
      }
      return distinct {
          ACCOUNT_ID,
          ARN as RESOURCE_KEY,
          RESOURCE_REGION,
          RESOURCE_TYPE,
          SERVICE,
          'AccessKey1NotRotated30Days' as COMPLIANCE_FAILURE_REASON
      }
  },
      source {
          LW_CFG_AWS_IAM_USERS_GET_CREDENTIAL_REPORT
      }
      filter {
          RESOURCE_CONFIG:access_key_2_active = 'true'
          and diff_days(case when RESOURCE_CONFIG:access_key_2_last_rotated = 'N/A' then null
          else to_timestamp(RESOURCE_CONFIG:access_key_2_last_rotated::string) end, sec_to_timestamp(current_timestamp_sec())) > 30
      }
      return distinct {
          ACCOUNT_ID,
          ARN as RESOURCE_KEY,
          RESOURCE_REGION,
          RESOURCE_TYPE,
          SERVICE,
          'AccessKey2NotRotated30Days' as COMPLIANCE_FAILURE_REASON
      }
  }}
```
