'''
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Notice that you should not modify the linked list.

 

Example 1:


Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.
Example 2:


Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.
Example 3:


Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

    def find_start(self, slow, temp):
        pointer_1 = slow
        pointer_2 = temp

        while pointer_1 != pointer_2:
            pointer_1 = pointer_1.next
            pointer_2 = pointer_2.next

        return pointer_1

    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        temp = head
        fast = head
        slow = head

        while fast is not None and fast.next is not None:

            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return self.find_start(slow, temp)

        return None
