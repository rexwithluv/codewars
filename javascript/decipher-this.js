/* ID: 581e014b55f2c52bb00000f8

You are given a secret message you need to decipher. Here are the things you need to know to decipher it:

For each word:
- the second and the last letter is switched (e.g. `Hello` becomes `Holle`)
- the first letter is replaced by its character code (e.g. `H` becomes `72`)

* there are no special characters used, only letters and spaces
* words are separated by a single space
* there are no leading or trailing spaces

Examples
```
'72olle 103doo 100ya' --> 'Hello good day'
'82yade 115te 103o'   --> 'Ready set go'
``` */

"use strict";

function changeOneAndLast(word) {
    let array = [...word];
    if (array.length <= 3) {
        return array.reverse().join("");
    }

    array.push(array[0]);
    array[0] = array[array.length - 2];
    array.splice(array.length - 2, 1);

    return array.join("");
}

function decipherThis(str) {
    return str.split(" ").map(word => {
        const num = word.match(/^\d+/)[0];
        const letters = word.match(/[A-Za-z]*$/)[0];

        return String.fromCharCode(num) + changeOneAndLast(letters);
    }).join(" ");
}

