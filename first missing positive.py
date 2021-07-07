'''
Given an unsorted integer array nums, find the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses constant extra space.

 

Example 1:

Input: nums = [1,2,0]
Output: 3
Example 2:

Input: nums = [3,4,-1,1]
Output: 2
Example 3:

Input: nums = [7,8,9,11,12]
Output: 1
'''


def firstMissingPositive(nums):

        # for x in range(1, len(nums)+2):
        #        if x not in nums:
        #            return x

        # [3, 4, -1, 1, 9]
        # ans will in range 1 to len(nums)+1
        # 1...6
        # [-3, 4, -6, -1, -6]

    for i in range(0, len(nums)):
        if nums[i] <= 0 or nums[i] > len(nums):
            nums[i] = len(nums) + 1

    for num in nums:
        num = abs(num)

        if num <= len(nums) and nums[num-1] >= 0:
            nums[num-1] *= -1

    for i in range(len(nums)):
        if nums[i] > 0:
            return i+1

    return len(nums) + 1
