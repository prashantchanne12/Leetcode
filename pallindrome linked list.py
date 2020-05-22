'''
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?
'''

# Solution 1

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):  
        res = []
        while head: 
            res.append(head.val)
            head = head.next
        return res == res[::-1]

# Solution 2 - Using Stack

class Solution(object):
    def isPalindrome(self, head):  
        res = []
        p = head
        while p: 
            res.append(p.val)
            p = p.next

        p = head
        while p:
            if p.val != res.pop():
                return False
            p = p.next

        return True
