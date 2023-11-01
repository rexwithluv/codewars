""" Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.

Note: input will never be an empty string """

def fake_bin(x: str) -> str:
    new_number = ""

    for i in x:
        if int(i) >= 5:
            new_number += "1"
        else:
            new_number += "0"

    return new_number