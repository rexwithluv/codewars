""" ID: 5899dc03bc95b1bf1b0000ad

Given a set of numbers, return the additive inverse of each. Each
positive becomes negatives, and the negatives become positives.

~~~if-not:racket
```
invert([1,2,3,4,5]) == [-1,-2,-3,-4,-5]
invert([1,-2,3,-4,5]) == [-1,2,-3,4,-5]
invert([]) == []
```
~~~

```if:javascript,python,ruby,php,elixir,dart,go
You can assume that all values are integers. Do not mutate the input
array/list.
```

```if:c,riscv
### Notes:
- All values are greater than `INT_MIN`
- The input should be modified, not returned.
```
~~~if:racket
```racket
(invert '(1 2 3 4 5))   ; '(-1 -2 -3 -4 -5)
(invert '(1 -2 3 -4 5)) ; '(-1 2 -3 4 -5)
(invert '())            ; '()
```
~~~

~~~if:riscv
RISC-V: The function signature is:

```c
void invert(int *arr, size_t size);
```

The input array is `arr` which contains `size` elements. Mutate the
array in-place according to the above specification. You do not need to
return anything.
~~~ """


def invert(lst):
    return [i * -1 for i in lst]
