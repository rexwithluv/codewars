""" Your task is to sum the differences between consecutive pairs in the
array in descending order.

## Example

```
[2, 1, 10]  -->  9
```

In descending order: `[10, 2, 1]`

Sum: `(10 - 2) + (2 - 1) = 8 + 1 = 9`

If the array is empty or the array has only one element the result
should be `0` (`Nothing` in Haskell, `None` in Rust).

~~~if:lambdacalc
#### Encodings

purity: `LetRec`
numEncoding: `BinaryScott`
export constructors `nil, cons` for your `List` encoding
~~~ """


def sum_of_differences(arr):
    old_arr = sorted(arr, reverse=True)
    new_arr = []

    for i in range(len(arr)):
        try:
            new_arr.append(old_arr[i] - old_arr[i + 1])
        except IndexError:
            return sum(new_arr)

    return 0


sum_of_differences([2, 1, 10])
