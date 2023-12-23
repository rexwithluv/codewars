""" Given a string, capitalize the letters that occupy even indexes and
odd indexes separately, and return as shown below. Index `0` will be
considered even.

For example, `capitalize("abcdef") = ['AbCdEf', 'aBcDeF']`. See test
cases for more examples.

The input will be a lowercase string with no spaces.

Good luck!

If you like this Kata, please try: 

[Indexed capitalization]
(https://www.codewars.com/kata/59cfc09a86a6fdf6df0000f1)

[Even-odd disparity]
(https://www.codewars.com/kata/59c62f1bdcc40560a2000060) """

from typing import List


def capitalize(s: str) -> List[str]:
    one = ""
    for i in range(len(s)):
        if i % 2 == 0:
            one += s[i].upper()
        else:
            one += s[i].lower()

    return [one, one.swapcase()]
