"""ID: 57eaec5608fed543d6000021

Given a mixed array of number and string representations of integers,
add up the non-string integers and subtract the total of the string
integers.

Return as a number."""


def div_con(x: list[int | str]) -> int:
    return sum(i if type(i) is int else -int(i) for i in x)
