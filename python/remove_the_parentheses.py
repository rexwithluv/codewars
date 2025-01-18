"""URL: https://www.codewars.com/kata/5f7c38eb54307c002a2b8cc8

Remove the parentheses
=
In this kata you are given a string for example:

```python
"example(unwanted thing)example"
```

Your task is to remove everything inside the parentheses as well as the
parentheses themselves.

The example above would return:

```python
"exampleexample"
```

## Notes
* Other than parentheses only letters and spaces can occur in the
string. Don't worry about other brackets like ```"[]"``` and ```"{}"```
as these will never appear.
* There can be multiple parentheses.
* The parentheses can be nested.
"""


def remove_parentheses(st: str) -> str:
    capt: int = 0
    new_str: str = ""

    for i in st:
        if i == "(":
            capt += 1

        if capt == 0:
            new_str += i

        if i == ")":
            capt -= 1

    return new_str


