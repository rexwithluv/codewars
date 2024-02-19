/* ID: 585b1fafe08bae9988000314

Given a string made of digits `[0-9]`, return a string where each digit is repeated a number of times equals to its value. 

## Examples

```haskell
"312" should return "333122"
```

```haskell
"102269" should return "12222666666999999999"
``` */
package kata;

public class DigitsExplosion {

    public static String explode(String digits) {
        String explosion = "";

        for (int i = 0; i < digits.length(); i++) {
            String actual = String.valueOf(digits.charAt(i));

            for (int j = 0; j < Integer.parseInt(actual); j++) {
                explosion += actual;
            }

        }

        return explosion;
    }

}
