'''
Given a string s, return the longest palindromic substring in s.

 
Example 1:

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
Example 3:

Input: s = "a"
Output: "a"
Example 4:

Input: s = "ac"
Output: "a"
'''


class Solution(object):
    def longestPalindrome(self, s):

        res = ''
        res_len = 0

        for i in range(len(s)):

            # odd length pallindromes

            left = i
            right = i

            while left >= 0 and right < len(s) and s[left] == s[right]:

                if (right - left) + 1 > res_len:
                    res = s[left: right+1]
                    res_len = (right-left) + 1

                left -= 1
                right += 1

            # even length pallindromes
            left = i
            right = i + 1

            while left >= 0 and right < len(s) and s[left] == s[right]:

                if (right - left) + 1 > res_len:
                    res = s[left: right+1]
                    res_len = (right-left) + 1

                left -= 1
                right += 1

        return res
