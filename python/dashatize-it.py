""" Given an integer, return a string with dash `'-'` marks before and
after each odd digit, but do not begin or end the string with a dash
mark.


Ex:
```javascript
274 -> '2-7-4'
6815 -> '68-1-5'
``` """


def dashatize(n):
    n = str(abs(n))

    lst = []
    new_str = ""
    for p, i in enumerate(n):
        if int(i) % 2 == 1:
            if len(new_str) > 0:
                lst.append(new_str)
                new_str = ""
            lst.append(i)
        else:
            new_str += str(i)

        if p == len(n) - 1 and len(new_str) > 0:
            lst.append(new_str)

    return "-".join(lst)
