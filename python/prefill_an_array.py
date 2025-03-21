"""URL: https://www.codewars.com/kata/54129112fb7c188740000162

Create the function `prefill` that returns an array of `n` elements that
all have the same value `v`.  See if you can do this *without* using a
loop.

You have to validate input:

 * `v` can be *anything* (primitive or otherwise)
 * if `v` is ommited, fill the array with `undefined`
 * if `n` is 0, return an empty array
 * if `n` is anything other than an **integer** or **integer-formatted** string (e.g. `'123'`) that is `>=0`, throw a `TypeError`

When throwing a `TypeError`, the message should be `n is invalid`, where
you replace `n` for the actual value passed to the function.

Code Examples

```javascript
    prefill(3,1) --> [1,1,1]

    prefill(2,"abc") --> ['abc','abc']

    prefill("1", 1) --> [1]

    prefill(3, prefill(2,'2d'))
      --> [['2d','2d'],['2d','2d'],['2d','2d']]

    prefill("xyz", 1)
      --> throws TypeError with message "xyz is invalid"
```
```ruby
    prefill(3,1) --> [1,1,1]

    prefill(2,"abc") --> ['abc','abc']

    prefill("1", 1) --> [1]

    prefill(3, prefill(2,'2d'))
      --> [['2d','2d'],['2d','2d'],['2d','2d']]

    prefill("xyz", 1)
      --> throws TypeError with message "xyz is invalid"
```
```python
    prefill(3,1) --> [1,1,1]

    prefill(2,"abc") --> ['abc','abc']

    prefill("1", 1) --> [1]

    prefill(3, prefill(2,'2d'))
      --> [['2d','2d'],['2d','2d'],['2d','2d']]

    prefill("xyz", 1)
      --> throws TypeError with message "xyz is invalid"
```
```coffeescript
    prefill 3, 1 #returns [1, 1, 1]

    prefill 2, "abc" #returns ["abc","abc"]

    prefill "1", 1 #returns [1]

    prefill 3, prefill(2, "2d")
      #returns [['2d','2d'],['2d','2d'],['2d','2d']]

    prefill "xyz", 1
      #throws TypeError with message "xyz is invalid"
```
"""


def prefill(n: int, v: any = None) -> list[any]:
    try:
        n = int(n)
        return [v for _ in range(n)]
    except:
        raise TypeError(f"{n} is invalid")
