'''
Given a set of positive numbers, find the total number of subsets whose sum is equal to a given number ‘S’.

Example 1: #
Input: {1, 1, 2, 3}, S=4
Output: 3
The given set has '3' subsets whose sum is '4': {1, 1, 2}, {1, 3}, {1, 3}
Note that we have two similar sets {1, 3}, because we have two '1' in our input.
Example 2: #
Input: {1, 2, 7, 1, 5}, S=9
Output: 3
The given set has '3' subsets whose sum is '9': {2, 7}, {1, 7, 1}, {1, 2, 1, 5}
'''


def count_of_subset(nums, sum):

    # create matrix
    dp = [[0 for x in range(sum+1)] for y in range(len(nums)+1)]

    for i in range(0, len(nums)+1):
        dp[i][0] = 1

    for i in range(1, len(nums)+1):
        for j in range(1, sum+1):

            if nums[i-1] <= j:
                dp[i][j] = dp[i-1][j-nums[i-1]] + dp[i-1][j]

            else:
                dp[i][j] = dp[i-1][j]

    return dp[len(nums)][sum]


print(count_of_subset([1, 1, 2, 3], 4))
print(count_of_subset([1, 2, 7, 1, 5], 9))
