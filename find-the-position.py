""" When provided with a letter, return its position in the alphabet.

Input :: "a"

Ouput :: "Position of alphabet: 1" """


def position(alphabet: str) -> str:
    return f"Position of alphabet: {'abcdefghijklmnopqrstuvwxyz'.index(alphabet) + 1}"
