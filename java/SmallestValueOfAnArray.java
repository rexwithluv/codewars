/* ID: 544a54fd18b8e06d240005c0

Write a function that can return the smallest value of an array or the index of that value. The function's 2nd parameter will tell whether it should return the value or the index.

Assume the first parameter will always be an array filled with at least 1 number and no duplicates. Assume the second parameter will be a string holding one of two values: 'value' and 'index'.

```javascript
min([1,2,3,4,5], 'value') // => 1
min([1,2,3,4,5], 'index') // => 0
```

```java
Arrays.findSmallest(new int[]{1,2,3,4,5}, 'value') // => 1
Arrays.findSmallest(new int[]{1,2,3,4,5}, 'index') // => 0
```

```C#
Kata.FindSmallest(new int[]{ 1, 2 , 3, 4, 5}, "value") // => 1
Kata.FindSmallest(new int[]{ 1, 2 , 3, 4, 5}, "index") // => 0
``` */
package kata;

public class SmallestValueOfAnArray {

    public static int findSmallest(final int[] numbers, final String toReturn) {
        int min = numbers[0];
        int index = 0;

        for (int i = 0; i < numbers.length; i++) {
            if (numbers[i] < min) {
                min = numbers[i];
                index = i;
            }
        }

        return toReturn.equals("index") ? index : min;
    }
}
