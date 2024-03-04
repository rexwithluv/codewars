""" Write Number in Expanded Form
You will be given a number and you will need to return it as a string in Expanded Form. For example:

expanded_form(12) # Should return '10 + 2'
expanded_form(42) # Should return '40 + 2'
expanded_form(70304) # Should return '70000 + 300 + 4'
NOTE: All numbers will be whole numbers greater than 0.

If you liked this kata, check out part 2!! """

def expanded_form(num: int) -> str:
    lst = []
    
    # Creamos la forma expandida en una lista
    for position, i in enumerate(str(num)):
        if i != 0:
            lst.append(i + ("0" * (len(str(num)) - (position + 1))))

    # Limpiamos la lista expandida por si tuviera algún elemento similar a '0000'
    clean_lst = []
    for i in lst:
        if i[0] != "0":
            clean_lst.append(i)
    
    return " + ".join(clean_lst)