""" You will be given an array and a limit value. You must check that
all values in the array are below or equal to the limit value. If they
are, return true. Else, return false.

You can assume all values in the array are numbers. """

from typing import Tuple


def small_enough(array: Tuple[int], limit: int) -> bool:
    for i in array:
        if i > limit:
            return False
    return True