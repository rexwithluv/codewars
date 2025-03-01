
import java.util.Arrays;

/* URL: https://www.codewars.com/kata/5356ad2cbb858025d800111d

Create a function that accepts an array of names, and returns an array of each name with its first letter capitalized and the remainder in lowercase.

### Examples
```ruby
['jo', 'nelson', 'jurie'] -->  ['Jo', 'Nelson', 'Jurie']
['KARLY', 'DANIEL', 'KELSEY'] --> ['Karly', 'Daniel', 'Kelsey']
```
*/

public class NameArrayCapping {
    public static String[] capMe(String[] strings) {
        return Arrays.stream(strings).map((str) -> {
            return str.length() != 0 ? str.substring(0, 1).toUpperCase() + str.substring(1).toLowerCase() : str;
        }).toArray(String[]::new);
    }
}