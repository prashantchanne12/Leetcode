'''
Problem 1: Given the head of a LinkedList with a cycle, find the length of the cycle
'''


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def has_cycle(head):
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next

        if fast == slow:  # found the cycle
            return cycle_length(slow)

    return False


def cycle_length(slow):
    current = slow
    count = 0

    while True:
        current = current.next
        count += 1

        if current == slow:
            break

    return count

def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    print(has_cycle(head))

    head.next.next.next.next.next.next = head.next.next
    print(has_cycle(head))


main()
