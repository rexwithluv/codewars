/* ID: 57aa218e72292d98d500240f

Write function heron which calculates the area of a triangle with sides a, b, and c (x, y, z in COBOL).

Heron's formula:
```math
\sqrt{s * (s - a) * (s - b) * (s - c)}
```
where
```math
s = \frac{a + b + c} 2
```
Output should have 2 digits precision. */
package kata;

public class HeronsFormula1 {

    public static double heron(double a, double b, double c) {
        double s = (a + b + c) / 2;
        return Math.sqrt(s * (s - a) * (s - b) * (s - c));
    }
}
