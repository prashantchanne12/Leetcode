'''
Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".
Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".
Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".
Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".
'''


class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        s1_pointer = len(S)-1
        s2_pointer = len(T)-1

        s1_skip = 0
        s2_skip = 0

        while s1_pointer >= 0 or s2_pointer >= 0:

            while s1_pointer >= 0:

                if S[s1_pointer] == '#':
                    s1_skip += 1
                    s1_pointer -= 1
                elif s1_skip > 0:
                    s1_skip -= 1
                    s1_pointer -= 1
                else:
                    break

            while s2_pointer >= 0:

                if T[s2_pointer] == '#':
                    s2_skip += 1
                    s2_pointer -= 1
                elif s2_skip > 0:
                    s2_skip -= 1
                    s2_pointer -= 1
                else:
                    break

            if s1_pointer >= 0 and s2_pointer >= 0 and S[s1_pointer] != T[s2_pointer]:
                return False

            if (s1_pointer >= 0) != (s2_pointer >= 0):
                return False

            s1_pointer -= 1
            s2_pointer -= 1

        return True
