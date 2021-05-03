'''
Given an array of positive integers nums, return the maximum possible sum of an ascending subarray in nums.

A subarray is defined as a contiguous sequence of numbers in an array.

A subarray [numsl, numsl+1, ..., numsr-1, numsr] is ascending if for all i where l <= i < r, numsi < numsi+1. Note that a subarray of size 1 is ascending.

 

Example 1:

Input: nums = [10,20,30,5,10,50]
Output: 65
Explanation: [5,10,50] is the ascending subarray with the maximum sum of 65.
Example 2:

Input: nums = [10,20,30,40,50]
Output: 150
Explanation: [10,20,30,40,50] is the ascending subarray with the maximum sum of 150.
Example 3:

Input: nums = [12,17,15,13,10,11,12]
Output: 33
Explanation: [10,11,12] is the ascending subarray with the maximum sum of 33.
Example 4:

Input: nums = [100,10,1]
Output: 100
'''


class Solution(object):
    def maxAscendingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        right = len(nums) - 1
        arr = []
        last_num = nums[0]
        max_sum = last_num

        if len(nums) == 1:
            return nums[0]

        for i in range(1, len(nums)):
            if nums[i] <= last_num:
                arr.append(max_sum)
                max_sum = nums[i]
            elif i == right:
                max_sum += nums[i]
                arr.append(max_sum)
            else:
                max_sum += nums[i]

            last_num = nums[i]

        return max(arr)
