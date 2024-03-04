""" Your job is to write a function which increments a string, to create
a new string.

- If the string already ends with a number, the number should be
  incremented by 1.
- If the string does not end with a number. the number 1 should be
  appended to the new string.

Examples:

`foo -> foo1`

`foobar23 -> foobar24`

`foo0042 -> foo0043`

`foo9 -> foo10`

`foo099 -> foo100`

*Attention: If the number has leading zeros the amount of digits should
be considered.* """


def increment_string(strng):
    if not strng.endswith(tuple("01234567859")):
        return strng + "1"

    if strng.isdigit():
        return f"{str(int(strng) + 1):>0{len(strng)}}"

    for position, i in enumerate(strng[::-1]):
        if not i.isdigit():
            strng_num = strng[len(strng) - position :]
            strng = strng[: len(strng) - position]
            break

    return f"{strng}{str(int(strng_num) + 1):>0{len(strng_num)}}"


print(increment_string("foobar002"))
