'''
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Follow-up: Could you solve the problem in linear time and in O(1) space?

 

Example 1:

Input: nums = [3,2,3]
Output: [3]
Example 2:

Input: nums = [1]
Output: [1]
Example 3:

Input: nums = [1,2]
Output: [1,2]
'''


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        num_1 = -1
        num_2 = -1

        count_1 = 0
        count_2 = 0

        for num in nums:

            if num == num_1:
                count_1 += 1

            elif num == num_2:
                count_2 += 1

            elif count_1 == 0:
                num_1 = num
                count_1 = 1

            elif count_2 == 0:
                num_2 = num
                count_2 = 1

            else:

                count_1 -= 1
                count_2 -= 1

        # [3, 2, 3] => [3]
        res = []
        count_1 = 0
        count_2 = 0

        for num in nums:

            if num == num_1:
                count_1 += 1

            elif num == num_2:
                count_2 += 1

        if count_1 > len(nums) // 3:
            res.append(num_1)

        if count_2 > len(nums) // 3:
            res.append(num_2)

        return res

# Solution 2

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        dict = {}

        for num in nums:
            if num not in dict:
                dict[num] = 0

            dict[num] += 1

            if len(dict) <= 2:
                continue

            new_dict = {}
            for key, val in dict.items():
                if val > 1:
                    new_dict[key] = val - 1

            dict = new_dict

        
        res = []

        for num in dict:
            if nums.count(num) > len(nums) // 3:
                res.append(num)

        return res
        