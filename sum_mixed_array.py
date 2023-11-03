""" Given an array of integers as strings and numbers, return the sum of the array values as if all were numbers.

Return your answer as a number. """

def sum_mix(arr: list) -> int:
    counter = 0

    for i in arr:
        counter += int(i)

    return counter