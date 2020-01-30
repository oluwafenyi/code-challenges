
# https://www.codewars.com/kata/valid-braces
# Write a function that takes a string of braces, and determines if the order
# of the braces is valid. It should return true if the string is valid,
# and false if it's invalid.


def validBraces(string):
    while '[]' in string or '{}' in string or '()' in string:
        string_list = list(string)
        if '[]' in string:
            string_list.remove('[')
            string_list.remove(']')
        elif '{}' in string:
            string_list.remove('{')
            string_list.remove('}')
        elif '()' in string:
            string_list.remove('(')
            string_list.remove(')')
        string = ''.join(string_list)
    return not bool(string)
