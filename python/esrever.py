"""ID: 5413759479ba273f8100003d

Write a function `reverse` which reverses a list (or in clojure's case,
any list-like data structure)

(the dedicated builtin(s) functionalities are deactivated)"""


def reverse(lst) -> list[any]:
    long = len(lst)

    for i in range(long // 2):
        lst[i], lst[long - 1 - i] = lst[long - 1 - i], lst[i]

    return lst
