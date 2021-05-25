'''
Given a sorted array of numbers, find if a given number ‘key’ is present in the array. Though we know that the array is sorted, we don’t know if it’s sorted in ascending or descending order. You should assume that the array can have duplicates.

Write a function to return the index of the ‘key’ if it is present in the array, otherwise return -1.

Example 1:

Input: [4, 6, 10], key = 10
Output: 2
Example 2:

Input: [1, 2, 3, 4, 5, 6, 7], key = 5
Output: 4
Example 3:

Input: [10, 6, 4], key = 10
Output: 0
Example 4:

Input: [10, 6, 4], key = 4
Output: 2
'''

import math


def order_agnostic_bin_search(arr, key):

    low = 0
    high = len(arr) - 1

    is_asc = arr[low] < arr[high]

    while low <= high:

        mid = math.floor((low+high)/2)

        if arr[mid] == key:
            return mid

        if is_asc:

            if key > arr[mid]:
                low = mid + 1

            else:
                high = mid - 1

        else:

            if key > arr[mid]:
                high = mid - 1

            else:
                low = mid + 1

    return -1


print(order_agnostic_bin_search([6, 7, 2, 1], 1))
