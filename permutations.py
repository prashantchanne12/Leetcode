'''
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]
'''


from collections import deque


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums_len = len(nums)
        res = []

        permutations = deque()
        permutations.append([])

        for current_number in nums:

            for i in range(0, len(permutations)):

                old_permutation = permutations.popleft()

                for j in range(0, len(old_permutation) + 1):

                    new_permutation = list(old_permutation)
                    new_permutation.insert(j, current_number)

                    if len(new_permutation) == nums_len:
                        res.append(new_permutation)
                    else:
                        permutations.append(new_permutation)

        return res
