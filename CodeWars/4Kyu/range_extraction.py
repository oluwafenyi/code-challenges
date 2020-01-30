
# Check https://www.codewars.com/kata/51ba717bb08c1cd60f00002f/python
# for specs


def get_range(args):
    const_first = args[0]
    var = args[0]
    next_index = 1

    try:
        while var == args[next_index] - 1:
            var = args[next_index]
            next_index += 1
    except IndexError:
        pass

    if var - const_first >= 2:
        return '{}_{}'.format(const_first, var)

    elif var - const_first == 1:
        return '{},{}'.format(const_first, var)

    else:
        return '{}'.format(var)


def solution(args):
    array = []
    charted = []
    for index, arg in enumerate(args):
        if arg in charted:
            continue
        val = get_range(args[index:])
        if '_' in val:
            start, end = map(lambda val: int(val), val.split('_'))
            charted += list(range(start, end + 1))
        else:
            charted += list(map(lambda val: int(val), val.split(',')))
        array.append(val.replace('_', '-'))
    return ','.join(array)


print(solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20]))
