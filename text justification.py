'''
Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left-justified, and no extra space is inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.
 

Example 1:

Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Example 2:

Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be", because the last line must be left-justified instead of fully-justified.
Note that the second line is also left-justified because it contains only one word.
Example 3:

Input: words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]
 
'''

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        
        res = []
        current_line = []
        current_line_length = 0
        i = 0

        while i < len(words):
            # len(current_line) = spaces we need after each word
            # if there are 3 words = we are gonna need 3 spaces ex. This<spaces>is<space>an<space>[next word]
            if len(current_line) + current_line_length + len(words[i]) > maxWidth:
                
                extra_space = maxWidth - current_line_length

                spaces = extra_space // max(1, len(current_line) - 1)
                remainder = extra_space % max(1, len(current_line) - 1)

                for j in range(0, max(1, len(current_line) - 1)):
                    current_line[j] += " " * spaces

                    if remainder:
                        current_line[j] += " "
                        remainder -= 1

                res.append("".join(current_line))
                current_line = []
                current_line_length = 0


            current_line.append(words[i])
            current_line_length += len(words[i])
            i += 1


        last_line = " ".join(current_line)
        trailing_space = maxWidth - len(last_line)
        res.append(last_line + " " * trailing_space)
        return res 