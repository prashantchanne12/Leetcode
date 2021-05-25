'''
Given an array of numbers sorted in ascending order, find the floor of a given number ‘key’. The floor of the ‘key’ will be the biggest element in the given array smaller than or equal to the ‘key’

Write a function to return the index of the floor of the ‘key’. If there isn’t a floor, return -1.

Example 1:

Input: [4, 6, 10], key = 6
Output: 1
Explanation: The biggest number smaller than or equal to '6' is '6' having index '1'.
Example 2:

Input: [1, 3, 8, 10, 15], key = 12
Output: 3
Explanation: The biggest number smaller than or equal to '12' is '10' having index '3'.
Example 3:

Input: [4, 6, 10], key = 17
Output: 2
Explanation: The biggest number smaller than or equal to '17' is '10' having index '2'.
Example 4:

Input: [4, 6, 10], key = -1
Output: -1
Explanation: There is no number smaller than or equal to '-1' in the given array.
'''


def search_floor(arr, key):

    low = 0
    high = len(arr) - 1

    if key < arr[low]:
        return -1

    while low <= high:

        mid = (low + high) // 2

        if key == arr[mid]:
            return mid

        if key > arr[mid]:
            low = mid + 1

        else:
            high = mid - 1

    return high


print(search_floor([4, 6, 10], 6))
print(search_floor([1, 3, 8, 10, 15], 12))
print(search_floor([4, 6, 10], 17))
print(search_floor([4, 6, 10], -1))
