'''
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
'''

class Solution(object):
    def reverseList(self, head):
        prev = None
        current = head
        while current is not None:
            n = current.next
            current.next = prev
            prev = current
            current = n
        head = prev
        return head
            
        