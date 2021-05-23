'''
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
'''


class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()

        subsets = []
        subsets.append([])

        start_index = 0
        end_index = 0

        for i in range(0, len(nums)):

            start_index = 0

            if i > 0 and nums[i-1] == nums[i]:
                start_index = end_index

            end_index = len(subsets)

            for j in range(start_index, end_index):

                set = list(subsets[j])
                set.append(nums[i])
                subsets.append(set)

        return subsets
