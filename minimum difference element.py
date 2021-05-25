'''
Given an array of numbers sorted in ascending order, find the element in the array that has the minimum difference with the given ‘key’.

Example 1:

Input: [4, 6, 10], key = 7
Output: 6
Explanation: The difference between the key '7' and '6' is minimum than any other number in the array 
Example 2:

Input: [4, 6, 10], key = 4
Output: 4
Example 3:

Input: [1, 3, 8, 10, 15], key = 12
Output: 10
Example 4:

Input: [4, 6, 10], key = 17
Output: 10
'''


def search_min_diff_element(arr, key):

    low = 0
    high = len(arr) - 1

    if key < arr[low]:
        return arr[low]

    if key > arr[high]:
        return arr[high]

    while low <= high:

        mid = (low + high) // 2

        if key == arr[mid]:
            return arr[mid]

        if key > arr[mid]:
            low = mid + 1

        else:
            high = mid - 1

    if abs(key - arr[low]) < abs(key - arr[high]):
        return arr[low]

    return arr[high]


print(search_min_diff_element([4, 6, 10], 7))
print(search_min_diff_element([4, 6, 10], 4))
print(search_min_diff_element([1, 3, 8, 10, 15], 12))
print(search_min_diff_element([4, 6, 10], 17))
