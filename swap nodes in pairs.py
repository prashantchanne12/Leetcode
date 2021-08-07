'''
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

 

Example 1:


Input: head = [1,2,3,4]
Output: [2,1,4,3]
Example 2:

Input: head = []
Output: []
Example 3:

Input: head = [1]
Output: [1]
'''

# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node = ListNode(0, head)

        prev = node
        current = head

        while current is not None and current.next is not None:

            # save pointers
            next_pair = current.next.next
            second = current.next

            # reverse the pairs
            second.next = current
            current.next = next_pair
            prev.next = second

            # update the pointers
            prev = current
            current = next_pair

        return node.next
