"""ID: 59c633e7dcc4053512000073

Given a lowercase string that has alphabetic characters only and no spaces, return the highest value of consonant substrings. Consonants are any letters of the alphabet except `"aeiou"`.

We shall assign the following values: `a = 1, b = 2, c = 3, .... z = 26`.

For example, for the word "zodiacs", let's cross out the vowels. We get: "z **~~o~~** d **~~ia~~** c"

```
"zodiac" -> 26
```
The consonant substrings are: `"z"`, `"d"` and `"c"` with values `"z"` = 26, `"di"` = 4 and `"c`" = 3. The highest is 26.

```
"strength" -> 57
```
The consonant substrings are: `"str"` and `"ngth"` with values `"str"` = 19 + 20 + 18 = 57 and `"ngth"` = 14 + 7 + 20 + 8 = 49. The highest is 57.

For C: do not mutate input.

More examples in test cases. Good luck!

If you like this Kata, please try:

[Word values](https://www.codewars.com/kata/598d91785d4ce3ec4f000018)

[Vowel-consonant
lexicon](https://www.codewars.com/kata/59cf8bed1a68b75ffb000026)"""

import re
import string


def solve(s: str) -> int:
    s = re.split(r"[aeiou]+", s)

    groups = []
    for part in s:
        actual_group = 0
        for letter in part:
            actual_group += string.ascii_lowercase.index(letter) + 1
        groups.append(actual_group)
    return max(groups)
