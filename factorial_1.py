""" ID: 57a049e253ba33ac5e000212

Your task is to write function `factorial`.

https://en.wikipedia.org/wiki/Factorial """

from math import prod


def factorial(n) -> int:
    return prod(i for i in range(1, n + 1))
