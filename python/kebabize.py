""" ID: 57f8ff867a28db569e000c4a

Modify the `kebabize` function so that it converts a camel case string
into a kebab case.


```
"camelsHaveThreeHumps"  -->  "camels-have-three-humps"
"camelsHave3Humps"  -->  "camels-have-humps"
"CAMEL"  -->  "c-a-m-e-l"
```

Notes:
  - the returned string should only contain lowercase letters """


def kebabize(st: str) -> str:
    lst = []
    actual = ""

    for i in st:
        if i.isdigit():
            continue

        if not i.islower():
            lst.append(actual)
            actual = ""
        actual += i.lower()

    if len(actual) > 0:
        lst.append(actual)

    return "-".join(lst).strip("-")
