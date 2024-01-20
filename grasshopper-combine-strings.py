""" ### Combine strings function
```if:coffeescript,haskell,javascript
Create a function named `combineNames` that accepts two parameters
(first and last name). The function should return the full name.
```
```if:python,ruby
Create a function named (`combine_names`) that accepts two parameters
(first and last name). The function should return the full name.
```
```if:csharp
Create a function named (`Combine_names`) that accepts two parameters
(first and last name). The function should return the full name.
```

Example:
```javascript
combineNames('James', 'Stevens')
```
```coffeescript
combineNames 'James', 'Stevens'
```
```python
combine_names('James', 'Stevens')
```
```ruby
combine_names('James', 'Stevens')
```
```haskell
combineNames "James"  "Stevens"
```
```csharp
CombineNames("James", "Stevens")
```
returns:
```javascript
'James Stevens'
```
```coffeescript
'James Stevens'
```
```python
'James Stevens'
```
```ruby
'James Stevens'
```
```haskell
"James Stevens"
```
```csharp
"James Stevens"
``` """


def combine_names(n1, n2):
    return n1 + " " + n2
