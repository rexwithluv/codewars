""" Simple, given a string of words, return the length of the shortest
word(s).

String will never be empty and you do not need to account for different
data types. """

def find_short(string: str) -> int:
    string = string.split()
    lst_len = [len(i) for i in string]

    return min(lst_len)