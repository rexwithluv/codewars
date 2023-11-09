""" Given an array of integers, find the one that appears an odd number of times.

There will always be only one integer that appears an odd number of times.

Examples
[7] should return 7, because it occurs 1 time (which is odd).
[0] should return 0, because it occurs 1 time (which is odd).
[1,1,2] should return 2, because it occurs 1 time (which is odd).
[0,1,0,1,0] should return 0, because it occurs 3 times (which is odd).
[1,2,2,3,3,3,4,3,3,3,2,2,1] should return 4, because it appears 1 time (which is odd). """

def find_it(lst: list[int]) -> int:
    # Creamos el diccionario con todos los números de la lista
    diccionary = {}
    for i in lst:
        if i not in diccionary:
            diccionary[i] = 0

    # Contamos las veces que aparece cada número en la lista
    for i in lst:
        diccionary[i] += 1

    # Comprobamos cual de los elementos aparece un número impar de veces
    print(diccionary)
    for i in diccionary:
        if diccionary[i] % 2 == 1:
            return i
    

print(find_it([1,1,3,3,3,3,3,3,4,4,5]))