""" Write a function which removes from string all non-digit characters
and parse the remaining to number. E.g: "hell5o wor6ld" -> 56

Function:
```javascript
getNumberFromString(s)
```

```ruby
get_number_from_string(s)
```

```csharp
GetNumberFromString(string s)
``` """


def get_number_from_string(st):
    return int("".join(i for i in st if i in "0123456789"))
