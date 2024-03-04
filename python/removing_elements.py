""" Take an array and remove every second element from the array. Always
keep the first element and start removing with the next element.

Example: ["Keep", "Remove", "Keep", "Remove", "Keep", ...] --> ["Keep",
"Keep", "Keep", ...]

None of the arrays will be empty, so you don't have to worry about that!
"""

from typing import List, Union


def remove_every_other(my_list: List[Union[int, str]]) -> List[Union[int, str]]:
    for i in range(len(my_list)):
        if i % 2 == 1:
            my_list[i] = ""
    
    while "" in my_list:
        my_list.remove("")

    return my_list