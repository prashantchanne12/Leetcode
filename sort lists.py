'''
Given the head of a linked list, return the list after sorting it in ascending order.

Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?

 

Example 1:


Input: head = [4,2,1,3]
Output: [1,2,3,4]
Example 2:


Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]
Example 3:

Input: head = []
Output: []
 
'''

# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):

    def get_mid(self, head):
        slow = head
        fast = head.next

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        return slow

    def merge(self, l1, l2):
        current = node = ListNode(0)

        while l1 is not None and l2 is not None:

            if l1.val < l2.val:
                node.next = ListNode(l1.val)
                l1 = l1.next

            else:
                node.next = ListNode(l2.val)
                l2 = l2.next

            node = node.next

        while l1 is not None:
            node.next = ListNode(l1.val)
            l1 = l1.next
            node = node.next

        while l2 is not None:
            node.next = ListNode(l2.val)
            l2 = l2.next
            node = node.next

        return current.next

    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head is None or head.next is None:
            return head

        # split the nodes in two halfs
        left_list = head
        right_list = self.get_mid(head)

        temp = right_list.next
        right_list.next = None
        right_list = temp

        left_list = self.sortList(left_list)
        right_list = self.sortList(right_list)

        return self.merge(left_list, right_list)
