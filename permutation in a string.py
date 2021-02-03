'''
Permutation in a String (hard) #
Given a string and a pattern, find out if the string contains any permutation of the pattern.

Permutation is defined as the re-arranging of the characters of the string. For example, “abc” has the following six permutations:

abc
acb
bac
bca
cab
cba
If a string has ‘n’ distinct characters it will have n!n! permutations.

Example 1:

Input: String="oidbcaf", Pattern="abc"
Output: true
Explanation: The string contains "bca" which is a permutation of the given pattern.
Example 2:

Input: String="odicf", Pattern="dc"
Output: false
Explanation: No permutation of the pattern is present in the given string as a substring.
Example 3:

Input: String="bcdxabcdy", Pattern="bcdyabcdx"
Output: true
Explanation: Both the string and the pattern are a permutation of each other.
Example 4:

Input: String="aaacb", Pattern="abc"
Output: true
Explanation: The string contains "acb" which is a permutation of the given pattern.
'''


def find_permutation(str, pattern):

    window_start = 0
    matched = 0
    dict = {}

    for chr in pattern:
        if chr not in dict:
            dict[chr] = 0

        dict[chr] += 1

    for window_end in range(0, len(str)):
        right_char = str[window_end]

        if right_char in dict:
            # decrement the freuency of matched character
            dict[right_char] -= 1
            if dict[right_char] == 0:
                matched += 1

        if matched == len(dict):
            return True

        if window_end >= len(pattern)-1:
            # shrink the window from start
            left_char = str[window_start]
            window_start += 1

            # reseting match and dictionary
            if left_char in dict:
                if dict[left_char] == 0:
                    macthed -= 1

                dict[left_char] += 1

    return False


print(find_permutation('oidbcaf', 'abc'))
