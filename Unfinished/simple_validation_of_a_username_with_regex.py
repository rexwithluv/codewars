"""ID: 56a3f08aa9a6cc9b75000023

Write a simple regex to validate a username. Allowed characters are:

- lowercase letters,
- numbers,
- underscore

Length should be between 4 and 16 characters (both included)."""

import re

def validate_usr(username: str) -> bool:
    if 4 > len(username) or len(username) > 16:
        return False

    for i in username:
        if i.isupper():
            return False

        if i.isspace():
            return False

        if i.isalpha():
            pass

    return True

import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
print(x)