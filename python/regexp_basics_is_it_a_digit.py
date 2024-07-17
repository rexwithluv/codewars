"""ID: 567bf4f7ee34510f69000032

Implement `String#digit?` (in Java `StringUtils.isDigit(String)`), which
should return `true` if given object is a digit (0-9), `false`
otherwise."""


def is_digit(n: str):
    import re

    if re.match("\d", n) and len(n) == 1:
        return True
    return False
