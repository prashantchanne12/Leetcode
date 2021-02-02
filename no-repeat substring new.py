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


def no_repeat_substring(str):

    window_start = 0
    max_length = 0
    dict = {}

    for window_end in range(0, len(str)):

        right_char = str[window_end]

        if right_char in dict:
            # jump the window_start pointer at the 'right_char'
            window_start = max(window_start, dict[right_char] + 1)

        # save the 'right_char' occurence with its index
        dict[right_char] = window_end

        max_length = max(max_length, (window_end-window_start+1))

    return max_length


print(no_repeat_substring('aabccbb'))
