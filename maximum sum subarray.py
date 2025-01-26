'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
'''
# Solution 1


def maxSub(nums):
    max_current = max_global = nums[0]
    for i in range(1, len(nums)):
        max_current = max(nums[i], max_current + nums[i])
        if max_current > max_global:
            max_global = max_current

    return max_global

# Solution 2


def max_sum_subarray(nums):
    max_sum = 0
    current_sum = 0

    for i in range(0, len(nums)):
        current_sum += nums[i]
        max_sum = max(max_sum, current_sum)

        if current_sum < 0:
            current_sum = 0

    return max_sum


print(max_sum_subarray([5, -4, -2, 6, -1]))


# Solution 3 - DP
# Time complexity: O(n)
# Space complexity: O(n)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:            
        res = [0]*(len(nums)+1)
        
        for i in range(1, len(nums)+1):
            res[i] = max(res[i-1] + nums[i-1], nums[i-1])
            
        return max(res[1:])