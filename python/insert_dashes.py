"""ID: 55960bbb182094bc4800007b

Write a function that takes an integer `num` (`num >= 0`) and inserts dashes (`'-'`) between each two **odd** digits in `num`.

## Examples

```python
454793 ---> "4547-9-3"
     0 ---> "0"
     1 ---> "1"
13579  ---> "1-3-5-7-9"
 86420 ---> "86420"
```"""


def is_odd(num: int) -> bool:
    return num % 2 == 1


def insert_dash(num: int) -> str:
    num = str(num)
    new_string = "0"
    for i in num:
        new_string += "-" + i if is_odd(int(i)) and is_odd(int(new_string[-1])) else i
    return new_string[1:]

