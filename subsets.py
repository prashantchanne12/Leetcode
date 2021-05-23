'''
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
 
'''

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        subsets = []
        subsets.append([])

        for current_number in nums:
            
            n = len(subsets)
            
            for i in range(0, n):
                
                set = list(subsets[i])
                set.append(current_number)
                subsets.append(set)
                
        return subsets