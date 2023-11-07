""" Create a function called shortcut to remove the lowercase vowels (a, e, i, o, u ) in a given string.

Examples
"hello"     -->  "hll"
"codewars"  -->  "cdwrs"
"goodbye"   -->  "gdby"
"HELLO"     -->  "HELLO"

don't worry about uppercase vowels
y is not considered a vowel for this kata """

def shortcut(chain: str) -> str:
    vowels = ["a", "e", "i", "o", "u"]

    new_chain = ""
    for i in chain:
        if i not in vowels:
            new_chain += i
        
    return new_chain