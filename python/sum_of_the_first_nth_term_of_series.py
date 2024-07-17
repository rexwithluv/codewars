""" ID: 555eded1ad94b00403000071

## Task:

Your task is to write a function which returns the sum of following
series upto nth term(parameter).

    Series: 1 + 1/4 + 1/7 + 1/10 + 1/13 + 1/16 +...

## Rules:

* You need to round the answer to 2 decimal places and return it as
  String.

* If the given value is 0 then it should return 0.00

* You will only be given Natural Numbers as arguments.

## Examples:(Input --> Output)

    1 --> 1 --> "1.00"
    2 --> 1 + 1/4 --> "1.25"
    5 --> 1 + 1/4 + 1/7 + 1/10 + 1/13 --> "1.57" """


def series_sum(n: int) -> str:
    if n == 0:
        return "0.00"

    denominator = 1
    total = 0
    for _ in range(n):
        total += 1 / denominator
        denominator += 3

    result = str(round(total, 2))
    if len(result) < 4:
        result += "0"

    return result
