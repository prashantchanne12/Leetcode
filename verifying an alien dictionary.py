'''
In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographically in this alien language.

 

Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
Example 2:

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
Example 3:

Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).
 
'''

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # Look for first different character
        # If word A is prefix of word B, word B must be AFTER word A

        dict = { char: index for index, char in enumerate(order)}

        # check the pair of words
        for i in range(0, len(words) - 1):
            word1, word2 = words[i], words[i+1]

            for j in range(0, len(word1)):
                if j == len(word2): # word2 is bigger [he, hello]
                    return False

                # Look for first different character
                if word1[j] != word2[j]:
                    if dict[word1[j]] < dict[word2[j]]:
                        break
                    else:
                        return False

        return True

# [hey, hez, hex]