'''
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

 

Example 1:

Input: cost = [10,15,20]
Output: 15
Explanation: Cheapest is: start on cost[1], pay that cost, and go to the top.
Example 2:

Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: Cheapest is: start on cost[0], and only step on 1s, skipping cost[3].
'''
# Solution - 1


def min_cost_1(cost):

    n = len(cost)
    dp = [0 for x in range(n)]
    dp[0] = cost[0]
    dp[1] = cost[1]

    for i in range(2, n):
        dp[i] = cost[i] + min(dp[i-1], dp[i-2])

    return min(dp[n-1], dp[n-2])

# Solution - 2


def min_cost_2(cost):

    n = len(cost)
    dp = [0 for x in range(n)]
    dp[0] = cost[0]
    dp[1] = cost[1]

    for i in range(2, n):
        dp[i] = cost[i] + min(dp[i-1], dp[i-2])

    return min(dp[n-1], dp[n-2])

# Solution - 3


def min_cost_3(cost):

    n = len(cost)

    dp = [0 for x in range(n)]

    return min(min_cost_recursive(n-1, cost, dp), min_cost_recursive(n-2, cost, dp))


def min_cost_recursive(i, cost, dp):

    if i < 0:
        return 0

    if i == 0 or i == 1:
        return cost[i]

    if dp[i] != 0:
        return dp[i]

    dp[i] = cost[i] + min(min_cost_recursive(i-1, cost, dp),
                          min_cost_recursive(i-2, cost, dp))
    return dp[i]
