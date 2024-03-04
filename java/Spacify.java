/* ID: 57f8ee485cae443c4d000127

Modify the spacify function so that it returns the given string with spaces
inserted between each character.

```coffeescript
spacify=("hello world") -> # returns "h e l l o   w o r l d
```
```crystal
spacify("hello world") # returns "h e l l o   w o r l d"
```
```haskell
spacify "hello world" -- returns "h e l l o   w o r l d"
```
```java
spacify("hello world") // returns "h e l l o   w o r l d"
```
```javascript
spacify("hello world") // returns "h e l l o   w o r l d"
```
```python
spacify("hello world") # returns "h e l l o   w o r l d"
```
```ruby
spacify("hello world") # returns "h e l l o   w o r l d"
```
```c
spacify("hello world") // returns "h e l l o   w o r l d"
```
```php
spacify("hello world") // "h e l l o   w o r l d"
```
```swift
spacify("hello world") // "h e l l o   w o r l d"
``` */
package kata;

public class Spacify {

    public static String spacify(String str) {
        String newStr = "";

        for (char i : str.toCharArray()) {
            newStr += i + " ";
        }
        return newStr.substring(0, newStr.length() - 1);
    }
}
