'''
Given a set of positive numbers, find if we can partition it into two subsets such that the sum of elements in both subsets is equal.

Example 1:

Input: {1, 2, 3, 4}
Output: True
Explanation: The given set can be partitioned into two subsets with equal sum: {1, 4} & {2, 3}
Example 2:

Input: {1, 1, 3, 4, 7}
Output: True
Explanation: The given set can be partitioned into two subsets with equal sum: {1, 3, 4} & {1, 7}
Example 3:

Input: {2, 3, 4, 6}
Output: False
Explanation: The given set cannot be partitioned into two subsets with equal sum.
'''


def equal_sum_partition(nums):

    sum = 0

    for num in nums:
        sum += num

    if sum % 2 != 0:
        return False

    sum = sum // 2

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


print(equal_sum_partition([1, 5, 11, 5]))
print(equal_sum_partition([1, 40, 11, 5]))
print(equal_sum_partition([1, 6, 3]))
print(equal_sum_partition([1, 4, 5]))
