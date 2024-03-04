""" Define a function that removes duplicates from an array of non negative numbers and returns it as a result.

The order of the sequence has to stay the same.

Examples:

Input -> Output
[1, 1, 2] -> [1, 2]
[1, 2, 1, 1, 3, 2] -> [1, 2, 3] """

def distinct(lst):
    clean_lst = []

    for i in lst:
        if i not in clean_lst:
            clean_lst.append(i)

    return clean_lst