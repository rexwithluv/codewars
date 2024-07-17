"""ID: 598f76a44f613e0e0b000026

Your task in this kata is to implement a function that calculates the
sum of the integers inside a string. For example, in the string
<code>"The30quick20brown10f0x1203jumps914ov3r1349the102l4zy dog"</code>,
the sum of the integers is <code>3635</code>.

*Note: only positive integers will be tested.*"""


def sum_of_integers_in_string(string: str) -> int:
    numbers = []
    actual_number = ""

    for i in string:
        if i.isdigit():
            actual_number += i
        elif not i.isdigit() and len(actual_number) > 0:
            numbers.append(actual_number)
            actual_number = ""

    if len(actual_number) > 0:
        numbers.append(actual_number)

    return sum(int(i) for i in numbers)
