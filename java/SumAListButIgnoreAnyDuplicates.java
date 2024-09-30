/* ID: 5993fb6c4f5d9f770c0000f2

Please write a function that sums a list, but ignores any duplicated items in the list.

For instance, for the list `[3, 4, 3, 6]` the function should return `10`,
and for the list `[1, 10, 3, 10, 10]` the function should return `4`.

~~~if:lambdacalc
### Encodings

purity: `LetRec`
numEncoding: `BinaryScott`

export constructors `nil, cons` for your `List` encoding
~~~ */
package kata;

import java.util.HashMap;

public class SumAListButIgnoreAnyDuplicates {

    public static int sumNoDuplicates(int[] arr) {
        HashMap<Integer, Integer> frequency = new HashMap<>();
        for (int number : arr) {
            if (frequency.containsKey(number)) {
                frequency.put(number, frequency.get(number) + 1);
            } else {
                frequency.put(number, 1);
            }
        }

        int sum = 0;
        for (int number : frequency.keySet()) {
            if (frequency.get(number) == 1) {
                sum += number;
            }
        }

        return sum;
    }
}
