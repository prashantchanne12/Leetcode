'''
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
'''

# Solution 1


class Solution(object):
    def reverseList(self, head):
        prev = None
        current = head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        head = prev
        return head

# Solution 2


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def print_list(head):

    while head is not None:
        print(head.val, end='->')
        head = head.next


def reverse_linked_list(current):

    previous = None
    current = head
    next = None

    while current is not None:
        next = current.next  # temporary store the next node
        current.next = previous  # reverse the current node

        # before we move to the next node, point previous node to the current node
        previous = current
        current = next  # move on the next node

    return previous


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

reversed = reverse_linked_list(head)
print_list(reversed)
