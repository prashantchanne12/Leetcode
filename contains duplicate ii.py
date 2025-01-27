'''
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

 

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
'''

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashset = set()
        window_start = 0
        window_end = 0

        while window_end < len(nums):

            if window_end - window_start > k:
                hashset.remove(nums[window_start])
                window_start += 1

            if window_end - window_start <= k and nums[window_end] in hashset:
                return True

            hashset.add(nums[window_end])
            window_end += 1


        return False

                
