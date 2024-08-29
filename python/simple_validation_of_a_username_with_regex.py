"""ID: 56a3f08aa9a6cc9b75000023

Write a simple regex to validate a username. Allowed characters are:

- lowercase letters,
- numbers,
- underscore

Length should be between 4 and 16 characters (both included)."""

import re


def validate_usr(username: str) -> bool:
    return re.fullmatch(r"[a-z_0-9]{4,16}", username) is not None
