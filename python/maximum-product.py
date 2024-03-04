""" ## Task

**_Given_** *an array of integers* , **_Find_** **_the maximum product_** *obtained from multiplying 2 adjacent numbers in the array*.
____

# Notes

* **_Array/list_** size is *at least 2*.

* **_Array/list_** numbers could be a *mixture of positives, negatives
  also zeroes* .
___

# Input >> Output Examples
```cpp
adjacentElementsProduct([1, 2, 3]); ==> return 6
```
```prolog
adjacent_elements_product([1, 2, 3], 6).
```

## **_Explanation_**:

* **_The maximum product_** *obtained from multiplying* ` 2 * 3 = 6 `,
  and **_they're adjacent numbers in the array_**.
___
```cpp
adjacentElementsProduct([9, 5, 10, 2, 24, -1, -48]); ==> return 50
```
```prolog
adjacent_elements_product([9, 5, 10, 2, 24, -1, -48], 50).
```
## **_Explanation_**:
**_Max product_** obtained *from multiplying*   ``` 5 * 10  =  50  ```.
___
```cpp
adjacentElementsProduct([-23, 4, -5, 99, -27, 329, -2, 7, -921])  ==>  return -14
```
```prolog
adjacent_elements_product([-23, 4, -5, 99, -27, 329, -2, 7, -921], -14).
```

## **_Explanation_**:

* **_The maximum product_** *obtained from multiplying* ` -2 * 7 = -14
  `, and **_they're adjacent numbers in the array_**.
___
___
___

# [Playing with Numbers
Series](https://www.codewars.com/collections/playing-with-numbers)

# [Playing With Lists/Arrays
Series](https://www.codewars.com/collections/playing-with-lists-slash-arrays)

# [For More Enjoyable
Katas](http://www.codewars.com/users/MrZizoScream/authored)
___

## ALL translations are welcomed

## Enjoy Learning !!
# Zizou """


def adjacent_element_product(array):
    products = []
    for i in range(len(array)):
        try:
            products.append(array[i] * array[i + 1])
        except IndexError:
            return max(products)

    return 0


print(adjacent_element_product([5, 1, 2, 3, 1, 4]))
