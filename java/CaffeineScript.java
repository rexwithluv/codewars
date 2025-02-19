/* URL: https://www.codewars.com/kata/5434283682b0fdb0420000e6

Complete the function which takes a non-zero integer as its argument.

If the integer is divisible by 3, return the string `"Java"`.

If the integer is divisible by 3 and divisible by 4, return the string `"Coffee"`

If one of the condition above is true and the integer is even, add `"Script"` to the end of the string.

If none of the condition is true, return the string `"mocha_missing!"`


## Examples

```python
1   -->  "mocha_missing!"
3   -->  "Java"
6   -->  "JavaScript"
12  -->  "CoffeeScript"
```
*/

public class CaffeineScript {
    public static String caffeineBuzz(int n) {
        String string = "";

        boolean byThree = n % 3 == 0;
        boolean byFour = n % 4 == 0;

        if (byThree && byFour) {
            string += "Coffee";
        } else if (byThree) {
            string += "Java";
        }

        if (!string.equals("") && n % 2 == 0) {
            string += "Script";
        }

        return !string.equals("") ? string : "mocha_missing!";
    }
}