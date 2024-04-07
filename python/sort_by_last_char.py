"""ID: 57eba158e8ca2c8aba0002a0

Given a string of words (x), you need to return an array of the words,
sorted alphabetically by the final character in each.

If two words have the same last letter, the returned array should show
them in the order they appeared in the given string.

All inputs will be valid."""



def last(s: str) -> list[str]:
    s = s.split()

    lst = []
    abc = "abcdefghijklmnopqrstuvwxyz"
    for letter in abc:

        for word in s:
            if word.endswith(letter):
                lst.append(word)

    return lst


print(last("man i need a taxi up to ubud"))
