'''
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range:
[−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
'''

class Solution(object):
    def reverse(self, x):
        num = int(str(abs(x))[::-1])
        
        if num >= 2**31-1 or num <= -2**31:
            return 0
            
        return -num if x<0 else num
