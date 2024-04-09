"""ID: 5a3e1319b6486ac96f000049

In this Kata your task q be to return the count of pairs that have
consecutive numbers as follows:
```Haskell
pairs([1,2,5,8,-4,-3,7,6,5]) = 3
The pairs are selected as follows [(1,2),(5,8),(-4,-3),(7,6),5]
--the first pair is (1,2) and the numbers in the pair are consecutive;
Count = 1
--the second pair is (5,8) and are not consecutive
--the third pair is (-4,-3), consecutive. Count = 2
--the fourth pair is (7,6), also consecutive. Count = 3.
--the last digit has no pair, so we ignore.
```

More examples in the test cases.

Good luck!

Please also try [Simple time
difference](https://www.codewars.com/kata/5b76a34ff71e5de9db0000f2)"""


def pairs(arr: list[int]) -> int:
    if len(arr) % 2 == 1:
        arr = arr[:-1]

    pairs = [(arr[i - 1], arr[i]) for i in range(len(arr)) if i % 2 == 1]

    return sum(1 for i in pairs if i[0] + 1 == i[1] or i[0] - 1 == i[1])


print(pairs([1, 2, 5, 8, -4, -3, 7, 6, 5]))
