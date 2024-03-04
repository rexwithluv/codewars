""" Task
You will be given an array of numbers. You have to sort the odd numbers
in ascending order while leaving the even numbers at their original
positions.

Examples [7, 1]  =>  [1, 7]
[5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
[9, 8,7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0] """

from typing import List


def sort_array(source_array: List[int]) -> List[int]:
    odd = sorted([i for i in source_array if i % 2 == 1])
    positions = [count for count, i in enumerate(source_array) if i % 2 == 1]

    for i in range(len(source_array)):
        if i in positions:
            source_array[i] = odd.pop(0)

    return source_array

