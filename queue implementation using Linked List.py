'''
QUEUE IMPLEMENATATION USING LINKED LIST
'''

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
        
class LinkedList:
    def __init__(self):
        self.head = None
    
    # ENQUEUE
    def enqueue(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        
        temp = self.head
        
        while temp.next:
            temp = temp.next
            
        temp.next = Node(data, None)
        
    # DEQUEUE
    def dequeue(self):
        dq_item = self.head.data
        self.head = self.head.next
        return dq_item
        
    # TOP OF THE QUEUE
    def toq(self):
        return self.head.data
    
    # DISPLAY
    def display(self):
        temp = self.head
        
        while temp:
            print(temp.data,end='->')
            temp = temp.next

l = LinkedList()
# ENQUEUE
l.enqueue(10)
l.enqueue(20)
l.enqueue(30)
l.enqueue(40)

l.display()
# 10->20->30->40->

# DEQUEUE
l.dequeue()
# 10

# TOP OF THE QUEUE
l.toq()
# 20

# DISPLAY
l.display()
# 20->30->40->

