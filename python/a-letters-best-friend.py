""" ### Task
Given a string, return if a given letter always appears immediately
before another given letter.

### Worked Example
```
("he headed to the store", "h", "e") ➞ True

# All occurences of "h": ["he", "headed", "the"]
# All occurences of "h" have an "e" after it.
# Return True

('abcdee', 'e', 'e') ➞ False

# For first "e" we can get "ee"
# For second "e" we cannot have "ee"
# Return False
```
### Examples
```
("i found an ounce with my hound", "o", "u") ➞ True

("we found your dynamite", "d", "y") ➞ False
```
### Notes
- All sentences will be given in lowercase. """


def best_friend(txt, a, b):
    try:
        indexs = [p for p, i in enumerate(txt) if i == a]
        for i in indexs:
            if txt[i + 1] != b:
                return False

        return True

    except IndexError:
        return False


best_friend("he hounded to the store", "h", "e")
