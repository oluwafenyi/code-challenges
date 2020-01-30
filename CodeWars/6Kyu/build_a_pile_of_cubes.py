
# https://www.codewars.com/kata/5592e3bd57b64d00f3000047/python

def find_nb(m):
    n = 0
    while ((n*(n+1))/2)**2 <= m:
        if ((n*(n+1))/2)**2 == m:
            return n
        n += 1
    return -1


print(find_nb(1071225))
