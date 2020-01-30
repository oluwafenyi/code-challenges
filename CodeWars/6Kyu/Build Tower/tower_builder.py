
# check https://www.codewars.com/kata/576757b1df89ecf5bd00073b/ for specs.

def tower_builder(n):
    return [('*'*(1+(i-1)*2)).center(1+(n-1)*2) for i in range(1, n+1)]
