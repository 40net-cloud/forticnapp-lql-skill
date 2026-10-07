<!-- Generated from FortiCNAPP 26.2 LQL Reference Guide (fetched 2026-08-26). Source:
     https://docs.fortinet.com/document/forticnapp/latest/lql-reference/486918/lql-functions -->

# LQL Functions

This topic lists all Lacework Query Language functions alphabetically.

| Function | Description |
| --- | --- |
| ABS | Returns the absolute value of a number. |
| ADD_DAYS | Adds the specified number of days to a timestamp. |
| ADD_HOURS | Adds the specified number of hours to a timestamp. |
| ADD_MILLIS | Adds the specified number of milliseconds to a timestamp. |
| ADD_MINUTES | Adds the specified number of minutes to a timestamp. |
| ADD_MONTHS | Adds the specified number of months to a timestamp. |
| ADD_SECONDS | Adds the specified number of seconds to a timestamp. |
| ADD_YEARS | Adds the specified number of years to a timestamp. |
| ANY_IN_ARRAY | Returns True if the `array` argument is an array in JSON and at least one of the provided values in contained in it. |
| ARRAY_SIZE | Returns the number of items in a JSON array. |
| ARRAY_TO_ROWS | Expands JSON arrays into rows. |
| ARRAY_TO_ROWS_NON_EMPTY | Expands JSON arrays into rows, while excluding NULL values. |
| CHAR_INDEX | Searches for the first time a string occurs in another string. If successful, returns the position of the first string in the second string. |
| COALESCE | Returns the first non-null expression among its arguments. Returns null if all arguments are null. |
| CONTAINS | Returns True if a string contains another string. |
| CURRENT_TIMESTAMP_MS | Returns the current timestamp as UTC epoch milliseconds |
| CURRENT_TIMESTAMP_SEC | Returns the current timestamp as UTC epoch seconds. |
| DAY_OF_MONTH | Returns the day of the month (number 1 to 31) from a timestamp. |
| DAY_OF_WEEK | Returns the day of the week (number 1 to 7) from a timestamp. |
| DAY_OF_YEAR | Returns the day of the year (number 1 to 366) from a timestamp. |
| DAY_PART | Returns the day of the month (number 1 to 31) from a timestamp. |
| DIFF_DAYS | Returns the number of days between two timestamps. |
| DIFF_HOURS | Returns the number of hours between two timestamps. |
| DIFF_MINUTES | Returns the number of minutes between two timestamps. |
| DIFF_MILLIS | Returns the number of milliseconds between two timestamps. |
| DIFF_MONTHS | Returns the number of months between two timestamps. |
| DIFF_SECONDS | Returns the number of seconds between two timestamps. |
| DIFF_YEARS | Returns the number of years between two timestamps. |
| ENDS_WITH | Returns True if a string ends with a specified string. |
| EPOCH_MS | Returns a number that is milliseconds from epoch for a timestamp. |
| EPOCH_SEC | Returns a number that is seconds from epoch for a timestamp. |
| HOUR_PART | Returns the hour of the day (number 0 to 23) from a timestamp. |
| IP_ADDRESS | Returns the IP address part of a CIDR or IP address. |
| IP_CONTAINS | Interprets `arg0` and `arg1` as sets of IP addresses and returns true if `arg0` contains `arg1` (i.e. `arg1` is a subset of, or equal to, `arg0`). See the detailed entry below. |
| IP_FAMILY | Returns the IP address family version as a number, 4 or 6. |
| IP_HIGH_NETMASK_BITS | Returns the number of high bits in the netmask of a CIDR, also known as the network prefix bits. |
| IS_ARRAY | Returns True if the input contains an ARRAY value. |
| IS_OBJECT | Returns True if the input contains an OBJECT value. |
| KEY_EXISTS | Returns True if a JSON object key exists, regardless of whether it maps to a null, an object, or an array. |
| LEFT | Returns the leftmost substring of the input. |
| LENGTH | Returns the number of characters in the input. |
| LOWER | Returns the input as all lowercase characters. |
| LTRIM | Removes leading characters from the input, including whitespace. |
| MINUTE_PART | Returns the minute (number 0 to 59) from a timestamp. |
| MONTH_PART | Returns the month (number 1 to 12) from a timestamp. |
| MS_TO_TIMESTAMP | Converts a number representing milliseconds from epoch into the equivalent timestamp. |
| QUARTER_PART | Returns the quarter (number 1 to 4) from a timestamp. |
| RIGHT | Returns the rightmost substring of the input. |
| RTRIM | Removes trailing characters from the input, including whitespace. |
| SECOND_PART | Returns the second (number 0 and 59) from a timestamp. |
| SEC_TO_TIMESTAMP | Converts a number representing seconds from epoch into the equivalent timestamp. |
| STARTS_WITH | Returns True if a string starts with a specified string. |
| SUBSTRING | Returns a portion of a string, starting from a specified position. |
| TO_BOOLEAN | Converts the input to a Boolean value. |
| TO_DOUBLE | Converts the input to a double-precision floating-point number. |
| TO_JSON | Parses a JSON string and produces a JSON object. |
| TO_TIMESTAMP | Converts a string-valued timestamp expression into the equivalent timestamp. |
| TRIM | Removes leading and trailing characters from a string. |
| TRY_TO_NUMBER | Attempts to convert a string to an integer. |
| UPPER | Returns the input as all uppercase characters. |
| VALUE_EXISTS | Returns True if a JSON object key has a non-null value. |
| YEAR_PART | Returns the year (any valid year) from a timestamp. |

---

`ABS ( n )`

Arguments

* `n`: A number.

Returns the absolute value of `n`.

---

`ADD_DAYS ( n, timestamp )`

Arguments

* `n`: The number of days to add. Can be positive or negative.
* `timestamp`: The timestamp to add to. If this is provided as a JSON string field, the string is automatically converted to a timestamp.

Adds `n` days to `timestamp`.

---

`ADD_HOURS ( n, timestamp )`

Arguments

* `n`: The number of hours to add. Can be positive or negative.
* `timestamp`: The timestamp to add to. If this is provided as a JSON string field, the string is automatically converted to a timestamp.

Adds `n` hours to `timestamp`.

---

`ADD_MILLIS ( n, timestamp )`

Arguments

* `n`: The number of milliseconds to add. Can be positive or negative.
* `timestamp`: The timestamp to add to. If this is provided as a JSON string field, the string is automatically converted to a timestamp.

Adds `n` milliseconds to `timestamp`.

---

`ADD_MINUTES ( n, timestamp )`

Arguments

* `n`: The number of minutes to add. Can be positive or negative.
* `timestamp`: The timestamp to add to. If this is provided as a JSON string field, the string is automatically converted to a timestamp.

Adds `n` minutes to `timestamp`.

---

`ADD_MONTHS ( n, timestamp )`

Arguments

* `n`: The number of months to add. Can be positive or negative.
* `timestamp`: The timestamp to add to. If this is provided as a JSON string field, the string is automatically converted to a timestamp.

Adds `n` months to `timestamp`.

---

`ADD_SECONDS ( n, timestamp )`

Arguments

* `n`: The number of seconds to add. Can be positive or negative.
* `timestamp`: The timestamp to add to. If this is provided as a JSON string field, the string is automatically converted to a timestamp.

Adds `n` seconds to `timestamp`.

---

`ADD_YEARS ( n, timestamp )`

Arguments

* `n`: The number of years to add. Can be positive or negative.
* `timestamp`: The timestamp to add to. If this is provided as a JSON string field, the string is automatically converted to a timestamp.

Adds `n` years to `timestamp`.

---

`ANY_IN_ARRAY ( array, val1 [, ... valN] )`

Arguments

* `array` : Array (in a JSON object) to search in.
* `val1` ... `valN` : Values to find in the array. (May be literals, column references, any derived values, or `NULL`)

Returns True if the `array` argument is an array in JSON and at least one of the provided values is contained in it. Returns False otherwise.

---

`ARRAY_SIZE ( array )`

Arguments

* `array` : The JSON array for which you want to get the item count.

Returns the number of items in a JSON array. This function is useful for getting resource counts, among other things, for example:

```
source {
    LW_CFG_AWS_ELBV2 ELB
}
return {
    array_size(ELB.RESOURCE_CONFIG:AvailabilityZones) NUM_SUBNETS
}
```

---

`ARRAY_TO_ROWS ( array )`

Arguments

* `array` : The JSON array to expand into rows.

Given a JSON array, this function expands each item in the row into a separate row in the results.

When the expression produces NULL, a null value is given for the returned field. (This is similar to a SQL outer join in the presence of a missing match).

For example:

```
source {
    LW_HA_CONNECTION_SUMMARY,
    array_to_rows(ENDPOINT_DETAILS) as EP_PA
}
filter {
    SRC_ENTITY_TYPE = 'Process'
    and not (EP_PA:dst_ip_addr in ('127.0.0.1', '0.0.0.0'))
}
return distinct {
    SRC_ENTITY_ID:mid::number as MID,
    SRC_ENTITY_ID:pid_hash::number as PID
}
```

For details, see Expanding JSON Arrays into Rows.

---

`ARRAY_TO_ROWS_NON_EMPTY ( array )`

Arguments

* `array` : The JSON array to expand into rows.

Given a JSON array, this function expands each item in the row into a separate row in the results.

When the expression produces NULL, the row is eliminated from the output. (This is similar to an inner join lacking a matching tuple.)

For example:

```
source {
    LW_HA_CONNECTION_SUMMARY,
    array_to_rows_non_empty(ENDPOINT_DETAILS) as EP_PA
}
filter {
    SRC_ENTITY_TYPE = 'Process'
    and not (EP_PA:dst_ip_addr in ('127.0.0.1', '0.0.0.0'))
}
return distinct {
    SRC_ENTITY_ID:mid::number as MID,
    SRC_ENTITY_ID:pid_hash::number as PID
}
```

For details, see Expanding JSON Arrays into Rows.

---

`CHAR_INDEX ( searchfor, searchin )`
  
`CHAR_INDEX ( searchfor, searchin, start )`

Arguments

* `searchfor`: The string to search for.
* `searchin`: The string to search in.
* `start`: A number that represents the starting position of the search. 1 represents the start of `searchin`.

Searches for the first time `searchfor` occurs in `searchin`. If successful, returns the position of `searchfor` in `searchin`. The `start` position is optional.

---

`COALESCE ( arg1, arg2, ... )`

Arguments

* `argn`: The arguments to coalesce. All arguments must have the same data type.

Returns the first non-null expression among its arguments. Returns null if all arguments are null.

---

`CONTAINS ( searchin, searchfor )`

Arguments

* `searchin`: The string to search in.
* `searchfor`: The string to search for.

Returns True if `searchin` contains `searchfor`.

---

`CURRENT_TIMESTAMP ( )` *DEPRECATED*

Returns the current timestamp.

This function is deprecated and might be removed in a future release.

---

`CURRENT_TIMESTAMP_MS ( )`

Returns the current timestamp as UTC epoch milliseconds (number of milliseconds since Jan 01, 1970 in the UTC timezone).
Note that this function returns a number, not a timestamp.

---

`CURRENT_TIMESTAMP_SEC ( )`

Returns the current timestamp as UTC epoch seconds (number of seconds since Jan 01, 1970 in the UTC timezone).
Note that this function returns a number, not a timestamp.

---

`DAY_OF_MONTH ( timestamp )`

Arguments

* `timestamp`: The timestamp to extract the day from. This is not automatically converted from a JSON string. If the source of the timestamp is JSON, you must explicitly cast it to TIMESTAMP to convert it.

Returns the day of the month (number 1 to 31) from `timestamp`.

---

`DAY_OF_WEEK ( timestamp )`

Arguments

* `timestamp`: The timestamp to extract the day from. This is not automatically converted from a JSON string. If the source of the timestamp is JSON, you must explicitly cast it to TIMESTAMP to convert it.

Returns the day of the month (number 1 to 7) from `timestamp`.

---

`DAY_OF_YEAR ( timestamp )`

Arguments

* `timestamp`: The timestamp to extract the day from. This is not automatically converted from a JSON string. If the source of the timestamp is JSON, you must explicitly cast it to TIMESTAMP to convert it.

Returns the day of the month (number 1 to 366) from `timestamp`.

---

`DAY_PART ( timestamp )`

Arguments

* `timestamp`: The timestamp to extract the day from. This is not automatically converted from a JSON string. If the source of the timestamp is JSON, you must explicitly cast it to TIMESTAMP to convert it.

Returns the day of the month (number 1 to 31) from `timestamp`.

---

`DIFF_DAYS ( from, to )`

Arguments

* `from`: Starting timestamp.
* `to`: Ending timestamp.

Returns the number of days between `from` and `to` as an integer.

---

`DIFF_HOURS ( from, to )`

Arguments

* `from`: Starting timestamp.
* `to`: Ending timestamp.

Returns the number of hours between `from` and `to` as an integer.

---

`DIFF_MINUTES ( from, to )`

Arguments

* `from`: Starting timestamp.
* `to`: Ending timestamp.

Returns the number of minutes between `from` and `to` as an integer.

---

`DIFF_MILLIS ( from, to )`

Arguments

* `from`: Starting timestamp.
* `to`: Ending timestamp.

Returns the number of milliseconds between `from` and `to` as an integer.

---

`DIFF_MONTHS ( from, to )`

Arguments

* `from`: Starting timestamp.
* `to`: Ending timestamp.

Returns the number of months between `from` and `to` as an integer.

---

`DIFF_SECONDS ( from, to )`

Arguments

* `from`: Starting timestamp.
* `to`: Ending timestamp.

Returns the number of seconds between `from` and `to` as an integer.

---

`DIFF_YEARS ( from, to )`

Arguments

* `from`: Starting timestamp.
* `to`: Ending timestamp.

Returns the number of years between `from` and `to` as an integer.

---

`ENDS_WITH ( string1, string2 )`

Arguments

* `string1`: The string to evaluate.
* `string2`: The ending string.

Returns True if `string1` ends with `string2`.

---

`EPOCH_MS ( timestamp )`

Arguments

* `timestamp`: The timestamp from which to extract milliseconds from epoch. This is not automatically converted from a JSON string. If the source of the timestamp is JSON, you must explicitly cast it to TIMESTAMP to convert it.

Returns a number that is milliseconds from epoch from `timestamp`.

---

`EPOCH_SEC ( timestamp )`

Arguments

* `timestamp`: The timestamp from which to extract seconds from epoch. This is not automatically converted from a JSON string. If the source of the timestamp is JSON, you must explicitly cast it to TIMESTAMP to convert it.

Returns a number that is seconds from epoch from `timestamp`.

---

`HOUR_PART ( timestamp )`

Arguments

* `timestamp`: The timestamp to extract the hour from. This is not automatically converted from a JSON string. If the source of the timestamp is JSON, you must explicitly cast it to TIMESTAMP to convert it.

Returns the hour (number 0 to 23) from `timestamp`.

---

`IP_ADDRESS ( arg )`

Arguments

* `arg`: IP address or CIDR.

Returns the IP address part of `arg`.

---

`IP_CONTAINS ( arg0, arg1 )`

Arguments

* `arg0`: IP address or CIDR.
* `arg1`: IP address or CIDR.

Interprets `arg0` and `arg1` as sets of IP addresses and return true if `arg0`
contains `arg1`. The set of IPv6 addresses is considered disjoint from the set
of IPv4 addresses, and `IP_CONTAINS` returns false when applied to a mix of
IPv4 and IPv6 CIDRs or addresses.

---

`IP_FAMILY ( arg )`

Arguments

* `arg`: CIDR or IP address

Returns the IP address family version as a number, 4 or 6.

---

`IP_HIGH_NETMASK_BITS ( arg )`

Arguments

* `arg`: CIDR or IP address

Returns the number of high bits in the netmask of a CIDR, also known as the network prefix bits. Returns 32 for an IPv4 address and 128 for an IPv6 address.

---

`IS_ARRAY ( arg )`

Arguments

* `arg`: The argument to evaluate.

Returns True if `arg` contains an ARRAY value.

---

`IS_OBJECT ( arg )`

Arguments

* `arg`: The argument to evaluate.

Returns True if `arg` contains an OBJECT value.

---

`KEY_EXISTS ( key::JSON )`

Arguments

* `key::JSON`: Where key is the key to evaluate.

Returns True if the JSON object `key` exists, regardless of whether it maps to a null, an object, or an array.

---

`LEFT ( string, n )`

Arguments

* `string`: The string to evaluate.
* `n`: The number of characters.

Returns the leftmost substring (`n` characters) of `string`.

---

`LENGTH ( string )`

Arguments

* `string`: The string to evaluate.

Returns the number of characters in `string`.

---

`LOWER ( string )`

Arguments

* `string`: The string to change.

Returns `string` as all lowercase characters.

---

`LTRIM ( string )`

Arguments

* `string`: The string to trim.

Removes leading characters from `string`, including whitespace.

---

`MS_TO_TIMESTAMP ( n )`

Arguments

* `n`: The number to convert to `timestamp`.

Converts a number representing UTC epoch milliseconds (number of milliseconds since Jan 01, 1970 in the UTC timezone) into TIMESTAMP.

---

`MINUTE_PART ( timestamp )`

Arguments

* `timestamp`: The timestamp to extract the minute from. This is not automatically converted from a JSON string. If the source of the timestamp is JSON, you must explicitly cast it to TIMESTAMP to convert it.

Returns the minute (number 0 to 59) from TIMESTAMP.

---

`MONTH_PART ( timestamp )`

Arguments

* `timestamp`: The timestamp to extract the month from. This is not automatically converted from a JSON string. If the source of the timestamp is JSON, you must explicitly cast it to TIMESTAMP to convert it.

Returns the month (number 1 to 12) from TIMESTAMP.

---

`QUARTER_PART ( timestamp )`

Arguments

* `timestamp`: The timestamp to extract the quarter from. This is not automatically converted from a JSON string. If the source of the timestamp is JSON, you must explicitly cast it to TIMESTAMP to convert it.

Returns the quarter (number 1 to 4) from `timestamp`.

---

`RIGHT ( string, n )`

Arguments

* `string`: The string to evaluate.
* `n`: The number of characters.

Returns the rightmost substring (`n` characters) of `string`.

---

`RTRIM ( string )`

Arguments

* `string`: The string to trim.

Removes trailing characters from `string`, including whitespace.

---

`SEC_TO_TIMESTAMP ( n )`

Arguments

* `n`: The number to convert to TIMESTAMP.

Converts a number representing UTC epoch seconds (number of seconds since Jan 01, 1970 in the UTC timezone) into TIMESTAMP.

---

`SECOND_PART ( timestamp )`

Arguments

* `timestamp`: The timestamp to extract the second from. This is not automatically converted from a JSON string. If the source of the timestamp is JSON, you must explicitly cast it to TIMESTAMP to convert it.

Returns the second (number 0 to 59) from TIMESTAMP.

---

`STARTS_WITH ( string1, string2 )`

Arguments

* `string1`: The string to evaluate.
* `string2`: The starting string.

Returns True if `string1` starts with `string2`.

---

`SUBSTRING ( string, start )`
  
`SUBSTRING ( string, start, length )`

Arguments

* `string`: The string to evaluate.
* `start`: The starting position.
* `length`: The length limit of the returned string portion.

Returns a portion of `string`, starting from `start`. Limiting by `length` is optional.

---

`TO_BOOLEAN ( string )`

Arguments

* `string`: The string to convert.

Converts `string` to a Boolean value.

---

`TO_DOUBLE ( string )`

Arguments

* `string`: The string to convert.

Converts `string` to a double-precision floating-point number.

---

`TO_JSON ( string )`

Arguments

* `string`: The JSON string to convert to a JSON object.

Parses an input string as a JSON document and produces a JSON object value. Returns a NULL value if an error occurs during parsing.

You can use `TO_JSON` in any context where a JSON object value is allowed, in particular, as an argument to `array_to_rows`, as in the following example:

```
source {
    T,
    array_to_rows(to_json(T.JSON_STRING):json_field) a
}
```

---

`TO_TIMESTAMP ( string )`

Arguments

* `string`: The string to convert to `timestamp`.

Converts a string expression of a timestamp into a TIMESTAMP.

---

`TRIM ( string )`
  
`TRIM ( string, n )`

Arguments

* `string`: The string to trim.
* `n`: The number of characters to remove from left and right side.

Removes `n` leading and trailing characters from `string`. Not specifying `n` removes all leading and trailing whitespaces.

---

`TRY_TO_NUMBER ( string )`

Arguments

* `string`: The string to convert.

Attempts to convert string to an equivalent integer, returning the resulting integer if successful. Returns a NULL value if the conversion is not successful.

Decimal numbers are rounded to the nearest integer. For example, `"1.4"` returns `1` while `"1.8"` returns `2`.

`UPPER ( string )`

Arguments

* `string`: The string to change.

Returns `string` as all uppercase characters.

---

`VALUE_EXISTS ( key::JSON )`

Arguments

* `key::JSON`: Where key is the key to evaluate.

Returns True if the JSON object `key` has a non-null value. `VALUE_EXISTS` considers empty values such as `[]`, `{}`, `““` to be actual values.

---

`YEAR_PART ( timestamp )`

Arguments

* `timestamp`: The timestamp to extract the year from. This is not automatically converted from a JSON string. If the source of the timestamp is JSON, you must explicitly cast it to TIMESTAMP to convert it.

Returns the year (any valid year) from the `timestamp`.
