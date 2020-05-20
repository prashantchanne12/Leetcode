'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):    
    def addTwoNumbers(self, l1, l2):
        # pointer to 1st and 2nd linked list
        p1 = l1
        p2 = l2
        
        # to store carry if generated
        carry = 0
        
        # initialize linked list with 0 so we don't have to 
        # check if linked list is empty or not in while loop
        # return head.next to avoid 0
        head = current = ListNode(0)
        
        while p1 or p2 or carry:
            currentVal = carry
            
            currentVal += 0 if p1 is None else p1.val
            currentVal += 0 if p2 is None else p2.val
            
            if currentVal >= 10:
                currentVal -= 10
                carry = 1
            else:
                carry = 0
                
            current.next = ListNode(currentVal)
            current = current.next
            
            if p1 is None and p2 is None:
                break
            elif p1 is None:
                p2 = p2.next
            elif p2 is None:
                p1 = p1.next
            else:
                p1 = p1.next
                p2 = p2.next
            
        return head.next
            
            
        