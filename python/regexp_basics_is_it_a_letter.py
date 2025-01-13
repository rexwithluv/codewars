"""URL: https://www.codewars.com/kata/567de72e8b3621b3c300000b

Complete the code which should return `true` if the given object is a
single ASCII letter (lower or upper case), `false` otherwise.
"""

import re


def is_letter(s: str) -> bool:
    if len(s) != 1:
        return False
    return bool(re.search(r"^[a-zA-Z]$", s))
