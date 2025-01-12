'''
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
'''

class Solution(object):
    def decodeString(self, s):
        counts = []
        result = []
        final = ''
        index = 0 

        while (index < len(s)):
            if s[index].isnumeric():
                count = 0 
                while(s[index].isnumeric()):
                    count = 10 * count + int(s[index])
                    index += 1

                counts.append(count)

            elif s[index] == '[':
                result.append(final)
                final = ''
                index += 1

            elif s[index] == ']':
                temp = []
                temp.append(result.pop())
                count = counts.pop();
                for i in range(count):
                    temp.append(final)

                final = ''.join(temp)
                index += 1

            else:
                final += s[index]
                index += 1

        return final
        
# Solution 2
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else:
                substr = ""
                while stack[-1] != "[":
                    substr = stack.pop() + substr
                stack.pop()

                multiplier = ""
                while stack and stack[-1].isdigit():
                    multiplier = stack.pop() + multiplier

                stack.append(int(multiplier) * substr)

        return "".join(stack)

