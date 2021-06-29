'''
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
Example 2:


Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
Example 3:

Input: head = [1,2,3,4,5], k = 1
Output: [1,2,3,4,5]
Example 4:

Input: head = [1], k = 1
Output: [1]
'''

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:

        prev = None
        current = head

        while True:

            last_node_of_prev_part = prev
            last_node_of_sub_list = current

            prev = None
            i = 0

            temp = current

            count = 0
            while temp is not None:
                temp = temp.next
                count += 1

            if count < k:
                return head

            while current and i < k:

                next = current.next
                current.next = prev

                prev = current
                current = next

                i += 1

            if last_node_of_prev_part is not None:
                last_node_of_prev_part.next = prev
            else:
                head = prev

            last_node_of_sub_list.next = current

            if current is None:
                break

            prev = last_node_of_sub_list

        return head
