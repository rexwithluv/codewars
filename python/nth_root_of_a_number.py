"""URL: https://www.codewars.com/kata/5520714decb43308ea000083

Given two numbers `x` and `n`, calculate the (positive) nth root of `x`;
this means that being `r = result`, `r^n = x`


## Examples
```
x = 4     n = 2  -->  2    # the square root of 4 is 2     2^2 = 4
x = 8     n = 3  -->  2    # the cube root of 8 is 2       2^3 = 8
x = 256   n = 4  -->  4    # the 4th root of 256 is 4      4^4 = 256
x = 9     n = 2  -->  3    # the square root of 9 is 3     3^2 = 9
x = 6.25  n = 2  -->  2.5  #                             2.5^2 = 6.25
```

### Notes:

* `4 <= x < 10 ^ 20`
* `4 <= n <= 50`

Good luck!
"""


def root(x: int, n: int) -> float:
    return x ** (1 / n)
