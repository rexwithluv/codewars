"""ID: 5809b62808ad92e31b000031

In this kata, you will do addition and subtraction on a given string. The return value must be also a string.

**Note:** the input will not be empty.

## Examples

```
"1plus2plus3plus4"  --> "10"
"1plus2plus3minus4" -->  "2"
```"""


def calculate(s: str) -> str:
    return str(eval(s.replace("plus", "+").replace("minus", "-")))
