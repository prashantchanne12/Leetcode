# Solution 1 - Recursive


def knapsack(profits, weights, capacity, n):

    # base case
    if n == 0 or capacity == 0:
        return 0

    if weights[n-1] <= capacity:
        return max(
            profits[n-1] + knapsack(profits, weights,
                                    capacity-weights[n-1], n-1),
            knapsack(profits, weights, capacity, n-1)
        )

    else:
        knapsack(profits, weights, capacity, n-1)


print(knapsack([1, 6, 10, ], [1, 2, 3], 5, 3))

# Solution 2 - DP


def solve_knapsack(profits, weights, capacity):

    n = len(profits)

    dp = [[-1 for x in range(0, capacity+1)] for y in range(0, n)]

    return knapsack_recursive_dp(profits, weights, capacity, n, dp)


def knapsack_recursive_dp(profits, weights, capacity, n, dp):

    if n == 0 or capacity == 0:
        return 0

    if dp[n-1][capacity] != -1:
        return dp[n-1][capacity]

    if weights[n-1] <= capacity:

        dp[n-1][capacity] = max(
            profits[n-1] +
            knapsack_recursive_dp(
                profits, weights, capacity-weights[n-1], n-1, dp),
            knapsack_recursive_dp(profits, weights, capacity, n-1, dp)
        )

        return dp[n-1][capacity]

    else:
        dp[n-1][capacity] = knapsack_recursive_dp(
            profits, weights, capacity, n-1, dp)
        return dp[n-1][capacity]


print(solve_knapsack([1, 6, 10], [1, 2, 3], 5))
