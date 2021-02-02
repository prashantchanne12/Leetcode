'''
Given a string with lowercase letters only, if you are allowed to replace no more than ‘k’ letters with any letter, find the length of the longest substring having the same letters after replacement.

Example 1:

Input: String="aabccbb", k=2
Output: 5
Explanation: Replace the two 'c' with 'b' to have a longest repeating substring "bbbbb".
Example 2:

Input: String="abbcb", k=1
Output: 4
Explanation: Replace the 'c' with 'b' to have a longest repeating substring "bbbb".
Example 3:

Input: String="abccde", k=1
Output: 3
Explanation: Replace the 'b' or 'd' with 'c' to have the longest repeating substring "ccc".
'''


class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        window_start = 0
        max_length = 0
        max_repeating_char_length = 0
        dict = {}

        for window_end in range(0, len(s)):

            right_char = s[window_end]

            if right_char not in dict:
                dict[right_char] = 0

            dict[right_char] += 1

            # calculate max repeating char for the window
            max_repeating_char_length = max(
                max_repeating_char_length, dict[right_char])

            if (window_end - window_start + 1) - max_repeating_char_length > k:
                # we can't replace the characters and form a longest substring as k is smaller
                # shrink the window from start
                left_char = s[window_start]
                dict[left_char] -= 1
                window_start += 1

            max_length = max(max_length, window_end-window_start+1)

        return max_length
