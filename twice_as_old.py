""" Your function takes two arguments:

- Current father's age (years)
- Current age of his son (years)

Calculate how many years ago the father was twice as old as his son (or
in how many years he will be twice as old). The answer is always greater
or equal to 0, no matter if it was in the past or it is in the future. """


def twice_as_old(dad: int, son: int) -> int:
    return abs(dad - son*2)
