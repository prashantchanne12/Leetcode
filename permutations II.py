'''
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

 

Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
'''


class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        permutations = []
        dict = {}

        for num in nums:
            if num not in dict:
                dict[num] = 0

            dict[num] += 1

        def backtrack():

            if len(permutations) == len(nums):
                res.append(list(permutations))
                return

            for num in dict:
                if dict[num] > 0:
                    permutations.append(num)
                    dict[num] -= 1

                    backtrack()

                    dict[num] += 1
                    permutations.pop()

        backtrack()
        return res
