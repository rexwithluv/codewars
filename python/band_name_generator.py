"""ID: 59727ff285281a44e3000011

My friend wants a new band name for her band. She like bands that use
the formula: "The" + a noun with the first letter capitalized, for
example:

`"dolphin" -> "The Dolphin"`

However, when a noun STARTS and ENDS with the same letter, she likes to
repeat the noun twice and connect them together with the first and last
letter, combined into one word (WITHOUT "The" in front), like this:

`"alaska" -> "Alaskalaska"`

Complete the function that takes a noun as a string, and returns her
preferred band name written as a string."""


def band_name_generator(name: str) -> str:
    if name[0] == name[-1]:
        name += name[1:]
    else:
        name = "the " + name
    return name.title()
