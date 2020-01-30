
# https://www.codewars.com/kata/create-phone-number

def create_phone_number(n):
    return '({}) {}-{}'.format(''.join(str(c) for c in n[:3]), ''.join(str(c) for c in n[3:6]), ''.join(str(c) for c in n[6:]))


print(create_phone_number(range(10)))
print(create_phone_number(([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])))
