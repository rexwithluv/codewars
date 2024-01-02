""" Input: Array of elements

["h","o","l","a"]

Output: String with comma delimited elements of the array in th same
order.

"h,o,l,a"

Note: if this seems too simple for you try [the next
level](https://www.codewars.com/kata/5711d95f159cde99e0000249)

Note2: the input data can be: boolean array, array of objects, array of
string arrays, array of number arrays... 😕 """


def print_array(arr):
    return ",".join(str(i) for i in arr)
