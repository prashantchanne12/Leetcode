'''
Reverse the first ‘k’ elements of a given LinkedList.
'''


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def print_list(head):
    temp = head

    while temp is not None:
        print(temp.val, end='->')
        temp = temp.next


def reverse_first_k_elements(head, k):

    if k == 1:
        return head

    current = head
    previous = None

    # after reversing the 'current' will be the last node in the sublist
    last_node_of_sub_list = current

    i = 0

    # reverse a linked list from 0 to k
    while current is not None and i < k:
        next = current.next
        current.next = previous

        previous = current
        current = next

        i += 1

    # point head to previous which is the first node
    head = previous

    last_node_of_sub_list.next = current

    return head


head = None
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

head = reverse_first_k_elements(head, 3)
print_list(head)
