"""URL: https://www.codewars.com/kata/559e10e2e162b69f750000b4

A zero-indexed array ```arr``` consisting of n integers is given. The dominator
of array ```arr``` is the value that occurs in <b>more</b> than half of the
elements of ```arr```.<br/>

For example, consider array ```arr``` such that

```arr = [3,4,3,2,3,1,3,3]```<br/> The dominator of ```arr``` is 3 because it
occurs in 5 out of 8 elements of ```arr``` and 5 is more than a half of 8.<br/>

Write a function ```dominator(arr)``` that, given a zero-indexed array ```arr```
consisting of n integers, returns the dominator of ```arr```. The function
should return −1 if array does not have a dominator. All values in ```arr```
will be >=0.
"""

from collections import defaultdict


def dominator(arr):
    if len(arr) == 0:
        return -1

    freq: dict[int, int] = defaultdict(int)
    for i in arr:
        freq[i] += 1

    dominator = max(freq, key=lambda x: freq[x])
    return dominator if freq[dominator] > len(arr) // 2 else -1


print(dominator([3, 4, 3, 2, 3, 1, 3, 3]))
