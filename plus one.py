'''
Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

 
Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Example 3:

Input: digits = [0]
Output: [1]
'''

# Solution 1


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        num = ''

        for i in digits:
            num += str(i)

        num = int(num)
        num += 1
        num = str(num)
        arr = [int(x) for x in num]

        return arr

# Solution 2


def plus_one(digits):

    n = len(digits)-1

    while n >= 0:
        if digits[n] < 9:
            digits[n] += 1
            return digits

        digits[n] = 0
        n -= 1

    digits.insert(0, 1)
    return digits


print(plus_one([1, 2, 5]))
