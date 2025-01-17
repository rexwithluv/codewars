""" URL: https://www.codewars.com/kata/545993ee52756d98ca0010e1

Write a function that takes two arguments: an array and a callback
function (in Ruby: a block).

The function should return `true` if the callback / block returns
`false` for **all** of the items in the array, or if the array is empty;
otherwise return `false`.
"""

def none(lst: list[int], func)-> bool:
    for i in lst:
        if func(i) is True:
            return False
    return True