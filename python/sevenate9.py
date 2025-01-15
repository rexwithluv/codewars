"""URL: https://www.codewars.com/kata/559f44187fa851efad000087

Write a function that removes every lone `9` that is inbetween `7`s.

```javascript
"79712312" --> "7712312"
"79797"    --> "777"
```
"""


def seven_ate9(string: str) -> str:
    new_string: str = ""

    for i in range(len(string)):
        if string[i] == "9":
            try:
                if string[i - 1] != "7" or string[i + 1] != "7":
                    new_string += string[i]
            except IndexError:
                new_string += string[i]
        else:
            new_string += string[i]

    return new_string


