'''
Given an infinite sorted array (or an array with unknown size), find if a given number ‘key’ is present in the array. Write a function to return the index of the ‘key’ if it is present in the array, otherwise return -1.

Since it is not possible to define an array with infinite (unknown) size, you will be provided with an interface ArrayReader to read elements of the array. ArrayReader.get(index) will return the number at index; if the array’s size is smaller than the index, it will return Integer.MAX_VALUE.

Example 1:

Input: [4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30], key = 16
Output: 6
Explanation: The key is present at index '6' in the array.
Example 2:

Input: [4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30], key = 11
Output: -1
Explanation: The key is not present in the array.
Example 3:

Input: [1, 3, 8, 10, 15], key = 15
Output: 4
Explanation: The key is present at index '4' in the array.
Example 4:

Input: [1, 3, 8, 10, 15], key = 200
Output: -1
Explanation: The key is not present in the array.
'''

import math


class ArrayReader:
    def __init__(self, arr):
        self.arr = arr

    def get(self, index):
        if index > len(self.arr):
            return math.inf

        return self.arr[index]


def search_in_infinite_array(reader, key):
    # first find the bounds

    low = 0
    high = 1

    while reader.get(high) < key:
        new_low = high + 1
        high = (high - low + 1)*2
        low = new_low

    return binary_search_array(reader, key, low, high)


def binary_search_array(reader, key, low, high):

    while low <= high:

        mid = (low + high) // 2

        if key == reader.get(mid):
            return mid

        if key > reader.get(mid):
            low = mid + 1

        else:
            high = mid - 1

    return - 1


reader = ArrayReader([4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30])
print(search_in_infinite_array(reader, 16))
