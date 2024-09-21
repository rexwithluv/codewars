"""ID: 5a9e86705ee396d6be000091

Given an array with exactly 5 strings `"a"`, `"b"` or `"c"` (`char`s in
Java, `character`s in Fortran), check if the array contains three and
two of the same values.

## Examples

```
["a", "a", "a", "b", "b"] ==> true  // 3x "a" and 2x "b"
["a", "b", "c", "b", "c"] ==> false // 1x "a", 2x "b" and 2x "c"
["a", "a", "a", "a", "a"] ==> false // 5x "a"
```"""


def check_three_and_two(array: list[str]) -> bool:
    if len(set(array)) != 2 or array.count(array[0]) not in (2, 3):
        return False
    return True
