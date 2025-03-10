"""URL: https://www.codewars.com/kata/5a1ee4dfffe75f0fcb000145

For this game of `BINGO`, you will receive a single array of 10 numbers
from 1 to 26 as an input. Duplicate numbers within the array are
possible.

Each number corresponds to their alphabetical order letter (e.g. 1 = A.
2 = B, etc). Write a function where you will win the game if your
numbers can spell `"BINGO"`. They do not need to be in the right order
in the input array. Otherwise you will lose. Your outputs should be
`"WIN"` or `"LOSE"` respectively.

~~~if:lambdacalc
#### Preloaded

`WIN, LOSE` are `Preloaded` for your convenience. You should return one
of these values, as appropriate.

#### Encodings

purity: `LetRec`
numEncoding: `Church`
export constructors `nil, cons` for your `List` encoding
~~~
"""


def bingo(array: list[int]) -> str:
    valid: list[int] = [2, 9, 14, 7, 15]  # "BINGO"
    return "WIN" if all(i in array for i in valid) else "LOSE"
