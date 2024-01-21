""" Given a string made up of letters a, b, and/or c, switch the
position of letters a and b (change a to b and vice versa). Leave any
incidence of c untouched.

Example:

'acb' --> 'bca'<br>
'aabacbaa' --> 'bbabcabb' """


def switcheroo(s):
    new_str = ""
    for i in s:
        if i == "a":
            new_str += "b"
        elif i == "b":
            new_str += "a"
        else:
            new_str += i

    return new_str
