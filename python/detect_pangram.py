""" A pangram is a sentence that contains every single letter of the alphabet at least once.
For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation. """
def is_pangram(s: str) -> bool:
    lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    s = s.lower()

    s_contains = []
    for i in s:
        if i not in s_contains and i in lst:
            s_contains.append(i)

    if sorted(s_contains) == lst:
        return True
    return False

print(is_pangram("The quick, brown fox jumps over the lazy dog!"))
