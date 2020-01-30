
#https://www.codewars.com/kata/find-the-missing-letter

from string import ascii_letters


def find_missing_letter(chars):
    ind = ascii_letters.index(chars[0])
    corr_seq = list(ascii_letters[ind:ind+len(chars)+1])
    return [char for char in corr_seq if char not in chars][0]
