'''
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
'''

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = {0 : 1}
        current_sum = 0
        res = 0

        for num in nums:
            current_sum += num

            difference = current_sum - k

            if difference in prefix:
                res += prefix[difference]

            if current_sum not in prefix:
                prefix[current_sum] = 0

            prefix[current_sum] += 1

        return res