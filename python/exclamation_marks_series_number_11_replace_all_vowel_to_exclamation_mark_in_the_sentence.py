"""ID: 57fb09ef2b5314a8a90001ed

### Description:

 Replace all vowel to exclamation mark in the sentence. `aeiouAEIOU` is
 vowel.

### Examples

```
replace("Hi!") === "H!!"
replace("!Hi! Hi!") === "!H!! H!!"
replace("aeiou") === "!!!!!"
replace("ABCDE") === "!BCD!"
```"""


def replace_exclamation(st: str) -> str:
    return "".join(i if i not in "aeiouAEIOU" else "!" for i in st)
