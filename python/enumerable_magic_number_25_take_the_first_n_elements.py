"""URL: https://www.codewars.com/kata/545afd0761aa4c3055001386

```if-not:swift
Create a function that accepts a list/array and a number **n**,
and returns a list/array of the first **n** elements from the list/array.

If
you need help, here's a reference:
```
```if:swift
Create a function *take* that
takes an `Array<Int>` and an `Int`, *n*, and returns an `Array<Int>` containing
the first up to *n* elements from the array.

If you need help, here's a
reference:
```
~~~if:javascript,coffeescript
https://developer.mozilla.org/en-
US/docs/Web/JavaScript/Reference/Global_Objects/Array/slice
~~~
~~~if:ruby
http://www.rubycuts.com/enum-take
~~~
~~~if:python
https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range
~~~
~~~if:java
https://docs.oracle.com/javase/6/docs/api/java/util/Arrays.html#c
opyOfRange(int[],%20int,%20int)
~~~
~~~if:swift
https://developer.apple.com/documentation/swift/array
~~~
~~~if:csharp
https://docs.microsoft.com/en-us/dotnet/api/system.array?view=netcore-3.1
~~~
~~~if:cobol
https://www.ibm.com/docs/en/cobol-zos/4.2?topic=program-handling-
tables
~~~
~~~if:scala
https://scala-lang.org/api/3.x/scala/collection/Seq.html
~~~
"""


def take(arr: list[int], n: int) -> list[int]:
    return arr[:n]
