'''
Given the head of a LinkedList and a number ‘k’, reverse every alternating ‘k’ sized sub-list starting from the head.

If, in the end, you are left with a sub-list with less than ‘k’ elements, reverse it too.

Input : 1->2->3->4->5->6->7->8->null k = 2
Output : 2->1->3->4->6->5->7->8->null 
'''

# solution 1


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def print_list(head):
    temp = head

    while temp is not None:
        print(temp.val, end='->')
        temp = temp.next

# Solution 1


def reverse_alternate_k_elements_2(head, k):
    if k <= 1 or head is None:
        return head

    current = head
    previous = None

    while True:

        last_node_of_first_part = previous
        last_node_of_sub_list = current

        i = 0

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

        last_node_of_sub_list.next = current

        if current is None:
            break

        previous = last_node_of_sub_list

        # skip k nodes
        i = 0
        while current is not None and i < k:
            previous = current
            current = current.next

            if current is None:
                break

            i += 1

        return head


head = None
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)
head.next.next.next.next.next.next = Node(7)
head.next.next.next.next.next.next.next = Node(8)

r = reverse_alternate_k_elements_2(head, 2)
print_list(r)

# Solution 2


def reverse_alternate_k_elements(head, k):
    if k <= 1 or head is None:
        return head

    current = head
    previous = None
    skip = 2

    while True:

        last_node_of_first_part = previous
        last_node_of_sub_list = current

        i = 0

        while current is not None and i < k and skip == 2:
            next = current.next
            current.next = previous

            previous = current
            current = next

            i += 1

        if skip == 2:
            if last_node_of_first_part is not None:
                last_node_of_first_part.next = previous
            else:
                head = previous

            last_node_of_sub_list.next = current
            previous = last_node_of_sub_list

        else:
            previous = current
            current = current.next

        if current is None:
            break

        skip -= 1
        if skip < 0:
            skip = 2

    return head


head = None
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)
head.next.next.next.next.next.next = Node(7)
head.next.next.next.next.next.next.next = Node(8)

head = reverse_alternate_k_elements(head, 2)
print_list(head)
