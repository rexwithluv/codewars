/* ID: 59c5f4e9d751df43cf000035

The vowel substrings in the word `codewarriors` are `o,e,a,io`. The longest of these has a length of 2. Given a lowercase string that has alphabetic characters only (both vowels and consonants) and no spaces, return the length of the longest vowel substring.
Vowels are any of `aeiou`. 

Good luck!

If you like substring Katas, please try:

[Non-even substrings](https://www.codewars.com/kata/59da47fa27ee00a8b90000b4)

[Vowel-consonant lexicon](https://www.codewars.com/kata/59cf8bed1a68b75ffb000026) */
package kata;

import java.util.ArrayList;
import java.util.Collections;

public class LongestVowelChain {

    public static int solve(String s) {
        String[] arr = new String[s.length()];
        for (int i = 0; i < s.length(); i++) {
            arr[i] = String.valueOf(s.charAt(i));
        }

        String[] vowels = {"a", "e", "i", "o", "u"};
        ArrayList<Integer> longStrings = new ArrayList<>();
        int actual = 0;

        for (String i : arr) {

            for (String vowel : vowels) {

                if (i.equals(vowel)) {
                    actual++;
                    break;
                } else if (vowel.equals("u")) {
                    longStrings.add(actual);
                    actual = 0;
                }

            }

            if (actual > 0) {
                longStrings.add(actual);
            }
        }

        return Collections.max(longStrings);

    }
}
