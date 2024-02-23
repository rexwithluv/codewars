/* ID: 5a55f04be6be383a50000187

# Definition 

A number is a **_Special Number_** *if it’s digits only consist 0, 1, 2, 3, 4
or 5*

**_Given_** a number *determine if it special number or not* .  



# Warm-up (Highly recommended)

# [Playing With Numbers Series]
(https://www.codewars.com/collections/playing-with-numbers)
___

# Notes 

* **_The number_** passed will be **_positive_** (N > 0) .

* All **single-digit numbers** within the interval **_[1:5]_** are considered as
**_special number_**. 
___

# Input >> Output Examples

```
specialNumber(2) ==> return "Special!!"
```
## Explanation: 

It's **_a single-digit number_** within the interval **_[1:5]_** . 

```
specialNumber(9) ==> return "NOT!!"
```
## Explanation:

Although, it's a single-digit number but **_Outside the interval [1:5]_** .

```
specialNumber(23) ==> return "Special!!"
```
## Explanation: 

All **_the number's digits_** formed from the interval **_[0:5]_** digits .

```
specialNumber(39) ==> return "NOT!!"
```
## Explanation: 

Although, *there is a digit (3) Within the interval* **_But_** **_the second
digit is not (Must be ALL The Number's Digits )_** .

```
specialNumber(59) ==> return "NOT!!"
```
## Explanation:  

Although, *there is a digit (5) Within the interval* **_But_** **_the second
digit is not (Must be ALL The Number's Digits )_** .

```
specialNumber(513) ==> return "Special!!"
```
___
```
specialNumber(709) ==> return "NOT!!"
```
___

# [For More Enjoyable Katas]
(http://www.codewars.com/users/MrZizoScream/authored)          

### ALL translation are welcomed

## Enjoy Learning !!
# Zizou */
package kata;

public class SpecialNumberSpecialNumbersSeriesNumber5 {

    private static boolean StringInIntArray(String str, int[] arr) {
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == Integer.parseInt(str)) {
                return true;
            }
        }
        return false;
    }

    public static String specialNumber(int number) {
        String numberString = String.valueOf(number);
        int[] specialArray = {0, 1, 2, 3, 4, 5};

        for (int i = 0; i < numberString.length(); i++) {

            if (!StringInIntArray(String.valueOf(numberString.charAt(i)), specialArray)) {
                return "NOT!!";
            }

        }

        return "Special!!";
    }
}
