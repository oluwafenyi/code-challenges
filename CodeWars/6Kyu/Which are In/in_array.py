
# check https://www.codewars.com/kata/550554fd08b86f84fe000a58 for specs.

def in_array(array1, array2):
    return sorted(list(set(string for string in array1 for other_string
                           in array2 if string in other_string)))
