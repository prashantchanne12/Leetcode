'''
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

 

Example 1:


Input: head = [1,2,3,4]
Output: [1,4,2,3]
Example 2:


Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def reverse(self, head):

        prev = None

        while head is not None:

            next = head.next
            head.next = prev

            prev = head
            head = next

        return prev

    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """

        if head is None or head.next is None:
            return

        current = head
        slow = head
        fast = head

        while fast is not None and fast.next is not None:

            slow = slow.next
            fast = fast.next.next

        second_half = self.reverse(slow)
        first_half = head

        while first_half is not None and second_half is not None:

            temp = first_half.next
            first_half.next = second_half
            first_half = temp

            temp = second_half.next
            second_half.next = first_half
            second_half = temp

        if first_half is not None:
            first_half.next = None

        return current
