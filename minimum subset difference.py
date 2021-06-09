'''
Given a set of positive numbers, partition the set into two subsets with minimum difference between their subset sums.

Example 1: #
Input: {1, 2, 3, 9}
Output: 3
Explanation: We can partition the given set into two subsets where minimum absolute difference 
between the sum of numbers is '3'. Following are the two subsets: {1, 2, 3} & {9}.
Example 2: #
Input: {1, 2, 7, 1, 5}
Output: 0
Explanation: We can partition the given set into two subsets where minimum absolute difference 
between the sum of number is '0'. Following are the two subsets: {1, 2, 5} & {7, 1}.
Example 3: #
Input: {1, 3, 100, 4}
Output: 92
Explanation: We can partition the given set into two subsets where minimum absolute difference 
between the sum of numbers is '92'. Here are the two subsets: {1, 3, 4} & {100}.
'''

import math


def minimum_subset_diff(nums):

    sum = 0
    for num in nums:
        sum += num

    # create matrix
    dp = [[False for x in range(sum+1)] for y in range(len(nums)+1)]

    for i in range(0, len(nums)+1):
        dp[i][0] = True

    for i in range(1, len(nums)+1):
        for j in range(1, sum+1):

            if nums[i-1] <= j:
                dp[i][j] = dp[i-1][j-nums[i-1]] or dp[i-1][j]

            else:
                dp[i][j] = dp[i-1][j]

    res = []

    for i in range(1, sum+1):
        if dp[len(nums)][i]:
            res.append(i)

    diff = math.inf

    for i in range(0, len(res)//2):
        diff = min(diff, sum - (2*res[i]))

    return diff


print(minimum_subset_diff([1, 3, 100, 4]))
