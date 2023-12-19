""" Create a combat function that takes the player's current health and
the amount of damage recieved, and returns the player's new health.
Health can't be less than <b>0<b>. """


def combat(health: int, damage: int) -> int:
    return health - damage if damage < health else 0
