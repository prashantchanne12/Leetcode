'''
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

 

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        result = nums[0] + nums[1] + nums[len(nums)-1]
        nums.sort()

        for i in range(0, len(nums)-2):
            left = i + 1
            right = len(nums) - 1

            while left < right:

                current_sum = nums[i] + nums[left] + nums[right]

                if target > current_sum:
                    left += 1
                else:
                    right -= 1

                if abs(current_sum - target) < abs(result-target):
                    result = current_sum

        return result
