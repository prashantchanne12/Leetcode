'''
Given an array of positive numbers and a positive number ‘k’, find the maximum sum of any contiguous subarray of size ‘k’.

Example 1:

Input: [2, 1, 5, 1, 3, 2], k=3 
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3].
Example 2:

Input: [2, 3, 4, 1, 5], k=2 
Output: 7
Explanation: Subarray with maximum sum is [3, 4].
'''


def max_sub_array(nums, k):

    windowSum = 0
    windowStart = 0
    max_sum = 0

    for windowEnd in range(0, len(nums)):

        windowSum += nums[windowEnd]

        if windowEnd >= k-1:
            max_sum = max(max_sum, windowSum)
            windowSum -= nums[windowStart]
            windowStart += 1

    return max_sum


print(max_sub_array([5, 1, 3], 3))
