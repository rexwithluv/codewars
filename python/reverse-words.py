""" Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.

Examples
"This is an example!" ==> "sihT si na !elpmaxe"
"double  spaces"      ==> "elbuod  secaps" """

""" def reverse_words(text):
    new_text = ""
    new_list = text.split()
    for i in new_list:
        new_text += i[::-1] + " "
        
        if i == new_list[(len(new_list) - 1)]:
            return new_text[:-1] """

def reverse_words(text: str) -> str:
    reverse_string = ""
    new_word = ""
    for i in text:
        if i == " ":
            reverse_string += new_word + " "
            new_word = ""
        else:
            new_word = i + new_word
        
    reverse_string += new_word
    
    return reverse_string


print(reverse_words("This is an example!"))
print("sihT si na !elpmaxe")
