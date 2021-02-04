'''
Given a string and a pattern, find the smallest substring in the given string which has all the characters of the given pattern.

Example 1:

Input: String="aabdec", Pattern="abc"
Output: "abdec"
Explanation: The smallest substring having all characters of the pattern is "abdec"
Example 2:

Input: String="abdabca", Pattern="abc"
Output: "abc"
Explanation: The smallest substring having all characters of the pattern is "abc".
Example 3:

Input: String="adcad", Pattern="abc"
Output: ""
Explanation: No substring in the given string has all characters of the pattern.
'''


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        window_start = 0
        substr_start = 0
        matched = 0
        min_length = len(s) + 1
        dict = {}

        for chr in t:
            if chr not in dict:
                dict[chr] = 0

            dict[chr] += 1

        for window_end in range(0, len(s)):

            right_char = s[window_end]

            if right_char in dict:
                dict[right_char] -= 1

                if dict[right_char] >= 0:
                    matched += 1

                while matched == len(t):

                    if window_end - window_start + 1 < min_length:
                        min_length = window_end - window_start + 1
                        substr_start = window_start

                    # shrink the window from start
                    left_char = s[window_start]
                    window_start += 1

                    if left_char in dict:
                        if dict[left_char] == 0:
                            matched -= 1

                        dict[left_char] += 1

        if min_length > len(s):
            return ''

        return s[substr_start: substr_start+min_length]
