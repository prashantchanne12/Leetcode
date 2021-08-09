'''
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

 

Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000
Example 2:

Input: x = 2.10000, n = 3
Output: 9.26100
Example 3:

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
 
'''


class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # if n is 0
        if n == 0:
            return 1

        # if n is -ve
        elif n < 0:
            return self.myPow(1/x, -n)

        # if n is even
        elif n % 2 == 0:
            temp = self.myPow(x, n/2)
            return temp * temp

        # if n is odd
        else:
            return x * self.myPow(x, n-1)
