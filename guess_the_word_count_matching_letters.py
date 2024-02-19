""" ID: 5912ded3f9f87fd271000120

Consider a game, wherein the player has to guess a target word. All the
player knows is the length of the target word.

To help them in their goal, the game will accept guesses, and return the
number of letters that are in the correct position.

Write a method that, given the correct word and the player's guess,
returns this number.

For example, here's a possible thought process for someone trying to
guess the word "dog":

```cs
CountCorrectCharacters("dog", "car"); //0 (No letters are in the correct position)
CountCorrectCharacters("dog", "god"); //1 ("o")
CountCorrectCharacters("dog", "cog"); //2 ("o" and "g")
CountCorrectCharacters("dog", "cod"); //1 ("o")
CountCorrectCharacters("dog", "bog"); //2 ("o" and "g")
CountCorrectCharacters("dog", "dog"); //3 (Correct!)
```
```javascript
countCorrectCharacters("dog", "car"); //0 (No letters are in the correct position)
countCorrectCharacters("dog", "god"); //1 ("o")
countCorrectCharacters("dog", "cog"); //2 ("o" and "g")
countCorrectCharacters("dog", "cod"); //1 ("o")
countCorrectCharacters("dog", "bog"); //2 ("o" and "g")
countCorrectCharacters("dog", "dog"); //3 (Correct!)
```
```python
count_correct_characters("dog", "car"); #0 (No letters are in the correct position)
count_correct_characters("dog", "god"); #1 ("o")
count_correct_characters("dog", "cog"); #2 ("o" and "g")
count_correct_characters("dog", "cod"); #1 ("o")
count_correct_characters("dog", "bog"); #2 ("o" and "g")
count_correct_characters("dog", "dog"); #3 (Correct!)
```
```ruby
count_correct_characters("dog", "car"); #0 (No letters are in the correct position)
count_correct_characters("dog", "god"); #1 ("o")
count_correct_characters("dog", "cog"); #2 ("o" and "g")
count_correct_characters("dog", "cod"); #1 ("o")
count_correct_characters("dog", "bog"); #2 ("o" and "g")
count_correct_characters("dog", "dog"); #3 (Correct!)
```

The caller should ensure that the guessed word is always the same length
as the correct word, but since it could cause problems if this were not
the case, you need to check for this eventuality:

```cs
//Throw an InvalidOperationException if the two parameters are of different lengths.
```
```javascript
//Throw an error if the two parameters are of different lengths.
```
```python
#Raise an exception if the two parameters are of different lengths.
```
```ruby
#Raise an error if the two parameters are of different lengths.
```

You may assume, however, that the two parameters will always be in the
same case. """


def count_correct_characters(correct, guess) -> int:
    if len(correct) != len(guess):
        raise Exception

    return sum(1 for i, j in zip(correct, guess) if i == j)


print(count_correct_characters("len", "lenght"))
