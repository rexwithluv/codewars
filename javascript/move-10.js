/* ID: 57cf50a7eca2603de0000090

Move every letter in the provided string forward 10 letters through the alphabet.

If it goes past 'z', start again at 'a'.

Input will be a string with length > 0.*/

"use strict";


function moveTen(s) {
    const abc = "abcdefghijklmnopqrstuvwxyz";
    return [...s].map(l => abc.charAt((abc.indexOf(l) + 10) % abc.length)).join("");
}