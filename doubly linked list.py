class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev
    
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def insert_at_beg(self,data):
        if self.head == None:
                node = Node(data, None, None)
                self.head = node
                self.tail = node
        else:
            node = Node(data)
            self.head.prev = node
            node.next = self.head
            node.prev = None
            self.head = node
                
    def insert_at_end(self,data):
        pass
                
    def display_forward(self):
        if self.head == None:
            print('List is empty')
            return
        
        temp = self.head
        
        while temp:
            print(temp.data, end=' -> ')
            temp = temp.next
            
    def display_backwords(self):
        if self.head == None:
            print('List is empty')
            return
        
        temp = self.tail
        
        while temp:
            print(temp.data, end=' -> ')
            temp = temp.prev
            
l = LinkedList()
l.insert_at_beg(10)
l.insert_at_beg(20)
l.insert_at_beg(30)
l.display_forward()
print()
l.display_backwords()