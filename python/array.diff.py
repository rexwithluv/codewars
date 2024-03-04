""" Your goal in this kata is to implement a difference function, which
subtracts one list from another and returns the result.

It should remove all values from list a, which are present in list b
keeping their order.

array_diff([1,2],[1]) == [2]
If a value is present in b, all of its occurrences must be removed from
the other:

array_diff([1,2,2,2,3],[2]) == [1,3] """
from typing import List

def array_diff(arr1: List[int], arr2: List[int]) -> List[int]:
    new_arr = [i for i in arr1 if i not in arr2]

    return new_arr

    