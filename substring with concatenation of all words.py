'''
Given a string and a list of words, find all the starting indices of substrings in the given string that are a concatenation of all the given words exactly once without any overlapping of words. It is given that all words are of the same length.

Example 1:

Input: String="catfoxcat", Words=["cat", "fox"]
Output: [0, 3]
Explanation: The two substring containing both the words are "catfox" & "foxcat".
Example 2:

Input: String="catcatfoxfox", Words=["cat", "fox"]
Output: [3]
Explanation: The only substring containing both the words is "catfox".
'''


class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if len(words) == 0 or len(words[0]) == 0:
            return []

        char_frequency = {}

        for word in words:
            if word not in char_frequency:
                char_frequency[word] = 0

            char_frequency[word] += 1

        res = []  # indices of substrings
        words_count = len(words)  # total words
        word_length = len(words[0])  # each word is of the same length

        for i in range(0, (len(s) - words_count * word_length)+1):

            # if the words are repeating
            # we are going to check if the words in words_seen has same count as the char_frequency
            words_seen = {}

            for j in range(0, words_count):

                next_word_index = i + j * word_length

                # add the word to the 'word_seen' map
                word = s[next_word_index: next_word_index + word_length]
                # break if the word is not in char frequency
                # that means word is not in 'words' and irrelavant
                if word not in char_frequency:
                    break

                # add the word to the 'word_seen' map
                if word not in words_seen:
                    words_seen[word] = 0

                words_seen[word] += 1

                # no need to process further if the word has higher frequency than required
                if words_seen[word] > char_frequency.get(word, 0):
                    break

                # j+1 == words_count that means we have found all the words
                # store index if we have found all the words
                if j+1 == words_count:
                    res.append(i)

        return res
