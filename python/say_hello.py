""" ID: 55955a48a4e9c1a77500005a

Say hello!

Write a function to greet a person. Function will take name as input and greet the person by saying hello.
Return null/nil/None if input is empty string or null/nil/None.

Example:

```javascript
greet("Niks") === "hello Niks!";
greet("") === null; // Return null if input is empty string
greet(null) === null; // Return null if input is null
```
```coffeescript
greet("Niks") === "hello Niks!";
greet("") === null; // Return null if input is empty string
greet(null) === null; // Return null if input is null
```
```ruby
greet("Niks") == "hello Niks!"
greet("") == nil; # Return nil if input is empty string
greet(nil) == nil; # Return nil if input is nil
```
```csharp
greet("Niks") == "hello Niks!"
greet("") == null; // Return null if input is empty string
greet(null) == null; // Return null if input is null
```
```python
greet("Niks") --> "hello Niks!"
greet("")    --> None # Return None if input is empty string
greet(None)  --> None # Return None if input is None
``` """

def greet(name:str) -> str | None:
    if type(name) is not str or len(name) == 0:
        return None
    return f"hello {name}!"