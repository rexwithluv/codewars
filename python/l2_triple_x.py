"""
Given a string, return true if the first instance of "x" in the string is immediately followed by the string "xx".

"abraxxxas" → true
"xoxotrololololololoxxx" → false
"softX kitty, warm kitty, xxxxx" → true
"softx kitty, warm kitty, xxxxx" → false
Note :

capital X's do not count as an occurrence of "x".
if there are no "x"'s then return false
"""


def triple_x(s: str) -> bool:
    if "x" not in s:
        return False

    for c, i in enumerate(s):
        if i == "x":
            if s[c + 1 : c + 3] == "xx":
                return True
            return False


