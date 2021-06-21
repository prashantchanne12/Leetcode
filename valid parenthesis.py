'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
'''

# Solution 1


class Solution(object):
    def isValid(self, s):
        if s == '':
            return True
        stack = []
        for i in s:
            if i in '{([':
                stack.append(i)
            elif i in '})]':
                if i == ')' and len(stack) > 0 and stack[-1] == '(':
                    stack.pop()
                elif i == '}' and len(stack) > 0 and stack[-1] == '{':
                    stack.pop()
                elif i == ']' and len(stack) > 0 and stack[-1] == '[':
                    stack.pop()
                else:
                    return False

        return len(stack) == 0


# Solution 2
class Solution(object):
    def isValid(self, s):
        dict = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for i in range(0, len(s)):
            if s[i] in '{[(':
                stack.append(s[i])
            elif len(stack) > 0 and dict[stack[-1]] == s[i]:
                stack.pop()
            else:
                return False

        return len(stack) == 0

# Solution 3


class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) == 0:
            return True

        stack = []
        dict = {
            '(': ')',
            '[': ']',
            '{': '}',
        }

        for bracket in s:

            if bracket in dict:
                stack.append(bracket)
            else:
                if len(stack) > 0:
                    if dict[stack.pop()] != bracket:
                        return False
                elif len(stack) == 0:
                    return False

        return len(stack) == 0
