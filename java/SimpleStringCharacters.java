/* ID: 5a29a0898f27f2d9c9000058

In this Kata, you will be given a string and your task will be to return a list
of ints detailing the count of uppercase letters, lowercase, numbers and special
characters, as follows.

```Haskell
Solve("*'&ABCDabcde12345") = [4,5,5,3]. 
--the order is: uppercase letters, lowercase, numbers and special characters.
```

More examples in the test cases. 

Good luck! */
package kata;

public class SimpleStringCharacters {

    public static int[] Solve(String word) {
        int upper = 0, lower = 0, nums = 0, special = 0;

        for (int i : word.toCharArray()) {
            if (Character.isUpperCase(i)) {
                upper++;
            } else if (Character.isLowerCase(i)) {
                lower++;
            } else if (Character.isDigit(i)) {
                nums++;
            } else {
                special++;
            }
        }
        int[] arr = {upper, lower, nums, special};
        return arr;
    }

}
