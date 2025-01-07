"""URL: https://www.codewars.com/kata/5738f5ea9545204cec000155

Bob is a lazy man.

He needs you to create a method that can determine how many
```letters``` (both uppercase and lowercase **ASCII** letters) and
```digits``` are in a given string.



Example:

"hel2!lo" --> 6

"wicked .. !" --> 6

"!?..A" --> 1
"""


def count_letters_and_digits(s: str) -> int:
    return sum(1 for i in s if i.isalpha() or i.isdigit())
