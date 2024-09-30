/* ID: 541629460b198da04e000bb9

Find the last element of the given argument(s). If a single argument is passed and is a list/array or a string, return its last element. It is guaranteed that there will be at least one argument and that single-argument arrays/lists/strings will not be empty.

## Examples

~~~if:python,javascript,coffeescript,ruby
```python
last(5)               ==> 5
last([1, 2, 3, 4])    ==>  4
last("xyz")           ==> "z"
last(1, 2, 3, 4)      ==>  4
last([1, 2], [3, 4])  ==>  [3, 4]
last([[1, 2], [3, 4]])  ==>  [3, 4]
```
~~~

~~~if-not:python,javascript,coffeescript,ruby
```haskell
last [1, 2, 3, 4]     -- =>  4
last ['x', 'y', 'z']  -- => 'z'
```
```clojure
(last [1, 2, 3, 4]) ; => 4
(last "xyz")        ; => \z
```
```java
last(Arrays.asList(1, 2, 3, 4)); // =>  4
last("xyz");                     // => "z"
last(1, 2, 3, 4);                // =>  4
last(new int[]{1, 2, 3, 4});     // =>  4
```
```rust
last(&[1, 2, 3, 4])     // =>  4
last(&['x', 'y', 'z'])  // => 'z'
```
~~~

(courtesy of [haskell.org](http://www.haskell.org/haskellwiki/99_questions/1_to_10)) */
package kata;

public class Last {

    public static <T> T last(final List<T> list) {
        return null;
    }

    public static char last(final String string) {
        return 0;
    }

    public static <T> T last(final T... list) {
        return null;
    }
}
