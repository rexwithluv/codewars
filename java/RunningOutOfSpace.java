/* ID: 56576f82ab83ee8268000059

Kevin is noticing his space run out! Write a function that removes the spaces from the values and returns an array showing the space decreasing.
For example, running this function on the array `['i', 'have','no','space']` would produce `['i','ihave','ihaveno','ihavenospace']` */
package kata;

public class RunningOutOfSpace {

    public static String[] spacey(String[] array) {
        String[] result = new String[array.length];
        String phrase = "";
        for (int i = 0; i < array.length; i++) {
            phrase += array[i];
            result[i] = phrase;
        }

        return result;
    }
}
