'''
Given an integer n, find fibonacci number for nth number
'''

# 1. Normal Recursive Solution


def fib(n):

    if n == 1 or n == 2:
        res = 1

    else:
        res = fib(n-1) + fib(n-2)

    return res


print(fib(6))

# 2. DP - Recusive Soluton


def fib_dp(n, memo):

    if memo[n] >= 0:
        return memo[n]

    if n == 1 or n == 2:
        res = 1

    else:
        res = fib_dp(n-1, memo) + fib_dp(n-2, memo)

    memo[n] = res
    return res


print(fib_dp(6,  [-1 for x in range(0, 6+1)]))

# 3. DP - Bottom up approach


def fib_bottom_up(n):

    memo = [-1 for x in range(0, n+1)]

    memo[1] = 1
    memo[2] = 1

    for i in range(3, n+1):

        memo[i] = memo[i-1] + memo[i-2]

    return memo[n]


print(fib_bottom_up(6))
