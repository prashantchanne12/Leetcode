'''
Given a string, find the length of the longest substring which has no repeating characters.

Example 1:

Input: String="aabccbb"
Output: 3
Explanation: The longest substring without any repeating characters is "abc".
Example 2:

Input: String="abbbb"
Output: 2
Explanation: The longest substring without any repeating characters is "ab".
Example 3:

Input: String="abccde"
Output: 3
Explanation: Longest substrings without any repeating characters are "abc" & "cde".
'''


def no_repeat_substring(string):

    window_start = 0
    max_length = 0
    dict = {}

    for window_end in range(0, len(string)):

        right_char = string[window_end]

        if right_char not in dict:
            dict[right_char] = 1

            max_length = max(max_length, (window_end-window_start+1))
        else:

            dict[right_char] += 1

            while dict[right_char] != 1:
                # shrink the window from start
                left_char = string[window_start]
                dict[left_char] -= 1
                window_start += 1

            max_length = max(max_length, (window_end-window_start+1))

    return max_length


print(no_repeat_substring('aabccbb'))
