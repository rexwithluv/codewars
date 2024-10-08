/* ID: 56582133c932d8239900002e

Complete the function to find the count of the most frequent item of an array. You can assume that input is an array of integers. For an empty array return `0`


## Example
```python
input array: [3, -1, -1, -1, 2, 3, -1, 3, -1, 2, 4, 9, 3]
ouptut: 5
```
The most frequent number in the array is `-1` and it occurs `5` times. */
package kata;

import java.util.HashMap;

public class FindCountOfMostFrequentItemInAnArray {

    public static int mostFrequentItemCount(int[] collection) {
        HashMap<Integer, Integer> frequency = new HashMap<>();

        for (int i : collection) {
            if (frequency.containsKey(i)) {
                frequency.put(i, frequency.get(i) + 1);
            } else {
                frequency.put(i, 1);
            }
        }

        int max = 0;
        for (int i : frequency.values()) {
            max = Math.max(max, i);
        }

        return max;
    }
}
