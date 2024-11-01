/* ID: 583ade15666df5a64e000058

This kata is about converting numbers to their binary or hexadecimal representation:
* If a number is even, convert it to binary.
* If a number is odd, convert it to hex.

Numbers will be positive. The hexadecimal string should be lowercased. */

const evensAndOdds = num => num.toString(num % 2 == 0 ? 2 : 16);