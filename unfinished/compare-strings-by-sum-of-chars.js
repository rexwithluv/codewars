/* ID: 576bb3c4b1abc497ec000065

Compare two strings by comparing the sum of their values (ASCII character code).

* For comparing treat all letters as UpperCase
* `null/NULL/Nil/None` should be treated as empty strings
* If the string contains other characters than letters, treat the whole string as it would be empty

Your method should return `true`, if the strings are equal and `false` if they are not equal.

## Examples:
```
"AD", "BC"  -> equal
"AD", "DD"  -> not equal
"gf", "FG"  -> equal
"zz1", ""   -> equal (both are considered empty)
"ZzZz", "ffPFF" -> equal
"kl", "lz"  -> not equal
null, ""    -> equal
``` */

"use strict";

const compare = (s1, s2) => {
    const check = (string) => /\d/.test(string) ? null : string;
    const getValue = (string) => [...string].reduce((acc, char) => char.charCodeAt(0) + acc, 0);

    s1 = check(s1);
    s2 = check(s2);

    return s1 === null || s2 === null ? getValue(s1.toUpperCase()) == getValue(s2.toUpperCase()) : true;
};

console.log(compare("zz1", ""));