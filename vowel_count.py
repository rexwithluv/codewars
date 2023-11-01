""" Return the number (count) of vowels in the given string.

We will consider a, e, i, o, u as vowels for this Kata (but not y).

The input string will only consist of lower case letters and/or spaces.

 """

def get_count(sentence: str) -> int:
    vowels = ["a", "e", "i", "o", "u"]
    counter = 0

    for i in vowels:
        counter += list(sentence).count(i)
    
    return counter