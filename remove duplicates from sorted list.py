'''
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

Example 1:

Input: head = [1,1,2]
Output: [1,2]
Example 2:

Input: head = [1,1,2,3,3]
Output: [1,2,3]
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 1 -> 1 -> 1 -> None


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        current = head

        if head is None or head.next is None:
            return head

        while head is not None:

            while head is not None and head.next is not None and head.val == head.next.val:

                next = head.next.next
                head.next = next

            head = head.next

        return current
