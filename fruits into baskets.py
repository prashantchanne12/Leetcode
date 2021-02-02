'''
Given an array of characters where each character represents a fruit tree, you are given two baskets and your goal is to put maximum number of fruits in each basket. The only restriction is that each basket can have only one type of fruit.

You can start with any tree, but once you have started you can’t skip a tree. You will pick one fruit from each tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.

Write a function to return the maximum number of fruits in both the baskets.

Example 1:

Input: Fruit=['A', 'B', 'C', 'A', 'C']
Output: 3
Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']
Example 2:

Input: Fruit=['A', 'B', 'C', 'B', 'B', 'C']
Output: 5
Explanation: We can put 3 'B' in one basket and two 'C' in the other basket. 
This can be done if we start with the second letter: ['B', 'C', 'B', 'B', 'C']
'''


def fruits_into_baskets(fruits):

    windowStart = 0
    max_length = 0
    dict = {}

    for windowEnd in range(0, len(fruits)):

        right_char = fruits[windowEnd]

        if right_char not in dict:
            dict[right_char] = 0

        dict[right_char] += 1

        while len(dict) > 2:
            # shrink the window
            left_char = fruits[windowStart]

            # remove left_char from dictionary
            dict[left_char] -= 1

            if dict[left_char] == 0:
                del dict[left_char]

            windowStart += 1

        max_length = max(max_length, (windowEnd-windowStart+1))

    return max_length


print(fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C']))
