/* ID: 593c9175933500f33400003e

Implement a function, `multiples(m, n)`, which returns an array of the first `m`
multiples of the real number `n`. Assume that `m` is a positive integer.

Ex.
```
multiples(3, 5.0)
```
should return
```
[5.0, 10.0, 15.0]
``` */
package kata;

public class ReturnTheFirstMMultiplesOfN {

    public static int[] multiples(int m, int n) {
        int[] mult = new int[m];

        for (int i = 1; i <= m; i++) {
            mult[i - 1] = i * n;
        }

        return mult;
    }
}
