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

'''

# Solution - 1


class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        def build(str):
            arr = []

            for i in str:
                if i != '#':
                    arr.append(i)
                else:
                    if arr:
                        arr.pop()

            return ''.join(arr)

        return build(S) == build(T)

# Solution - 2


def build(string):
    arr = []
    for chr in string:
        if chr == '#' and len(arr) != 0:
            arr.pop()
        elif chr != '#':
            arr.append(chr)

    return arr


def typed_out_strings(s, t):

    s_arr = build(s)
    t_arr = build(t)

    return ''.join(s_arr) == ''.join(t_arr)


print(typed_out_strings('##z', '#z'))
