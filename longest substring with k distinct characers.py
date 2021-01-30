'''
Given a string, find the length of the longest substring in it with no more than K distinct characters.

Example 1:

Input: String="araaci", K=2
Output: 4
Explanation: The longest substring with no more than '2' distinct characters is "araa".
Example 2:

Input: String="araaci", K=1
Output: 2
Explanation: The longest substring with no more than '1' distinct characters is "aa".
Example 3:

Input: String="cbbebi", K=3
Output: 5
Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi".
'''


def longest_substring_with_k_distinct(str, k):

    window_start = 0
    max_length = 0
    char_frequency = {}

    for window_end in range(0, len(str)):

        right_char = str[window_end]

        if right_char not in char_frequency:
            char_frequency[right_char] = 0

        char_frequency[right_char] += 1

        # shrink the sliding window, until we are left with 'k' distinct characters in the char_frequency
        while len(char_frequency) > k:

            left_char = str[window_start]
            window_start += 1

            char_frequency[left_char] -= 1

            if char_frequency[left_char] == 0:
                del char_frequency[left_char]

        # remember the maximum length so far
        max_length = max(max_length, window_end - window_start + 1)

    return max_length


print(longest_substring_with_k_distinct('araaci', 2))
