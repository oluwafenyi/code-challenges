
# https://www.codewars.com/kata/find-the-odd-int
# For a given array, find the number that appears an odd number of times.


# def find_it(arr):
#     for num in arr:
#         if arr.count(num) % 2 != 0:
#             return num


def find_it(arr):
    return [num for num in arr if arr.count(num) % 2 != 0][0]
