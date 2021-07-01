'''
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2
Example 2:

Input: [1,3,5,6], 2
Output: 1
Example 3:

Input: [1,3,5,6], 7
Output: 4
Example 4:

Input: [1,3,5,6], 0
Output: 0
'''


class Solution(object):
    def searchInsert(self, nums, target):
        for i in range(len(nums)):
            if target - nums[i] == 0:
                return i

        if target < min(nums):
            return 0
        if target > max(nums):
            return(len(nums))

        for i in range(len(nums)-1):
            if nums[i] < target and nums[i+1] > target:
                return i+1


# Binary Search - Solution

def search_insert(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:

        mid = (left + right) // 2

        if target == nums[mid]:
            return mid

        if target > nums[mid]:
            left = mid + 1

        else:
            right = mid - 1

    return left
