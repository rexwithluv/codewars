/* ID: 593b1909e68ff627c9000186

Nickname Generator

Write a function, `nicknameGenerator` that takes a string name as an argument and returns the first 3 or 4 letters as a nickname.

If the 3rd letter is a consonant, return the first 3 letters.

```javascript
nickname("Robert") //=> "Rob"
nickname("Kimberly") //=> "Kim"
nickname("Samantha") //=> "Sam"
```

If the 3rd letter is a vowel, return the first 4 letters.

```javascript
nickname("Jeannie") //=> "Jean"
nickname("Douglas") //=> "Doug"
nickname("Gregory") //=> "Greg"
```

If the string is less than 4 characters, return "Error: Name too short".

**Notes:**

- Vowels are "aeiou", so discount the letter "y".
- Input will always be a string.
- Input will always have the first letter capitalised and the rest lowercase (e.g. Sam).
- The input can be modified*/

"use strict";

function nicknameGenerator(name) {
  if (name.length <= 3) {
    return "Error: Name too short";
  }
  return name.slice(0, /[aeiou]/.test(name.charAt(2)) ? 4 : 3);
}
