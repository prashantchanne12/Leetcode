'''
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]
Example 2:

Input: head = [5], left = 1, right = 1
Output: [5]
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


def reverse_sub_list(head, p, q):
    if p == q:
        return head

    # after skipping 'p-1' nodes, current will point to 'p'th Node
    # and previous will point to the node before 'p'
    current = head
    previous = None
    i = 0

    while current is not None and i < p - 1:
        previous = current
        current = current.next
        i += 1

    # we are intrested in three parts of the LinkedList
    # 1. The part before 'p'
    # 2. The part between 'p' and 'q'
    # 3. The part after q

    last_node_of_first_part = previous

    # after reversing the LinkedList 'current' will become the last node of the sub-list
    last_node_of_sub_list = current

    i = 0
    previous = None

    # reverse nodes between 'p' and 'q'
    while current is not None and i < q - p + 1:
        next = current.next
        current.next = previous

        previous = current
        current = next

        i += 1

    # connect with the first
    if last_node_of_first_part is not None:
        # 'previous' is now the first node of the sub-list
        last_node_of_first_part.next = previous
    else:
        # this means p == 1 i.e., we are changing the first node (head) of the LinkedList
        head = previous

    # connect with the last part
    last_node_of_sub_list.next = current

    return head


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

head = reverse_sub_list(head, 2, 4)
print_list(head)
