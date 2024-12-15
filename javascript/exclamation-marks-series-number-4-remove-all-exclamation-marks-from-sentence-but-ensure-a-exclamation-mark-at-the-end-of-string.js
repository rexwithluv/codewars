/* ID: 57faf12b21c84b5ba30001b0

## Description:

Remove all exclamation marks from sentence but ensure a exclamation mark at the end of string. For a beginner kata, you can assume that the input data is always a non empty string, no need to verify it.

## Examples

```
"Hi!"     ---> "Hi!"
"Hi!!!"   ---> "Hi!"
"!Hi"     ---> "Hi!"
"!Hi!"    ---> "Hi!"
"Hi! Hi!" ---> "Hi Hi!"
"Hi"      ---> "Hi!"
``` */

function remove(string) {
    return string.replaceAll("!", "") + "!";
}

console.log(remove("Hi!!!!"))