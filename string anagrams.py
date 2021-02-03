'''
Given a string and a pattern, find all anagrams of the pattern in the given string.

Example 1:

Input: String="ppqp", Pattern="pq"
Output: [1, 2]
Explanation: The two anagrams of the pattern in the given string are "pq" and "qp".
Example 2:

Input: String="abbcabc", Pattern="abc"
Output: [2, 3, 4]
Explanation: The three anagrams of the pattern in the given string are "bca", "cab", and "abc".
'''


def string_anagrams(str, pattern):

    window_start = 0
    mactched = 0
    dict = {}
    res = []

    for chr in pattern:
        if chr not in dict:
            dict[chr] = 0

        dict[chr] += 1

    for window_end in range(0, len(str)):

        right_char = str[window_end]

        if right_char in dict:
            dict[right_char] -= 1

            if dict[right_char] == 0:
                mactched += 1

            if mactched == len(pattern):
                res.append(window_start)

        if window_end >= len(pattern) - 1:
            # shrink the window from start
            left_char = str[window_start]
            window_start += 1

            # increment the char if it is in dict
            if left_char in dict:
                if dict[left_char] == 0:
                    mactched -= 1

                dict[left_char] += 1

    return res


print(string_anagrams('ppqp', 'pq'))
