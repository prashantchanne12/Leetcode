'''
Given an unsorted array containing numbers, find the smallest missing positive number in it.

Example 1:

Input: [-3, 1, 5, 4, 2]
Output: 3
Explanation: The smallest missing positive number is '3'
Example 2:

Input: [3, -2, 0, 1, 2]
Output: 4
Example 3:

Input: [3, 2, 5, 1]
Output: 4
'''


def find_missing_positive(nums):
    i = 0
    n = len(nums)

    while i < n:
        j = nums[i] - 1

        if nums[i] > 0 and nums[i] <= n and nums[i] != nums[j]:
            # swap
            nums[i], nums[j] = nums[j], nums[i]

        else:
            i += 1

    for i in range(0, n):
        if nums[i] != i + 1:
            return i + 1

    return n + 1


print(find_missing_positive([3, -2, 0, 1, 2]))
