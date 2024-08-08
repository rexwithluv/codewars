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

function generateHashtag(str) {
  if (str.split(" ")[0] == "" || str.replaceAll(" ", "").length >= 140) {
    return false;
  } else {
    const capitalize = (string) => string[0].toUpperCase() + string.slice(1);
    return "#" + str.replace(/\s+/g, " ").split(" ").map(capitalize).join("");
  }
}

console.log(generateHashtag("code" + " ".repeat(140) + "wars"));
