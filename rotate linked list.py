'''
Given the head of a linked list, rotate the list to the right by k places.

Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

Input: head = [0,1,2], k = 4
Output: [2,0,1
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


# Solution 1 - brute force

def rotate_linked_list(head, k):

    if k < 1 or head is None or head.next is None:
        return head

    first_node = head

    while k > 0:
        temp = first_node
        previous = None

        while temp is not None and temp.next is not None:
            previous = temp
            temp = temp.next

        last_node = temp
        previous.next = None

        last_node.next = first_node
        first_node = last_node

        k -= 1

    return first_node


head = None
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)
r = rotate_linked_list(head, 3)
print_list(r)

# Solution 2 - optimal


def rotate_linked_list_2(head, rotations):
    if rotations <= 0 or head is None or head.next is None:
        return head

    # find the length and the last node of the list
    last_node = head
    list_length = 1

    while last_node.next is not None:
        last_node = last_node.next
        list_length += 1

    # connect the last node with the head to make it circular list
    last_node.next = head

    # no need to do rotations more than the length of the list
    rotations = rotations % list_length

    skip_length = list_length - rotations

    last_node_of_rotated_list = head

    for i in range(skip_length - 1):
        last_node_of_rotated_list = last_node_of_rotated_list.next

    print(last_node_of_rotated_list.val)

    # 'last_node_of_rotated_list.next' is pointing to the sub-list of 'k' ending nodes
    head = last_node_of_rotated_list.next
    last_node_of_rotated_list.next = None

    return head


head = None
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)

r = rotate_linked_list_2(head, 3)
print_list(r)
