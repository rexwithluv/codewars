""" Given a string of words, you need to find the highest scoring word.

Each letter of a word scores points according to its position in the
alphabet: a = 1, b = 2, c = 3 etc.

For example, the score of abad is 8 (1 + 2 + 1 + 4).

You need to return the highest scoring word as a string.

If two words score the same, return the word that appears earliest in
the original string.

All letters will be lowercase and all inputs will be valid. """

def high(string: str) -> str:
    string = string.split()
    abc = "abcdefghijklmnopqrstuvwxyz"
    
    lst_len = []
    for i in string:
        temp_lst = []
        for j in i:
            temp_lst.append(abc.index(j) + 1)
        lst_len.append(sum(temp_lst))

    return string[lst_len.index(max(lst_len))]
