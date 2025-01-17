/* URL: https://www.codewars.com/kata/545993ee52756d98ca0010e1

Write a function that takes two arguments: an array and a callback function (in Ruby: a block).

The function should return `true` if the callback / block returns `false` for **all** of the items in the array, or if the array is empty; otherwise return `false`.
*/

"use strict";

function none(arr, fun) {
    let response = true;
    arr.forEach(num => {
        if (fun(num) === true) {
            response = false;
        }
    });
    return response;
}
