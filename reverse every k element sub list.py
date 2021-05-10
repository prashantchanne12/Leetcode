'''
Given the head of a LinkedList and a number ‘k’, reverse every ‘k’ sized sub-list starting from the head.

If, in the end, you are left with a sub-list with less than ‘k’ elements, reverse it too.

Input: 1->2->3->4->5->6->7->8->null, k = 3
Output: 3->2->1->6->5->4->8->7->null

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


def reverse_every_k_elements(head, k):
    if k <= 1 or head is None:
        return head

    current = head
    previous = None

    while True:

        # 3->2->1 '1' is the previous
        last_node_of_first_part = previous

        # as we are reversing linked list
        # current will become last node of sub list eventually
        last_node_of_sub_list = current

        i = 0

        # 1->2->3 = 3->2->1
        while current is not None and i < k:
            next = current.next
            current.next = previous

            previous = current
            current = next

            i += 1

        if last_node_of_first_part is not None:
            last_node_of_first_part.next = previous
        else:
            head = previous

        # 3->2->1 -> 4->5->6->7->8
        last_node_of_sub_list.next = current

        if current is None:
            break

        # 3->2->1 '1' is last node of sublist and previous node
        previous = last_node_of_sub_list

    return head


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)
head.next.next.next.next.next.next = Node(7)
head.next.next.next.next.next.next.next = Node(8)

head = reverse_every_k_elements(head, 3)
print_list(head)
