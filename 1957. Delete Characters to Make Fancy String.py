class Solution:
    def makeFancyString(self, s: str) -> str:
        result = []
        count = 1
        
        for i in range(len(s)):
            if i > 0 and s[i] == s[i - 1]:
                count += 1
            else:
                count = 1
            
            if count < 3:
                result.append(s[i])
        
        return ''.join(result)
