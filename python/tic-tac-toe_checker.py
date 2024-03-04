from typing import Union, List, Tuple

def win_row(lst: List[int]) -> Union[None, int]:
    for i in lst:
        if i[0] == 1 and i[1] == 1 and i[2] == 1:
            return 1
        elif i[0] == 2 and i[1] == 2 and i[2] == 2:
            return 2


def win_column(lst: List[int]) -> Union[None, int]:
    # This block transposes the list
    transpose = []
    for i in range(3):
        add_to_transpose = []
        for j in lst:
            add_to_transpose.append(j[i])
        transpose.append(add_to_transpose)

    # Here we check if you have won, who and in which column.
    for count, i in enumerate(transpose):
        if i[0] == 1 and i[1] == 1 and i[2] == 1:
            return 1
        elif i[0] == 2 and i[1] == 2 and i[2] == 2:
            return 2

def win_diagonally(lst: List[int]) -> Union[None, int]:
    # With this we find out the descending diagonal
    diagonal = []
    for count, i in enumerate(lst):
        diagonal.append(i[count])

    if diagonal[0] == 1 and diagonal[1] == 1 and diagonal[2] == 1:
        return 1
    elif diagonal[0] == 2 and diagonal[1] == 2 and diagonal[2] == 2:
        return 2

    # With this we find out the ascending diagonal
    diagonal = []
    for count, i in enumerate(reversed(lst)):
        diagonal.append(i[count])

    if diagonal[0] == 1 and diagonal[1] == 1 and diagonal[2] == 1:
        return 1
    elif diagonal[0] == 2 and diagonal[1] == 2 and diagonal[2] == 2:
        return 2


def is_solved(table: List[str]) -> Union[None, str]:
    if isinstance(win_row(table), int):
        return win_row(table)
    elif isinstance(win_column(table), int):
        return win_column(table)
    elif isinstance(win_diagonally(table), int):
        return win_diagonally(table)
    
    for i in table:
        for j in i:
            if j == 0:
                return -1
    
    return 0

board = [[1,2,0],
         [0,1,2],
         [0,0,1]]
        
print(is_solved(board))