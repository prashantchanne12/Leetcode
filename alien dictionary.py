'''
There is a dictionary containing words from an alien language for which we don’t know the ordering of the characters. Write a method to find the correct order of characters in the alien language.

Example 1:

Input: Words: ["ba", "bc", "ac", "cab"]
Output: bac
Explanation: Given that the words are sorted lexicographically by the rules of the alien language, so
from the given words we can conclude the following ordering among its characters:
 
1. From "ba" and "bc", we can conclude that 'a' comes before 'c'.
2. From "bc" and "ac", we can conclude that 'b' comes before 'a'
 
From the above two points, we can conclude that the correct character order is: "bac"

Example 2:

Input: Words: ["cab", "aaa", "aab"]
Output: cab
Explanation: From the given words we can conclude the following ordering among its characters:
 
1. From "cab" and "aaa", we can conclude that 'c' comes before 'a'.
2. From "aaa" and "aab", we can conclude that 'a' comes before 'b'
 
From the above two points, we can conclude that the correct character order is: "cab"

Example 3:

Input: Words: ["ywx", "wz", "xww", "xz", "zyy", "zwz"]
Output: ywxz
Explanation: From the given words we can conclude the following ordering among its characters:
 
1. From "ywx" and "wz", we can conclude that 'y' comes before 'w'.
2. From "wz" and "xww", we can conclude that 'w' comes before 'x'.
3. From "xww" and "xz", we can conclude that 'w' comes before 'z'
4. From "xz" and "zyy", we can conclude that 'x' comes before 'z'
5. From "zyy" and "zwz", we can conclude that 'y' comes before 'w'
 
From the above five points, we can conclude that the correct character order is: "ywxz"
'''

from collections import deque


def alien_dictionary(words):

    if len(words) == 0:
        return ''

    # 1) Initialize the graph

    # count the incoming edges
    in_degrees = {}

    # adjacency list graph
    graph = {}

    for word in words:
        for char in word:
            in_degrees[char] = 0
            graph[char] = []

    # 2) Build the graph
    for i in range(0, len(words)-1):
        # find ordering of characters from adjacent words
        w1, w2 = words[i], words[i+1]

        for j in range(0, min(len(w1), len(w2))):
            parent, child = w1[j], w2[j]

            # if the two characters are differnet
            if parent != child:
                # put the child into the parent's list
                graph[parent].append(child)
                # increment in_degrees
                in_degrees[child] += 1

                # only the first different character between two words will help us finding the order
                break

    # 3) Find all sources i.e., all vertices wih 0 in-in_degrees
    sources = deque()
    for key in in_degrees:
        if in_degrees[key] == 0:
            sources.append(key)

    # 4) For each source, add it to the sorted_order and subtract 1 from all of its childrens in_degrees
    # if a child's in_degrees becomes zero, add it ti the source queue
    sorted_order = []

    while sources:
        node = sources.popleft()
        sorted_order.append(node)

        for child in graph[node]:
            in_degrees[child] -= 1

            if in_degrees[child] == 0:
                sources.append(child)

    if len(sorted_order) != len(in_degrees):
        return ''

    return ''.join(sorted_order)


print(alien_dictionary(['ba', 'bc', 'ac', 'cab']))
