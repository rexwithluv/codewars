""" ID: 5420fc9bb5b2c7fd57000004

Complete the method which returns the number which is most frequent in the given input array. If there is a tie for most frequent number, return the largest number among them.

Note: no empty arrays will be given.


## Examples

```
[12, 10, 8, 12, 7, 6, 4, 10, 12]              -->  12
[12, 10, 8, 12, 7, 6, 4, 10, 12, 10]          -->  12
[12, 10, 8, 8, 3, 3, 3, 3, 2, 4, 10, 12, 10]  -->   3
``` """


def highest_rank(arr) -> int:
    freq = {}
    for i in arr:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1

    max_freq = max(freq.values())
    max_nums = [i for i in freq.keys() if freq.get(i) == max_freq]
    return max(max_nums)



