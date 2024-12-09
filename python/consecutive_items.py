"""ID: 5f6d533e1475f30001e47514

You are given a list of unique integers `arr`, and two integers `a` and
`b`. Your task is to find out whether or not `a` and `b` appear
consecutively in `arr`, and return a boolean value (`True` if `a` and
`b` are consecutive, `False` otherwise).

It is guaranteed that `a` and `b` are both present in `arr`.

~~~if:lambdacalc
### Encodings

purity: `LetRec`
numEncoding: `BinaryScott`

export constructors `nil, cons` for your `List` encoding, and
deconstructor `if` for your `Boolean` encoding.

~~~"""


def consecutive(arr, a, b) -> bool:
    for i in range(1, len(arr)):
        if (arr[i] == a and arr[i - 1] == b) or (arr[i] == b and arr[i - 1] == a):
            return True
    return False
