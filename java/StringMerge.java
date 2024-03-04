/* ID: 597bb84522bc93b71e00007e

Given two words and a letter, return a single word that's a combination of both words, merged at the point where the given letter first appears in each word. The returned word should have the beginning of the first word and the ending of the second, with the dividing letter in the middle. You can assume both words will contain the dividing letter.

## Examples

```python
("hello", "world", "l")       ==>  "held"
("coding", "anywhere", "n")   ==>  "codinywhere"
("jason", "samson", "s")      ==>  "jasamson"
("wonderful", "people", "e")  ==>  "wondeople"
``` */
package kata;

public class StringMerge {

    public static String stringMerge(String s1, String s2, char letter) {
        String merge = "";

        for (int i = 0; i < s1.length(); i++) {

            if (s1.charAt(i) == letter) {
                merge += s1.substring(0, i);
                break;
            }

        }

        for (int i = 0; i < s2.length(); i++) {

            if (s2.charAt(i) == letter) {
                merge += s2.substring(i);
                break;
            }

        }

        return merge;
    }
}
