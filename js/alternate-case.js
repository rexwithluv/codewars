/* ID: 57a62154cf1fa5b25200031e

Write function alternateCase which switch every letter in string from upper to lower and from lower to upper.
E.g: Hello World -> hELLO wORLD */

function alternateCase(s) {
  let newString = "";
  for (let i = 0; i < s.length; i++) {
    if (s[i] === s[i].toUpperCase()) {
      newString += s[i].toLowerCase();
    } else {
      newString += s[i].toUpperCase();
    }
  }

  return newString;
}
