'''
Given a string s, return true if the s can be palindrome after deleting at most one character from it.


Example 1:

Input: s = "aba"
Output: true
Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
Example 3:

Input: s = "abc"
Output: false
'''


class Solution(object):
    def check_pallindrome(self, string, left, right):

        while left < right:
            if string[left] == string[right]:
                left += 1
                right -= 1

            else:
                return False

        return True

    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        if len(s) <= 2:
            return True

        s = s.split(' ')
        s = ''.join(s)

        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return self.check_pallindrome(s, left+1, right) or self.check_pallindrome(s, left, right-1)

        return True
