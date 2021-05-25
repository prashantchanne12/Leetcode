''''
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
'''


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = [-1, -1]

        res[0] = self.binary_search(nums, target, False)

        if res[0] != -1:
            res[1] = self.binary_search(nums, target, True)

        return res

    def binary_search(self, arr, key, find_max_index):

        key_index = -1

        low = 0
        high = len(arr) - 1

        while low <= high:

            mid = (low+high) // 2

            if key == arr[mid]:

                key_index = mid

                if find_max_index:
                    low = mid + 1
                else:
                    high = mid - 1

            elif key > arr[mid]:
                low = mid + 1
            else:
                high = mid - 1

        return key_index
