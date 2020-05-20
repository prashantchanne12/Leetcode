'''
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        temp = head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        
        itr = (count - n)-1
        current = temp = head

        while itr and temp.next:
            temp = temp.next
            itr -= 1
            
        if temp.next:
            temp.next = temp.next.next
        else:
            return current.next
        
        return current
            
            
        