/* ID: 52449b062fb80683ec000024

The marketing team is spending way too much time typing in hashtags.
Let's help them with our own Hashtag Generator!

Here's the deal:

- It must start with a hashtag (`#`).
- All words must have their first letter capitalized.
- If the final result is longer than 140 chars it must return `false`.
- If the input or the result is an empty string it must return `false`.


## Examples

```
" Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
"    Hello     World   "                  =>  "#HelloWorld"
""                                        =>  false
``` */

"use strict";


function generateHashtag(str) {
    if (str.trim().length === 0) return false;

    const capitalize = (string) => string.charAt(0).toUpperCase() + string.slice(1).toLowerCase();
    let result = "#" + str.split(" ").map(word => capitalize(word)).join("");

    return result.length > 140 ? false : result;
}

