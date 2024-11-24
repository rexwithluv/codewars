/* ID: 55960bbb182094bc4800007b

Write a function that takes an integer `num` (`num >= 0`) and inserts dashes (`'-'`) between each two **odd** digits in `num`.

## Examples

```python
454793 ---> "4547-9-3"
     0 ---> "0"
     1 ---> "1"
13579  ---> "1-3-5-7-9"
 86420 ---> "86420"
``` */

"use strict";


const insertDash = (numbers) => {
     const isOdd = num => num % 2 == 1;

     let newString = "0";
     Array.from(numbers.toString()).forEach(num => {
          if (isOdd(parseInt(num)) && isOdd(parseInt(newString.charAt(newString.length - 1)))) {
               newString += "-" + num
          } else {
               newString += num
          }
     });

     return newString.slice(1);
}
