'''
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
'''


class Solution(object):
    def climbStairs(self, n):

        res = 0
        memo = [-1 for x in range(n+1)]

        def stairs(n, res, memo):

            if memo[n] > 0:
                return memo[n]

            if n == 0 or n == 1:
                return 1

            res += stairs(n-1, res, memo) + stairs(n-2, res, memo)
            memo[n] = res
            return res

        return stairs(n, res, memo)
