"""ID: 5939ab6eed348a945f0007b2

Given a string of space separated words, return the longest word.
If there are multiple longest words, return the rightmost longest word.

#### Examples

    "red white blue"  =>  "white"
    "red blue gold"   =>  "gold" """


def longest_word(string_of_words: str) -> str:
    return sorted(string_of_words.split(" "), key=len)[-1]
