""" Your task in order to complete this Kata is to write a function
which formats a duration, given as a number of seconds, in a
human-friendly way.

The function must accept a non-negative integer. If it is zero, it just
returns "now". Otherwise, the duration is expressed as a combination of
years, days, hours, minutes and seconds.


It is much easier to understand with an example:

* For seconds = 62, your function should return 
    "1 minute and 2 seconds"
* For seconds = 3662, your function should return
    "1 hour, 1 minute and 2 seconds"
For the purpose of this Kata, a year is 365 days and a day is 24 hours.

Note that spaces are important.

Detailed rules
The resulting expression is made of components like 4 seconds, 1 year,
etc. In general, a positive integer and one of the valid units of time,
separated by a space. The unit of time is used in plural if the integer
is greater than 1.

The components are separated by a comma and a space (", "). Except the
last component, which is separated by " and ", just like it would be
written in English.

A more significant units of time will occur before than a least
significant one. Therefore, 1 second and 1 year is not correct, but 1
year and 1 second is.

Different components have different unit of times. So there is not
repeated units like in 5 seconds and 1 second.

A component will not appear at all if its value happens to be zero.
Hence, 1 minute and 0 seconds is not valid, but it should be just 1 minute.

A unit of time must be used "as much as possible". It means that the
function should not return 61 seconds, but 1 minute and 1 second
instead. Formally, the duration specified by of a component must not be
greater than any valid more significant unit of time. """
from typing import Tuple


def seconds_to(seconds: int) -> Tuple[int]:
    years = seconds // 31536000
    seconds -= years * 31536000

    days = seconds // 86400
    seconds -= days * 86400

    hours = seconds // 3600
    seconds -= hours * 3600

    minutes = seconds // 60
    seconds -= minutes * 60

    return years, days, hours, minutes, seconds


def format_duration(seconds: int) -> str:
    if seconds == 0:
        return "now"
    
    years, days, hours, minutes, seconds = seconds_to(seconds)

    base = []
    if years >= 1:
        if years == 1:
            base.append("1 year")
        else:
            base.append(f"{years} years")
    
    if days >= 1:
        if days == 1:
            base.append("1 day")
        else:
            base.append(f"{days} days")

    if hours >= 1:
        if hours == 1:
            base.append("1 hour")
        else:
            base.append(f"{hours} hours")
    
    if minutes >= 1:
        if minutes == 1:
            base.append("1 minute")
        else:
            base.append(f"{minutes} minutes")
    
    if seconds >= 1:
        if seconds == 1:
            base.append("1 second")
        else:
            base.append(f"{seconds} seconds")


    if len(base) == 1:
        return f"{base[0]}"
    elif len(base) == 2:
        return f"{base[0]} and {base[1]}"
    elif len(base) == 3:
        return f"{base[0]}, {base[1]} and {base[2]}"
    elif len(base) == 4:
        return f"{base[0]}, {base[1]}, {base[2]} and {base[3]}"
    elif len(base) == 5:
        return f"{base[0]}, {base[1]}, {base[2]}, {base[3]} and {base[4]}"


print(format_duration(66663894))
