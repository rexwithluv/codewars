"""ID: 5848565e273af816fb000449

## Acknowledgments:

I thank [yvonne-liu](https://www.codewars.com/users/yvonne-liu) for the idea and for the example tests :)

## Description:

Encrypt this!

You want to create secret messages which can be deciphered by the [Decipher this!](https://www.codewars.com/kata/decipher-this) kata. Here are the conditions:

1. Your message is a string containing space separated words.
2. You need to encrypt each word in the message using the following rules:
    * The first letter must be converted to its ASCII code.
    * The second letter must be switched with the last letter
3. Keepin' it simple: There are no special characters in the input.

## Examples:

```haskell
encryptThis "Hello" == "72olle"
encryptThis "good" == "103doo"
encryptThis "hello world" == "104olle 119drlo"
```
```python
encrypt_this("Hello") == "72olle"
encrypt_this("good") == "103doo"
encrypt_this("hello world") == "104olle 119drlo"
```
```ruby
encrypt_this("Hello") == "72olle"
encrypt_this("good") == "103doo"
encrypt_this("hello world") == "104olle 119drlo"
```
```groovy
Kata.encryptThis("Hello") == "72olle"
Kata.encryptThis("good") == "103doo"
Kata.encryptThis("hello world") == "104olle 119drlo"
```
```scala
Encrypt.encryptThis("Hello") == "72olle"
Encrypt.encryptThis("good") == "103doo"
Encrypt.encryptThis("hello world") == "104olle 119drlo"
```
```java
Kata.encryptThis("Hello") => "72olle"
Kata.encryptThis("good") => "103doo"
Kata.encryptThis("hello world") => "104olle 119drlo"
```
```javascript
encryptThis("Hello") === "72olle"
encryptThis("good") === "103doo"
encryptThis("hello world") === "104olle 119drlo"
```
```coffeescript
encryptThis("Hello") === "72olle"
encryptThis("good") === "103doo"
encryptThis("hello world") === "104olle 119drlo"
```
```c
encrypt_this("Hello") == "72olle"
encrypt_this("good") == "103doo"
encrypt_this("hello world") == "104olle 119drlo"
```
```cpp
encrypt_this("Hello") == "72olle"
encrypt_this("good") == "103doo"
encrypt_this("hello world") == "104olle 119drlo"
```
```go
EncryptThis("Hello") == "72olle"
EncryptThis("good") == "103doo"
EncryptThis("hello world") == "104olle 119drlo"
```
```csharp
Kata.EncryptThis("Hello") == "72olle"
Kata.EncryptThis("good") == "103doo"
Kata.EncryptThis("hello world") == "104olle 119drlo"
```
```vb
Kata.EncryptThis("Hello") = "72olle"
Kata.EncryptThis("good") = "103doo"
Kata.EncryptThis("hello world") = "104olle 119drlo"
```
```clojure
(= (encrypt-this "Hello") "72olle")
(= (encrypt-this "good" ) "103doo")
(= (encrypt-this "hello world") "104olle 119drlo")
```
```rust
encrypt_this("Hello") == "72olle"
encrypt_this("good") == "103doo"
encrypt_this("hello world") == "104olle 119drlo"
```
```lua
solution.encrypt_this("Hello") == "72olle"
solution.encrypt_this("good") == "103doo"
solution.encrypt_this("hello world") == "104olle 119drlo"
```
```php
encryptThis("Hello") === "72olle"
encryptThis("good") === "103doo"
encryptThis("hello world") === "104olle 119drlo"
```"""


def old_encrypt_this(text: str) -> str:
    if len(text) == 0:
        return text

    ascii_text = ord(text[0])

    # Revert second by last
    text = list(text[1:])
    second = text[0]
    text[0] = text[-1]
    text[-1] = second

    return str(ascii_text) + "".join(text)


def revert_second_last(word: str) -> str:
    if len(word) <= 1:
        return str(ord(word))

    first = ord(word[0])
    second = word[1]

    if len(word) == 2:
        return str(first) + word[2:-1] + second

    last = word[-1]
    return str(first) + last + word[2:-1] + second


def encrypt_this(text: str) -> str:
    if len(text) == 0:
        return text

    text = text.split()

    return " ".join(revert_second_last(word) for word in text)


print(encrypt_this("A wise old owl lived in an oak"))
