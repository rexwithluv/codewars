

/* URL: https://www.codewars.com/kata/5a995c2aba1bb57f660001fd

Let's create some scrolling text!

Your task is to complete the function which takes a string, and returns an array with all possible rotations of the given string, **in uppercase**.


## Example

`scrollingText("codewars")` should return:
```javascript
[ "CODEWARS",
  "ODEWARSC",
  "DEWARSCO",
  "EWARSCOD",
  "WARSCODE",
  "ARSCODEW"
  "RSCODEWA",
  "SCODEWAR" ]
```

Good luck!
 */
public class ScrollingText {

    public static String[] scrollingText(String text) {
        String[] rotations = new String[text.length()];

        for (int i = 0; i < text.length(); i++) {
            String actualRotation = text.substring(i) + text.substring(0, i);
            rotations[i] = actualRotation.toUpperCase();
        }

        return rotations;
    }
}
