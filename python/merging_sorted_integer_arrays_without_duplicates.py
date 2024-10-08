"""ID: 573f5c61e7752709df0005d2

Write a function that merges two sorted arrays into a single one. The
arrays only contain integers. Also, the final outcome must be sorted and
not have any duplicate."""


def merge_arrays(first, second):
    return sorted(set(first + second))
