/* ID: 54557d61126a00423b000a45

Given 2 strings, `a` and `b`, return a string of the form: `shorter+reverse(longer)+shorter.`


In other words, the shortest string has to be put as prefix and as suffix of the reverse of the longest.

Strings `a` and `b` may be empty, but not null (In C# strings may also be null. Treat them as if they are empty.).  
If `a` and `b` have the same length treat `a` as the longer producing `b+reverse(a)+b` */
package kata;

public class ShorterConcatReverseLonger {

    private static String reverse(String str) {
        String reverseString = "";

        for (int i = str.length() -1; i >= 0; i--) {
            reverseString += str.charAt(i);
        }

        return reverseString;
    }

    public static String shorterReverseLonger(String a, String b) {
        String longer;
        String shorter;
        if (b.length() > a.length()) {
            longer = reverse(b);
            shorter = a;
        } else {
            longer = reverse(a);
            shorter = b;
        }

        return shorter + longer + shorter;

    }
}
