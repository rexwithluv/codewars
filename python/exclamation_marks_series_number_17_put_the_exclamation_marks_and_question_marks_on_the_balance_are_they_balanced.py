"""ID: 57fb44a12b53146fe1000136

Each exclamation mark's weight is 2; each question mark's weight is 3.
Putting two strings `left` and `right` on the balance - are they
balanced?

If the left side is more heavy, return `"Left"`; if the right side is
more heavy, return `"Right"`; if they are balanced, return `"Balance"`.

## Examples

```python
"!!", "??"     -->  "Right"
"!??", "?!!"   -->  "Left"
"!?!!", "?!?"  -->  "Left"
"!!???!????", "??!!?!!!!!!!"  -->  "Balance"
```
```haskell
-- For Haskell use the Comparison type defined in Preloaded code
-- data Comparison = Left | Right | Balance deriving (Show, Eq, Enum,
Bounded)

balance :: String -> String -> Comparison

balance "!!" "??" == Right
balance "!??" "?!!" == Left
balance "!?!!" "?!?" == Left
balance "!!???!????" "??!!?!!!!!!!" == Balance
```"""


def balance(left: str, right: str) -> str:
    left_value: int = left.count("!") * 2 + left.count("?") * 3
    right_value: int = right.count("!") * 2 + right.count("?") * 3

    if left_value == right_value:
        return "Balance"
    return "Left" if left_value > right_value else "Right"
