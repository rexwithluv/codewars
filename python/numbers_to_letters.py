"""ID: 57ebaa8f7b45ef590c00000c

Given an array of numbers (in string format), you must return a string.
The numbers correspond to the letters of the alphabet in reverse order:
a=26, z=1 etc. You should also account for `'!'`, `'?'` and `' '` that
are represented by '27', '28' and '29' respectively.

All inputs will be valid."""


def switcher(arr: str) -> str:
    abc = " ?!abcdefghijklmnopqrstuvwxyz"[::-1]
    return "".join(abc[int(i) - 1] for i in arr)


switcher("puta")
