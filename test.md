# Test en los diferentes lenguajes

## En JS

```js
function hello(name) {
    return `Hello ${name}!`;
}

const assert = require('assert');
try {
    assert.strictEqual(hello("RexWithLuv"), "Hello RexWithLuv!");
    assert.strictEqual(hello("Anonymous"), "Hello Anonymous!");
    assert.strictEqual(hello("Linus"), "Hello Linus!");
    assert.strictEqual(hello("you"), "Hello you!");

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
    assert hello("RexWithLuv") == "Hello RexWithLuv!"
    assert hello("Anonymous") == "Hello Anonymous!"
    assert hello("Linus") == "Hello Linus!"
    assert hello("you") == "Hello you!"

    print("Todos los tests pasaron correctamente")
except AssertionError as error:
    print(f"Ha fallado el test: {error}")
```
