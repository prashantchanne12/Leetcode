'''
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
'''


class Solution(object):
    def majorityElement(self, nums):
        dict = {}
        for i in range(len(nums)):
            if nums[i] in dict:
                dict[nums[i]] = dict.get(nums[i]) + 1
            else:
                dict[nums[i]] = 1

        for key, value in dict.items():
            if value > len(nums)/2:
                return key


def majority_element_2(nums):
    ans_index = 0
    count = 1

    for i in range(1, len(nums)):

        if nums[i] == nums[ans_index]:
            count += 1
        else:
            count -= 1

        if count == 0:
            ans_index = i
            count = 1

    return nums[ans_index]
