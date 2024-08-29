/* ID: 558f9f51e85b46e9fa000025

*Recreation of [Project Euler problem #6](https://projecteuler.net/problem=6)*

Find the difference between the square of the sum of the first `n` natural numbers `(1 <= n <= 100)` and the sum of their squares.

## Example
For example, when `n = 10`:

* The square of the sum of the numbers is:

      (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10)² = 55² = 3025


* The sum of the squares of the numbers is:

      1² + 2² + 3² + 4² + 5² + 6² + 7² + 8² + 9² + 10² = 385

Hence the difference between square of the sum of the first ten natural numbers and the sum of the squares of those numbers is: `3025 - 385 = 2640` */

function differenceOfSquares(n) {
  let squareSum = 1;
  for (let i = 2; i <= n; i++) {
    squareSum += i;
  }

  let sumSquare = 1;
  for (let i = 2; i <= n; i++) {
    sumSquare += Math.pow(i, 2);
  }

  return Math.pow(squareSum, 2) - sumSquare;
}

console.log(differenceOfSquares(10));
