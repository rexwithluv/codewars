/* URL: https://www.codewars.com/kata/559cc2d2b802a5c94700000c

Write a function that takes an array of **unique** integers and returns the minimum number of integers needed to make the values of the array consecutive from the lowest number to the highest number.


## Example

```
[4, 8, 6] --> 2
Because 5 and 7 need to be added to have [4, 5, 6, 7, 8]

[-1, -5] --> 3
Because -2, -3, -4 need to be added to have [-5, -4, -3, -2, -1]

[1] --> 0
[]  --> 0
```
*/

import java.util.Arrays;

public class HowManyConsecutiveNumbersAreNeeded {

    public static void main(String[] args) {
        System.out.println(consecutive(new int[] {}));
    }

    public static int consecutive(final int[] arr) {
        if (arr.length <= 1) {
            return 0;
        }

        int min = Arrays.stream(arr).min().orElse(0);
        int max = Arrays.stream(arr).max().orElse(0);

        return Math.max(max - min - (arr.length - 2) - 1, 0);
    }
}