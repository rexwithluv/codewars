"""ID: 5ae7e3f068e6445bc8000046

# Scenario

*You're saying good-bye your best friend* , **_See you next happy year_** .

**_Happy Year_** *is the year with only distinct digits* , (e.g) **_2018_**

___
# Task

**_Given_** a year, **_Find_** **_The next happy year_** or **_The closest year You'll see your best friend_**      ![!alt](https://i.imgur.com/mdX8dJP.png) ![!alt](https://i.imgur.com/mdX8dJP.png)

___
# Notes

* **_Year_** Of Course always **_Positive_** .
* **_Have no fear_** , *It is guaranteed that the answer exists* .
* **_It's not necessary_** *that the year passed to the function is Happy one* .
* **_Input Year with in range_** *(1000  ≤  y  ≤  9000)*

____
# Input >> Output Examples:

```cpp
nextHappyYear (7712) ==> return (7801)
```
```prolog
next_happy_year(7712, 7801).
```

## **_Explanation_**:

As the **_Next closest year with only distinct digits is_**  *7801* .
___

```cpp
nextHappyYear (8989) ==> return (9012)
```
```prolog
next_happy_year(8989, 9012).
```

## **_Explanation_**:

As the **_Next closest year with only distinct digits is_**  *9012* .
___

```cpp
nextHappyYear (1001) ==> return (1023)
```
```prolog
next_happy_year(1001, 1023).
```


## **_Explanation_**:

As the **_Next closest year with only distinct digits is_**  *1023* .
___
___
___

# [Playing with Numbers Series](https://www.codewars.com/collections/playing-with-numbers)

# [Playing With Lists/Arrays Series](https://www.codewars.com/collections/playing-with-lists-slash-arrays)

# [For More Enjoyable Katas](http://www.codewars.com/users/MrZizoScream/authored)
___

## ALL translations are welcomed

## Enjoy Learning !!
# Zizou"""


def next_happy_year(year: int) -> int:
    happy_year: int = year + 1
    while len(str(year)) != len(set(str(happy_year))):
        happy_year += 1
    return happy_year
