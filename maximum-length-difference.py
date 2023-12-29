""" You are given two arrays `a1` and `a2` of strings. Each string is
composed with letters from `a` to `z`.
Let `x` be any string in the first array and `y` be any string in the
second array. 

  `Find max(abs(length(x) − length(y)))`

If `a1` and/or `a2` are empty return `-1` in each language
except in Haskell (F#) where you will return `Nothing` (None).

#### Example:
```
a1 = ["hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa",
"xxwwkktt", "znnnnfqknaz", "qqquuhii", "dvvvwz"]
a2 = ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]
mxdiflg(a1, a2) --> 13

```

#### Bash note:
 - input : 2 strings with substrings separated by `,`
 - output: number as a string """

from typing import List


def mxdiflg(a1: List[str], a2: List[str]) -> int:
    if len(a1) == 0 or len(a2) == 0:
        return -1

    max_a1 = max(len(i) for i in a1)
    max_a2 = max(len(i) for i in a2)

    min_a1 = min(len(i) for i in a1)
    min_a2 = min(len(i) for i in a2)

    return max(abs(max_a1 - min_a2), abs(max_a2 - min_a1))
