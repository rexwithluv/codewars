/* URL: https://www.codewars.com/kata/5a0d38c9697598b67a000041

# Task

You are given a string representing a number in binary. Your task is to delete all the **unset** bits in this string and return the corresponding number (after keeping only the '1's).

In practice, you should implement this function:

~~~if:nasm
```c
unsigned long eliminate_unset_bits(const char* number);
```
~~~
~~~if-not:nasm
```c
long eliminate_unset_bits(const char* number);
```
```python
def eliminate_unset_bits(number):
```
```javascript
function eliminateUnsetBits(number);
```
```coffeescript
eliminateUnsetBits = (number) ->
```
```haskell
eliminateUnsetBits :: String -> Integer
```
```ruby
def eliminate_set_bits number
```
```crystal
def eliminate_set_bits(number)
```
```java
public long eliminateUnsetBits(String number);
```
```cpp
long eliminate_unset_bits(string number);
```
```scala
def eliminateUnsetBits(number: String): Long
```
~~~

## Examples

~~~if:java,ruby,javascript,coffeescript,crystal,haskell,scala
```java
eliminateUnsetBits("11010101010101") ->  255 (= 11111111)
eliminateUnsetBits("111") ->  7
eliminateUnsetBits("1000000") -> 1
eliminateUnsetBits("000") -> 0
```
```ruby
eliminate_set_bits("11010101010101") ->  255 (= 11111111)
eliminate_set_bits("111") ->  7
eliminate_set_bits("1000000") -> 1
eliminate_set_bits("000") -> 0
```
```crystal
eliminate_set_bits("11010101010101") ->  255 (= 11111111)
eliminate_set_bits("111") ->  7
eliminate_set_bits("1000000") -> 1
eliminate_set_bits("000") -> 0
```
```javascript
eliminateUnsetBits("11010101010101") ->  255 (= 11111111)
eliminateUnsetBits("111") ->  7
eliminateUnsetBits("1000000") -> 1
eliminateUnsetBits("000") -> 0
```
```coffeescript
eliminateUnsetBits("11010101010101") ->  255 (= 11111111)
eliminateUnsetBits("111") ->  7
eliminateUnsetBits("1000000") -> 1
eliminateUnsetBits("000") -> 0
```
```haskell
eliminateUnsetBits "11010101010101" ->  255 (= 11111111)
eliminateUnsetBits "111" ->  7
eliminateUnsetBits "1000000" -> 1
eliminateUnsetBits "000" -> 0
```
```scala
eliminateUnsetBits("11010101010101") ->  255 (= 11111111)
eliminateUnsetBits("111") ->  7
eliminateUnsetBits("1000000") -> 1
eliminateUnsetBits("000") -> 0
```
~~~
~~~if-not:java,ruby,javascript,crystal,coffeescript,haskell
```c
eliminate_unset_bits("11010101010101") ->  255 (= 11111111)
eliminate_unset_bits("111") ->  7
eliminate_unset_bits("1000000") -> 1
eliminate_unset_bits("000") -> 0
```
~~~
*/

public class EliminateTheIntrudersBitManipulation {
    public static long eliminateUnsetBits(String number) {
        final String onlyBits = number.replace("0", "");
        return onlyBits.length() != 0 ? Long.parseLong(onlyBits, 2) : 0L;
    }
}