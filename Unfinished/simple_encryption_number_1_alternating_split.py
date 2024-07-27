"""ID: 57814d79a56c88e3e0000786

Implement a pseudo-encryption algorithm which given a string `S` and an
integer `N` concatenates all the odd-indexed characters of `S` with all
the even-indexed characters of `S`, this process should be repeated `N`
times.

Examples:

```
encrypt("012345", 1)  =>  "135024"
encrypt("012345", 2)  =>  "135024"  ->  "304152"
encrypt("012345", 3)  =>  "135024"  ->  "304152"  ->  "012345"

encrypt("01234", 1)  =>  "13024"
encrypt("01234", 2)  =>  "13024"  ->  "32104"
encrypt("01234", 3)  =>  "13024"  ->  "32104"  ->  "20314"
```

Together with the encryption function, you should also implement a
decryption function which reverses the process.

If the string `S` is an empty value or the integer `N` is not positive,
return the first argument without changes.

___

This kata is part of the Simple Encryption Series:

* [Simple Encryption #1 - Alternating Split](https://www.codewars.com/kata/simple-encryption-number-1-alternating-split)
* [Simple Encryption #2 - Index-Difference](https://www.codewars.com/kata/simple-encryption-number-2-index-difference)
* [Simple Encryption #3 - Turn The Bits Around](https://www.codewars.com/kata/simple-encryption-number-3-turn-the-bits-around)
* [Simple Encryption #4 - Qwerty](https://www.codewars.com/kata/simple-encryption-number-4-qwerty)

Have fun coding it and please don't forget to vote and rank this kata!
:-)"""

from typing import List, Tuple


def sep_even_odd(string: str) -> Tuple[List[int], List[str]]:
    even = []
    odd = []

    for i in range(len(string)):
        if i % 2 == 0:
            even.append(string[i])
        else:
            odd.append(string[i])

    return even, odd


def decrypt(encrypted_text: str, n: int) -> str:
    for _ in range(n):
        even, odd = sep_even_odd(encrypted_text)

        encrypted_text = "".join(odd + even)

    return list(encrypted_text)


def encrypt(text: str, n: int) -> str:
    for _ in range(n):
        even, odd = sep_even_odd(text)

        text = "".join(odd) + "".join(even)

    return text


test = "This is a test!"
print(test)

test_encrypted = encrypt(test, 3)
print(test_encrypted)

test_decrypted = decrypt(test_encrypted, 3)
print(test_decrypted)
