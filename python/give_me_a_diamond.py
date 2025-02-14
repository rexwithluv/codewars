"""URL: https://www.codewars.com/kata/5503013e34137eeeaa001648

Jamie is a programmer, and James' girlfriend. She likes diamonds, and wants a
diamond string from James. Since James doesn't know how to make this happen, he
needs your help.

## Task

You need to return a string that looks like a diamond
shape when printed on the screen, using asterisk (`*`) characters. Trailing
spaces should be removed, and every line must be terminated with a newline
character (`\n`).

Return `null/nil/None/...` if the input is an even number or
negative, as it is not possible to print a diamond of even or negative size.

##
Examples

A size 3 diamond:


```
 *
***
 *
```

...which would appear as a
string of `" *\n***\n *\n"`


A size 5 diamond:

```
  *
 ***
*****
 ***
  *
```
...that is:
```
"  *\n ***\n*****\n ***\n  *\n"
```
"""


def diamond(n: int) -> None | str:
    if n % 2 == 0 or n <= 0:
        return None

    diamond: list[str] = []

    half: int = n // 2
    counter: int = 1
    for i in range(n):
        diamond.append(((counter * "*").center(n)).rstrip())
        counter += 2 if i < half else -2

    return "\n".join(diamond) + "\n"


print(diamond(7))
