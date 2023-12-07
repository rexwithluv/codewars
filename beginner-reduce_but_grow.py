""" Given a non-empty array of integers, return the result of
multiplying the values together in order.

Example:
[1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24 """

from typing import List
from math import prod

def grow(arr: List[int]) -> int:
    return prod(arr)
    
