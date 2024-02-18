/* ID: 535474308bb336c9980006f2

Write a method that takes one argument as name and then greets that name, capitalized and ends with an exclamation point.

Example:

```
"riley" --> "Hello Riley!"
"JACK"  --> "Hello Jack!"
``` */
package kata;

public class GreetMe {

    private static String capitalice(String word) {
        String upper = word.substring(0, 1).toUpperCase();
        String lower = word.substring(1).toLowerCase();
        return upper + lower;
    }

    public static String greet(String name) {
        return "Hello " + capitalice(name) + "!";
    }
}
