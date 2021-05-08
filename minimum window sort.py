'''
Given an array, find the length of the smallest subarray in it which when sorted will sort the whole array.

Example 1:

Input: [1, 2, 5, 3, 7, 10, 9, 12]
Output: 5
Explanation: We need to sort only the subarray [5, 3, 7, 10, 9] to make the whole array sorted
Example 2:

Input: [1, 3, 2, 0, -1, 7, 10]
Output: 5
Explanation: We need to sort only the subarray [1, 3, 2, 0, -1] to make the whole array sorted
Example 3:

Input: [1, 2, 3]
Output: 0
Explanation: The array is already sorted
Example 4:

Input: [3, 2, 1]
Output: 3
Explanation: The whole array needs to be sorted.
'''

import math


def shortest_window_sort(arr):
    left = 0
    right = len(arr) - 1

    # find the first number which is out of sorting order from the begining
    while left < right and arr[left] <= arr[left + 1]:
        left += 1

    # this means array is sorted
    if left == right:
        return 0

    # find the first number which is out of sorting order from the end
    while right > 0 and arr[right] >= arr[right-1]:
        right -= 1

    # print(arr[left])
    # print(arr[right])

    # find the minimum and maximum of both subarray
    subarray_max = -math.inf
    subarray_min = math.inf

    for k in range(left, right+1):
        subarray_max = max(subarray_max, arr[k])
        subarray_min = min(subarray_min, arr[k])

    # print(subarray_max)
    # print(subarray_min)

    # extend the subarray to include any number which is bigger than the minimum of the subarray
    while left > 0 and arr[left-1] > subarray_min:
        left -= 1

    # extend the subarray to include any number which is smaller than the maximum of the subarray
    while right < len(arr) - 1 and arr[right+1] < subarray_max:
        right += 1

    return right - left + 1


print(shortest_window_sort([1, 2, 3]))
