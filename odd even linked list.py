'''
Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]

'''


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def print_list(head):
    temp = head

    while temp is None:
        print(temp.val, end='->')
        temp = temp.next


def odd_even_linked_list(head):
    if head is None or head.next is None:
        return head

    odd = head
    even = head.next
    even_head = even

    while even is not None and even.next is not None:

        odd.next = even.next
        odd = odd.next

        even.next = odd.next
        even = even.next

    odd.next = even_head

    return head


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

head = odd_even_linked_list(head)
print_list(head)
