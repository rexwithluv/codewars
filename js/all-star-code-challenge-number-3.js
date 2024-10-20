/* ID: 58640340b3a675d9a70000b9

**This Kata is intended as a small challenge for my students**

Create a function that takes a string argument and returns that same string with all vowels removed (vowels are "a", "e", "i", "o", "u").

Example (**Input** --> **Output**)
```
"drake" --> "drk"
"aeiou" --> ""
```

```cpp
remove_vowels("drake") // => "drk"
remove_vowels("aeiou") // => ""
``` */

const removeVowels = (str) => {
    const regex = /[aeiou]/gi
    return str.replaceAll(regex, "");
};

console.log(removeVowels("aeiuasdof"));