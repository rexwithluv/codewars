""" Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).

Examples:

solution('abc', 'bc') # returns true
solution('abc', 'd') # returns false """

""" def solution(text, ending):
    if ending in text:
        return True
    return False """

def solution(text, ending):
    final = text[-len(ending):len(text)]

    if final == ending:
        return True
    return False