'''
Given a set of positive numbers, determine if a subset exists whose sum is equal to a given number ‘S’.

Example 1: #
Input: {1, 2, 3, 7}, S=6
Output: True
The given set has a subset whose sum is '6': {1, 2, 3}

Example 2: #
Input: {1, 2, 7, 1, 5}, S=10
Output: True
The given set has a subset whose sum is '10': {1, 2, 7}

Example 3: #
Input: {1, 3, 4, 8}, S=6
Output: False
The given set does not have any subset whose sum is equal to '6'.
'''


def subset_sum(nums, sum):

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

    return dp[len(nums)][sum]


print(subset_sum([1, 2, 3, 7], 6))
print(subset_sum([1, 2, 7, 1, 5], 10))
print(subset_sum([1, 2, 3], 7))
