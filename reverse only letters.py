'''
Given a string S, return the "reversed" string where all characters that are not a letter stay in the same place, and all letters reverse their positions.

 

Example 1:

Input: "ab-cd"
Output: "dc-ba"
Example 2:

Input: "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"
Example 3:

Input: "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"
 
'''
import re
class Solution(object):
    def reverseOnlyLetters(self, S):
        list = ''.join(re.split(r'[^a-zA-Z\s]',S))[::-1]
        res = []
        index = 0
        for i in range(len(S)):
            if not S[i].isalpha():
                res.append(S[i])
            else:
                res.append(list[index])
                index += 1

        return ''.join(res)
        