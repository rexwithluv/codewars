"""ID: 539de388a540db7fec000642

# Story

Your online store likes to give out coupons for special occasions. Some customers try to cheat the system by entering invalid codes or using expired coupons.

# Task

Your mission:
Write a function called `checkCoupon` which verifies that a coupon code is valid and not expired.

A coupon is no more valid on the day **AFTER** the expiration date.  All dates will be passed as strings in this format: `"MONTH DATE, YEAR"`.

## Examples:

```javascript
checkCoupon("123", "123", "July 9, 2015", "July 9, 2015")  ===  true
checkCoupon("123", "123", "July 9, 2015", "July 2, 2015")  ===  false
```
```typescript
checkCoupon("123", "123", "July 9, 2015", "July 9, 2015")  ===  true
checkCoupon("123", "123", "July 9, 2015", "July 2, 2015")  ===  false
```
```csharp
CheckCoupon("123", "123", "July 9, 2015", "July 9, 2015")  ==  true
CheckCoupon("123", "123", "July 9, 2015", "July 2, 2015")  ==  false
```
```python
checkCoupon("123", "123", "July 9, 2015", "July 9, 2015")  == True
checkCoupon("123", "123", "July 9, 2015", "July 2, 2015")  == False
```"""


def check_coupon(entered_code, correct_code, current_date, expiration_date) -> bool:
    if entered_code is not correct_code:
        return False

    current_date = current_date.replace(",", "").lower().split()
    expiration_date = expiration_date.replace(",", "").lower().split()

    months = {
        "january": 1,
        "february": 2,
        "march": 3,
        "april": 4,
        "may": 5,
        "june": 6,
        "july": 7,
        "august": 8,
        "september": 9,
        "october": 10,
        "november": 11,
        "december": 12,
    }

    current_day = int(current_date[1])
    current_month = months[current_date[0]]
    current_year = int(current_date[2])
    expiration_day = int(expiration_date[1])
    expiration_month = months[expiration_date[0]]
    expiration_year = int(expiration_date[2])

    if current_year > expiration_year:
        return False

    if current_year == expiration_year and current_month > expiration_month:
        return False

    if (
        current_year == expiration_year
        and current_month == expiration_month
        and current_day > expiration_day
    ):
        return False

    return True
