/* ID: 5831c204a31721e2ae000294

When provided with a String, capitalize all vowels

For example:

Input : "Hello World!"

Output : "HEllO WOrld!"

Note: Y is not a vowel in this kata. */


const swap = (string) => {
    return string.split("").map((letter) => {
        return ["a", "e", "i", "o", "u"].includes(letter) ? letter.toUpperCase() : letter;
    }).join("");
}