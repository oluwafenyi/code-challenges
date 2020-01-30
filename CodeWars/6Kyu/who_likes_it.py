
# https://www.codewars.com/kata/who-likes-it

def likes(name):
    if len(name) == 0:
        return 'no one likes this'
    elif len(name) == 1:
        return name[0] + ' likes this'
    elif len(name) == 2:
        return ' and '.join(name) + ' like this'
    elif len(name) == 3:
        return ', '.join(name[:2]) + ' and ' + name[2] + ' like this'
    else:
        return ', '.join(name[:2]) + ' and ' + str(len(name[2:])) + ' others'
        + ' like this'


print(likes([]))
print(likes(["Peter"]))
print(likes(["Jacob", "Alex"]))
print(likes(["Max", "John", "Mark"]))
print(likes(["Alex", "Jacob", "Mark", "Max"]))
