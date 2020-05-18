class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    
class LinkedList:
    def __init__(self):
        self.head = None
        
    def insert_at_beg(self, data):
        node = Node(data, self.head)
        self.head = node
        
    def insert_at_end(self, data):
        if self.head == None:
            self.head = Node(data, None)
            return
        
        temp = self.head
        
        while temp.next:
            temp = temp.next
        
        temp.next = Node(data, None)
        
    def insert_at_index(self, index, data):
        if index < 0 or index > self.getLength():
            raise Exception('Invalid Index')
            return
    
        count = 0
        temp = self.head
        
        while temp:
            if count == index-1:
                node = Node(data, temp.next)
                temp.next = node
                break
            temp = temp.next
            count = count+1
            
    def insert_after_data(self, data_after, data_to_insert):
        temp = self.head
        
        while temp.data != data_after:
            temp = temp.next
            
        node = Node(data_to_insert, temp.next)
        temp.next = node
        
    def remove_at_beg(self):
        if self.head == None:
            print('List is empty')
            return
    
        self.head = self.head.next
    
    def remove_at_end(self):
        if self.head == None:
            print('List is empty')
            return 
        temp = self.head
        prev = None
        while temp.next:
            prev = temp
            temp = temp.next
            
        prev.next = None
            
    
    def remove_at_index(self, index):
        if index<0 or index> self.getLength():
            raise Exception('Invalid Index')
            return
        temp = self.head
        count = 0
        
        while count == index-1:
            temp = temp.next
            
        temp.next = temp.next.next
    
    def remove_by_data(self, data):
        temp = self.head
        prev = None
        
        while temp.data != data and temp.next!=None:
            prev = temp
            temp = temp.next
            
        prev.next = prev.next.next
            
        
    def getLength(self):
        count = 0
        temp = self.head
        
        while temp:
            count = count+1
            temp = temp.next
        
        return count
    
        
    def display(self):
        if self.head == None:
            print('List is empty')
            return
        
        temp = self.head
        
        while temp:
            print(temp.data, end=' -> ')
            temp = temp.next
    
    
l = LinkedList()
l.insert_at_end(10)
l.insert_at_end(20)
l.insert_at_end(30)
l.insert_at_end(40)
l.insert_at_index(2,89)
l.insert_after_data(30,35)
l.insert_after_data(30,34)
l.remove_at_beg()
l.remove_at_end()
l.remove_at_index(2)
l.remove_by_data(3)

l.display()