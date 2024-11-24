"""ID: 5436f26c4e3d6c40e5000282

A [sequence or a series](http://world.mathigon.org/Sequences), in mathematics, is a string of objects, like numbers, that follow a particular pattern. The individual elements in a sequence are called terms. A simple example is `3, 6, 9, 12, 15, 18, 21, ...`, where the pattern is: _"add 3 to the previous term"_.

In this kata, we will be using a more complicated sequence:   `0, 1, 3, 6, 10, 15, 21, 28, ...`
This sequence is generated with the pattern: _"the nth term is the sum of numbers from 0 to n, inclusive"_.

```
[ 0,  1,    3,      6,   ...]
  0  0+1  0+1+2  0+1+2+3
```

## Your Task

Complete the function that takes an integer `n` and returns a list/array of length `abs(n) + 1` of the arithmetic series explained above. When`n < 0` return the sequence with negative terms.

## Examples

```
 5  -->  [0,  1,  3,  6,  10,  15]
-5  -->  [0, -1, -3, -6, -10, -15]
 7  -->  [0,  1,  3,  6,  10,  15,  21,  28]
```"""


def sum_of_n(n: int) -> list[int]:
    lst: list[int] = [0]
    actual_number: int = 0

    for i in range(1, abs(n) + 1):
        actual_number += i
        lst.append(actual_number)

    return lst if n > 0 else [-i for i in lst]
