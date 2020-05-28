'''
STACK IMPLEMENTATION USING LINKED LIST
'''

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
        
class LinkedList:
    def __init__(self):
        self.head = None
    
    # PUSH
    def push(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        
        new_node = Node(data, None)
        new_node.next = self.head
        self.head = new_node
        
    # POP
    def pop(self):
        pop_item = self.head.data
        self.head = self.head.next
        return pop_item
        
    # TOP OF THE STACK
    def tos(self):
        return self.head.data
    
    # DISPLAY
    def display(self):
        temp = self.head
        
        while temp:
            print(temp.data,end='->')
            temp = temp.next

l = LinkedList()
# PUSH
l.push(10)
l.push(11)
l.push(12)
l.push(13)
l.display()

# 13->12->11->10->

# TOP OF THE STACK
l.tos()

# POP
l.pop()

# DISPLAY
l.display()
# 12->11->10->

        