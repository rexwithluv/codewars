/* ID: 5748838ce2fab90b86001b1a

Complete the function that calculates the area of the red square, when the length of the circular arc `A` is given as the input. Return the result rounded to two decimals.

![Graph](http://i.imgur.com/nJrae8n.png)

Note: use the π value provided in your language (`Math::PI`, `M_PI`, `math.pi`, etc) */

const squareArea = (A) => ((A * 2) / Math.PI) ** 2;