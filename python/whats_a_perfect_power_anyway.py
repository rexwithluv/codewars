"""URL: https://www.codewars.com/kata/54d4c8b08776e4ad92000835

A [perfect power](https://en.wikipedia.org/wiki/Perfect_power) is a
classification of positive integers:

> In mathematics, a **perfect power** is a
positive integer that can be expressed as an integer power of another positive
integer. More formally, n is a perfect power if there exist natural numbers m >
1, and k > 1 such that m<sup>k</sup> = n.

Your task is to check wheter a given
integer is a perfect power. If it is a perfect power, return a pair `m` and `k`
with m<sup>k</sup> = n as a proof. Otherwise return `Nothing`, `Nil`, `null`,
`NULL`, `None` or your language's equivalent.

**Note:** For a perfect power,
there might be several pairs. For example `81 = 3^4 = 9^2`, so `(3,4)` and
`(9,2)` are valid solutions. However, the tests take care of this, so if a
number is a perfect power, return any pair that proves it.

### Examples
```javascript
describe("perfect powers", function(){
  it("should work for some
examples",function(){
    assert.deepEqual(isPP(4), [2,2], "4 = 2^2");
assert.deepEqual(isPP(9), [3,2], "9 = 3^2");
    assert.strictEqual(isPP(5),
null, "5 isn't a perfect number");
  });
});
```
```coffeescript
Test.describe
"perfect powers", ->
  Test.it "should work for some examples", ->
Test.assertSimilar isPP(4), [ 2, 2 ], "4 = 2^2"
    Test.assertSimilar isPP(9),
[ 3, 2 ], "9 = 3^2"
    Test.assertEquals isPP(5), null, "5 isn't a perfect
number"
```
```haskell
isPP 4 `shouldBe` Just (2,2)
isPP 9 `shouldBe` Just (3,2)
isPP 5 `shouldBe` Nothing
```
```python
isPP(4) => [2,2]
isPP(9) => [3,2]
isPP(5) => None
```
```ruby
isPP(4) => [2,2]
isPP(9) => [3,2]
isPP(5) => nil
```
```java
isPerfectPower(4) => new int[]{2,2}
isPerfectPower(5) => null
isPerfectPower(8) => new int[]{2,3}
isPerfectPower(9) => new int[]{3,2}
```
```r
isPP(4) => 2 2
isPP(9) => 3 2
isPP(5) => NULL
```
```csharp
IsPerfectPower(4) =>
(2,2)
IsPerfectPower(5) => null
IsPerfectPower(8) => (2,3)
IsPerfectPower(9) =>
(3,2)
```
"""

from typing import List


def isPP(n: int) -> List[int] | None:
    for base in range(2, int(n**0.5) + 1):
        pow = 2
        while (pot := base**pow) <= n:
            if pot == n:
                return [base, pow]
            pow += 1
    return None
