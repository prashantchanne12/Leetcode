'''
Design a class that simulates a Stack data structure, implementing the following two operations:

push(int num): Pushes the number ‘num’ on the stack.
pop(): Returns the most frequent number in the stack. If there is a tie, return the number which was pushed later.
Example:

After following push operations: push(1), push(2), push(3), push(2), push(1), push(2), push(5)
 
1. pop() should return 2, as it is the most frequent number
2. Next pop() should return 1
3. Next pop() should return 2
'''

from heapq import *


class FreqStack(object):

    def __init__(self):
        self.dict = {}
        self.max_heap = []
        self.index = 0

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """

        if val not in self.dict:
            self.dict[val] = 0

        self.dict[val] += 1

        heappush(self.max_heap, (-self.dict[val], -self.index, val))

        self.index += 1

    def pop(self):
        """
        :rtype: int
        """
        val = heappop(self.max_heap)[2]

        self.dict[val] -= 1

        return val

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
