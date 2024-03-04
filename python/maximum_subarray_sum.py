""" The maximum sum subarray problem consists in finding the maximum sum
of a contiguous subsequence in an array or list of integers:

max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]) # should be 6: [4, -1, 2,
1] Easy case is when the list is made up of only positive numbers and
the maximum sum is the sum of the whole array. If the list is made up of
only negative numbers, return 0 instead.

Empty list is considered to have zero greatest sum. Note that the empty
list or array is also a valid sublist/subarray. """

from typing import List, Union


def check_special(arr: List[int]) -> Union[int, None]:
    if len(arr) == 0:
        return 0
    
    positive = 0
    for i in arr:
        if i > 0:
            positive += 1
    
    if positive == len(arr):
        return sum(arr)
    elif positive == 0:
        return 0


def max_sequence(arr: List[int]) -> int:
    special = check_special(arr)
    if isinstance(special, int):
        return special
    
    max_current = max_global = arr[0]

    for i in range(1, len(arr)):
        max_current = max(arr[i], max_current + arr[i])
        max_global = max(max_global, max_current)
    
    return max_global
