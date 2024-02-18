""" ID: 5514e5b77e6b2f38e0000ca9

Given an array of integers of any length, return an array that has 1 added to the value represented by the array.

- the array can't be empty
- only non-negative, single digit integers are allowed

Return `nil` (or your language's equivalent) for invalid inputs.

### Examples

**Valid arrays**

`[4, 3, 2, 5]` would return `[4, 3, 2, 6]`
`[1, 2, 3, 9]` would return `[1, 2, 4, 0]`
`[9, 9, 9, 9]` would return `[1, 0, 0, 0, 0]`
`[0, 1, 3, 7]` would return `[0, 1, 3, 8]`

**Invalid arrays**

`[1, -9]` is invalid because `-9` is **not a non-negative integer**

`[1, 2, 33]` is invalid because `33` is **not a single-digit integer**
"""

from typing import Optional, List


def up_array(arr) -> Optional[List[int]]:
    if len(arr) < 1:
        return None

    for i in arr:
        if i < 0 or len(str(i)) > 1:
            return None

    num = str(int("".join(str(i) for i in arr)) + 1)
    num_lst = [int(i) for i in num]

    if len(arr) - len(num_lst) > 0:
        for i in range(len(arr) - len(num_lst)):
            num_lst.insert(0, 0)

    return num_lst
