""" Given an array of numbers, check if any of the numbers are the
character codes for lower case vowels (`a, e, i, o, u`).

If they are, change the array value to a string of that vowel.

Return the resulting array. """


def is_vow(inp):
    vow = {97: "a", 101: "e", 105: "i", 111: "o", 117: "u"}
    return [chr(i) if i in vow.keys() else i for i in inp]


print(ord("a"))
print(ord("e"))
print(ord("i"))
print(ord("o"))
print(ord("u"))
