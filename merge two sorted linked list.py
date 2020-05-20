'''
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        # pointers pointing to the l1 and l2
        p1 = l1
        p2 = l2
        
        head = current = ListNode(0)
        
        while p1 or p2:        
            if p1 is not None and p2 is not None:
                if p1.val < p2.val:
                    current.next = ListNode(p1.val)
                    current = current.next
                    p1 = p1.next
                else:
                    current.next = ListNode(p2.val)
                    current = current.next
                    p2 = p2.next
            elif p1 is None:
                current.next = ListNode(p2.val)
                current = current.next
                p2 = p2.next
            elif p2 is None:
                current.next = ListNode(p1.val)
                current = current.next
                p1 = p1.next
                
                
        return head.next
            
            
        
        
        