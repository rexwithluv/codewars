"""URL: https://www.codewars.com/kata/61daff6b2fdc2a004328ffe4

## Task

Consider an n-th-degree polynomial with integer coefficients:


```math
x^n  + a_1*x^{n-1} + ... + a_{n-1}*x + a_n
```

Let's call this polynomial
compact if it has only **integer** roots which are **non-repeating** and **non-
zero** and  `$|a_n|$` is minimal.

Your task is to ﬁnd the maximum and minimum
values of `$a_1$` in the compact polynomial.

You're given the degree of the
polynomial: `$n$`  `$(1≤n≤10^{18})$`.

```if:python
Return a `tuple` (min, max).
```

```if:cpp
Return a `pair<long long, long long>` {min, max}.
```

```if:c
Assign the correct values to the min and max pointers.
```

#### Note

Test
feedback is minimal as part of this puzzle.

## Examples

```if:python
``first_coefficient(1) => (-1, 1)``
```

```if:cpp
``first_coefficient(1) =>
{-1, 1}``
```


```if:c
``first_coefficient(1, &a, &b) => a := -1; b := 1``
```
"""


def first_coefficient(n: int) -> tuple[int]:
    return (0, 0) if n % 2 == 0 else (-(n + 1) // 2, (n + 1) // 2)
