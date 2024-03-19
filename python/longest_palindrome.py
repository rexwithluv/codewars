"""ID: 54bb6f887e5a80180900046b

### Longest Palindrome

Find the length of the longest substring in the given string `s` that is
the same in reverse.

As an example, if the input was “I like racecars that go fast”, the
substring (`racecar`) length would be `7`.

If the length of the input string is `0`, the return value must be `0`.

### Example:
```
"a" -> 1
"aab" -> 2
"abcde" -> 1
"zzbaabcd" -> 4
"" -> 0
```"""


def longest_palindrome(s: str) -> int:
    palindromes = [""]
    for i in range(len(s)):
        for j in range(len(s) + 1):
            if s[i:j] == s[i:j][::-1] and s[i:j] not in palindromes:
                palindromes.append(s[i:j])

    return len(max(palindromes, key=len))
