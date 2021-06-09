'''
You are given a set of positive numbers and a target sum ‘S’. Each number should be assigned either a ‘+’ or ‘-’ sign. We need to find the total ways to assign symbols to make the sum of the numbers equal to the target ‘S’.

Example 1: #
Input: {1, 1, 2, 3}, S=1
Output: 3
Explanation: The given set has '3' ways to make a sum of '1': {+1-1-2+3} & {-1+1-2+3} & {+1+1+2-3}

Example 2: #
Input: {1, 2, 7, 1}, S=9
Output: 2
Explanation: The given set has '2' ways to make a sum of '9': {+1+2+7-1} & {-1+2+7+1}
'''


def target_sum(nums, diff):

    s = sum(nums)

    s = (s + diff) // 2

    # create matrix
    dp = [[0 for x in range(s+1)] for y in range(len(nums)+1)]

    for i in range(0, len(nums)+1):
        dp[i][0] = 1

    for i in range(1, len(nums)+1):
        for j in range(1, s+1):

            if nums[i-1] <= j:
                dp[i][j] = dp[i-1][j-nums[i-1]] + dp[i-1][j]

            else:
                dp[i][j] = dp[i-1][j]

    return dp[len(nums)][s]


print(target_sum([1, 1, 2, 3], 1))
