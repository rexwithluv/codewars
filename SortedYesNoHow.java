/* ID: 580a4734d6df748060000045

Complete the method which accepts an array of integers, and returns one of the following:

* `"yes, ascending"` - if the numbers in the array are sorted in an ascending order
* `"yes, descending"` - if the numbers in the array are sorted in a descending order
* `"no"` - otherwise


You can assume the array will always be valid, and there will always be one correct answer. */
package kata;

import java.util.Arrays;
import java.util.Collections;

public class SortedYesNoHow {

    public static String isSortedAndHow(int[] array) {
        Integer[] arr = new Integer[array.length];
        for (int i = 0; i < array.length; i++) {
            arr[i] = array[i];
        }

        Integer[] asc = new Integer[array.length];
        for (int i = 0; i < array.length; i++) {
            asc[i] = array[i];
        }
        Arrays.sort(asc);

        Integer[] desc = new Integer[array.length];
        for (int i = 0; i < array.length; i++) {
            desc[i] = array[i];
        }
        Arrays.sort(desc, Collections.reverseOrder());

        if (Arrays.equals(arr, asc)) {
            return "yes, ascending";
        } else if (Arrays.equals(arr, desc)) {
            return "yes, descending";
        } else {
            return "no";
        }

    }
}
