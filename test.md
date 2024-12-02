# Test en los diferentes lenguajes

## En JS

```js
function hello(name) {
    return `Hello ${name}!`;
}

const assert = require('assert');
try {
    assert.strictEqual(hello("RexWithLuv"), "Hello RexWithLuv!");

    console.log("Todos los tests pasaron correctamente.");
} catch (error) {
    console.error("Test fallido:", error.message);
}
```

## En Python

```py
def hello(name):
    return f"Hello {name}!"

try:
    test_cases = [
        ("RexWithLuv","Hello RexWithLuv!")
    ]

    for param, expected in test_cases:
        result = hello(param)
        assert result == expected, f"El test ha fallado con el parámetro {param}: se esperaba {expected}, obtenido {result}"

    print("Todos los tests pasaron correctamente")
except AssertionError as error:
    print(error)
```
