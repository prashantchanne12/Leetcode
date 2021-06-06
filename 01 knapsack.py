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

# Solution 3 - DP Bottom up approach


def knapsack_bottom_up(profits, weights, capacity):

    # create matrix
    dp = [[0 if x == 0 or y == 0 else -
           1 for x in range(0, capacity+1)] for y in range(0, len(profits)+1)]

    for i in range(1, len(profits)+1):
        for j in range(1, capacity+1):

            if weights[i-1] <= j:
                dp[i][j] = max(
                    profits[i-1] + dp[i-1][j-weights[i-1]],
                    dp[i-1][j]
                )
            else:
                dp[i][j] = dp[i-1][j]

    return dp[len(profits)][capacity]


print(knapsack_bottom_up([20, 30, 10, 50], [1, 3, 4, 6], 10))
