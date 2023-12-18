""" Write a function `centroid(c)` to calculate the centroid of 3D
coordinates.

Return the results as a list of floats. Round the values to two decimal
places. """

from typing import List


def centroid(coordinates: List[List[float]]) -> List[float]:
    lst = []
    for i in range(3):
        tmp = [j[i] for j in coordinates]
        lst.append(round(sum(tmp) / len(tmp), 2))

    return lst
