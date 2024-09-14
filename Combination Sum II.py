'''
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

 

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]
 

Constraints:

1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30
'''

class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(current, index):
            if sum(current) == target:
                res.append(current.copy())
                return 

            if index > len(nums) - 1:
                return

            if sum(current) > target:
                return 

            current.append(nums[index])
            backtrack(current, index+1)
            current.pop()

            while index + 1 < len(nums) and nums[index] == nums[index+1]:
                index += 1

            backtrack(current, index+1)

        backtrack([], 0)

        return res 

