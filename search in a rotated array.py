'''
Given an array of numbers which is sorted in ascending order and also rotated by some arbitrary number, find if a given ‘key’ is present in it.

Write a function to return the index of the ‘key’ in the rotated array. If the ‘key’ is not present, return -1. You can assume that the given array does not have any duplicates.

Example 1:

Input: [10, 15, 1, 3, 8], key = 15
Output: 1
Explanation: '15' is present in the array at index '1'.

Input: [4, 5, 7, 9, 10, -1, 2], key = 10
Output: 4
Explanation: '10' is present in the array at index '4'.
'''


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0
        high = len(nums) - 1

        arr = nums
        key = target

        while low <= high:

            mid = (low + high) // 2

            if key == arr[mid]:
                return mid

            if arr[low] <= arr[mid]:  # low to mid is sorted

                # check if key is present in low to end
                if key >= arr[low] and key < arr[mid]:
                    high = mid - 1

                else:
                    low = mid + 1

            else:  # mid to high is sorted

                # check if key is present int mid to high
                if key > arr[mid] and key <= arr[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1
