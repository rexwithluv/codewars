/* ID: 55a5befdf16499bffb00007b

Make multiple functions that will return the sum, difference, modulus, product, quotient, and the exponent respectively.

Please use the following function names:

```if-not:csharp
addition = **add**

multiply = **multiply**

division = **divide** (both integer and float divisions are accepted)

modulus = **mod**

exponential = **exponent**

subtraction = **subt**
```

```if:csharp
addition = **Add**

multiply = **Multiply**

division = **Divide**

modulus = **Mod**

exponential = **Exponent**

subtraction = **Subt**

**Note: All funcitons can return int and all will recieve 2 integers.**
```


*Note: All math operations will be:
  a (operation) b* */

function add(a, b) {
  return a + b;
}

function divide(a, b) {
  return a / b;
}

function multiply(a, b) {
  return a * b;
}

function mod(a, b) {
  return a % b;
}

function exponent(a, b) {
  return Math.pow(a, b);
}

function subt(a, b) {
  return a - b;
}