/* ID: 534d2f5b5371ecf8d2000a08

Your task, is to create N×N multiplication table, of size provided in parameter.

For example, when given `size` is 3:
```
1 2 3
2 4 6
3 6 9
```

For the given example, the return value should be:

```js
[[1,2,3],[2,4,6],[3,6,9]]
```
```julia
[1 2 3; 2 4 6; 3 6 9]
```

```if:c
Note: in C, you must return an allocated table of allocated rows
``` */

const multiplicationTable = (size) => {
    let table = []
    for (let i = 1; i <= size; i++) {
        let row = []
        for (let j = 0; j < size; j++) {
            row.push(i +j);
        }
        table.push(row);
    }

    return table;
}

console.log(multiplicationTable(3));