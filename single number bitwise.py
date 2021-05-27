'''
In a non-empty array of integers, every number appears twice except for one, find that single number.

Example 1:

Input: 1, 4, 2, 1, 3, 2, 3
Output: 4
Example 2:

Input: 7, 9, 7
Output: 9
'''


def find_single_number(arr):

    res = 0

    for num in arr:
        res = res ^ num

    return res


print(find_single_number([1, 2, 3, 2, 1]))
