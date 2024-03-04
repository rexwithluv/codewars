""" Write a function to split a string and convert it into an array of
words.

### Examples (Input ==> Output):

``` "Robin Singh" ==> ["Robin", "Singh"]

"I love arrays they are my favorite" ==> ["I", "love", "arrays", "they",
"are", "my", "favorite"] ``` """

from typing import List


def string_to_array(s: str) -> List[str]:
    return s.split() if len(s) > 0 else [""]