"""ID: 538835ae443aae6e03000547

Create a function `add(n)`/`Add(n)` which returns a function that always
adds n to any number

Note for Java: the return type and methods have not been provided to
make it a bit more challenging.

```javascript
var addOne = add(1);
addOne(3); // 4

var addThree = add(3);
addThree(3); // 6
```
```python
add_one = add(1)
add_one(3)  # 4

add_three = add(3)
add_three(3) # 6
```
```haskell
addOne = add 1
addOne 3 `shouldBe` 4
```
```fsharp
addOne = add 1
addOne 3 # 4
```
```swift
addOne = add(1)
addOne(3) // 4
```
```csharp
Func<double, double> AddOne = Kata.Add(1);
AddOne(3) => 4
```
```java
...returnType addOne = Kata.add(1);
addOne.method(3) => 4
```
```go
var addOne = Add(1)
addOne(3) // 4
```
```elixir
add_one = Kata.add(1)
add_one.(3) # 4
```"""


def add(n: int):
    return lambda a: a + n
