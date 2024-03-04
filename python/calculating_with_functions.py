""" ID: 525f3eda17c7cd9f9e000b39

This time we want to write calculations using functions and get the
results. Let's have a look at some examples:

```javascript
seven(times(five())); // must return 35
four(plus(nine())); // must return 13
eight(minus(three())); // must return 5
six(dividedBy(two())); // must return 3
```
```haskell
seven $ times $ five   ->  35 :: Int
four $ plus $ nine     ->  13 :: Int
eight $ minus $ three  ->   5 :: Int
six $ dividedBy $ two  ->   3 :: Int
```
```ruby
seven(times(five)) # must return 35
four(plus(nine)) # must return 13
eight(minus(three)) # must return 5
six(divided_by(two)) # must return 3
```
```python
seven(times(five())) # must return 35
four(plus(nine())) # must return 13
eight(minus(three())) # must return 5
six(divided_by(two())) # must return 3
```
```factor
seven multiplied-by five   ! must evaluate to 35
four plus nine             ! must evaluate to 13
eight minus three          ! must evaluate to 5
six divided-by two         ! must evaluate to 3
```

Requirements:
~~~if:ruby,python
* There must be a function for each number from 0 ("zero") to 9 ("nine")
* There must be a function for each of the following mathematical
operations: plus, minus, times, divided_by * Each calculation consist of
exactly one operation and two numbers * The most outer function
represents the left operand, the most inner function represents the
right operand * Division should be **integer division**. For example,
this should return `2`, not `2.666666...`:
~~~
~~~if:factor
* There must be a word for each number from 0 ("zero") to 9 ("nine") *
There must be a word for each of the following mathematical operations:
plus, minus, multiplied-by, divided-by * Each calculation consist of
exactly one operation and two numbers * The leftmost word represents the
left operand, the rightmost word represents the right operand * Division
should be **integer division**. For example, this should return `2`, not
`2.666666...`:
~~~
~~~if-not:ruby,python,factor
* There must be a function for each number from 0 ("zero") to 9 ("nine")
* There must be a function for each of the following mathematical
operations: plus, minus, times, dividedBy * Each calculation consist of
exactly one operation and two numbers * The most outer function
represents the left operand, the most inner function represents the
right operand * Division should be **integer division**. For example,
this should return `2`, not `2.666666...`:
~~~

```javascript
eight(dividedBy(three()));
```
```haskell
eight $ dividedBy $ three
```
```ruby
eight(divided_by(three))
```
```python
eight(divided_by(three()))
```
```factor
eight divided-by three
``` """

numstr_to_numint = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

opstr_to_oplog = {
    "plus": "+",
    "minus": "-",
    "times": "*",
    "divided_by": "/",
}


def zero(operator: str = ""):
    return eval(f"0{operator}")


def one(operator: str = ""):
    return eval(f"1{operator}")


def two(operator: str = ""):
    return eval(f"2{operator}")


def three(operator: str = ""):
    return eval(f"3{operator}")


def four(operator: str = ""):
    return eval(f"4{operator}")


def five(operator: str = ""):
    return eval(f"5{operator}")


def six(operator: str = ""):
    return eval(f"6{operator}")


def seven(operator: str = ""):
    return eval(f"7{operator}")


def eight(operator: str = ""):
    return eval(f"8{operator}")


def nine(operator: str = ""):
    return eval(f"9{operator}")


def plus(num: str = ""):
    return f"+{num}"


def minus(num: str = ""):
    return f"-{num}"


def times(num: str = ""):
    return f"*{num}"


def divided_by(num: str = ""):
    return f"//{num}"


print(seven(times(five())))
