""" - Kids drink toddy.
- Teens drink coke.
- Young adults drink beer.
- Adults drink whisky.

Make a function that receive age, and return what they drink.

**Rules:**

- Children under 14 old.
- Teens under 18 old.
- Young under 21 old.
- Adults have 21 or more.

**Examples: (Input --> Output)**

```
13 --> "drink toddy"
17 --> "drink coke"
18 --> "drink beer"
20 --> "drink beer"
30 --> "drink whisky"
``` """


def people_with_age_drink(age: int) -> str:
    string = "drink "
    if age <= 13:
        return string + "toddy"
    elif age <= 17:
        return string + "coke"
    elif age <= 20:
        return string + "beer"
    else:
        return string + "whisky"
