""" ```if-not:javascript
Find the sum of the odd numbers within an array, after cubing the
initial integers. The function should return
`undefined`/`None`/`nil`/`NULL` if any of the values aren't numbers.
```
```if:javascript
Find the sum of the odd numbers within an array, after cubing the
initial integers. The function should return `undefined` if any of the
values aren't numbers.
```

~~~if:java,csharp
Note: There are ONLY integers in the JAVA and C# versions of this Kata.
~~~

~~~if:python
Note: Booleans should not be considered as numbers.
~~~ """


def cube_odd(arr):
    x = 0
    for i in arr:
        if not isinstance(i, int) or isinstance(i, bool):
            return None
        if i % 2 == 1:
            x += i**3

    return x
