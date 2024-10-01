/* ID: 564e7fc20f0b53eb02000106

Complete the function that takes a string of English-language text and returns the number of consonants in the string.

Consonants are all letters used to write English excluding the vowels `a, e, i, o, u`. */
package kata;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class CountConsonants {

    public static int getCount(String str) {
        Pattern pattern = Pattern.compile("[b-df-hj-np-tv-z]", Pattern.CASE_INSENSITIVE);
        Matcher matcher = pattern.matcher(str);
        int counter = 0;
        while (matcher.find()) {
            counter++;
        }
        return counter;
    }

}
