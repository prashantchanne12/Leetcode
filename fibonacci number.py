class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n == 0 or n == 1:
            return n

        memo = [-1 for x in range(n+1)]
        memo[1] = 1
        memo[2] = 1

        for i in range(3, n+1):
            memo[i] = memo[i-1] + memo[i-2]

        return memo[-1]
