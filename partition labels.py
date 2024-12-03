'''
You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.

Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

Return a list of integers representing the size of these parts.

 

Example 1:

Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.
Example 2:

Input: s = "eccbbbbdec"
Output: [10]
'''

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        if s == None or len(s) == 0:
            return None

        res = []
        # we are gonna use this array to find last index of each letter
        last_indices = [0]*26

        for i in range(0, len(s)):
            last_indices[ord(s[i]) - ord('a')] = i
            
        
        start = 0
        end = 0

        for i in range(0, len(s)):
            end = max(end, last_indices[ord(s[i]) - ord('a')])

            # am I the last letter
            if i == end:
                res.append(end - start + 1)
                start = end + 1

            
        
        return res