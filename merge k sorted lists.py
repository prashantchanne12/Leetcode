'''
Given an array of ‘K’ sorted LinkedLists, merge them into one sorted list.

Example 1:

Input: L1=[2, 6, 8], L2=[3, 6, 7], L3=[1, 3, 4]
Output: [1, 2, 3, 3, 4, 6, 6, 7, 8]
Example 2:

Input: L1=[5, 8, 9], L2=[1, 7]
Output: [1, 5, 7, 8, 9]
'''

# Solution - 1

from heapq import *


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def display(listNode):
    while listNode is not None:
        print(listNode.val, end='->')
        listNode = listNode.next


def merge_lists(lists):
    result_head = None

    min_heap = []

    for listNode in lists:
        while listNode is not None:
            heappush(min_heap, (listNode.val))
            listNode = listNode.next

    temp = None

    while min_heap:

        if result_head is None:
            val = heappop(min_heap)
            result_head = ListNode(val)
            temp = result_head

        val = heappop(min_heap)
        result_head.next = ListNode(val)
        result_head = result_head.next

    return temp


l1 = ListNode(2)
l1.next = ListNode(6)
l1.next.next = ListNode(8)

l2 = ListNode(3)
l2.next = ListNode(6)
l2.next.next = ListNode(7)

l3 = ListNode(1)
l3.next = ListNode(3)
l3.next.next = ListNode(4)

listNode = merge_lists([l1, l2, l3])
display(listNode)


# Solution - 2


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __lt__(self, other):
        return self.val < other.val


def display(listNode):
    while listNode is not None:
        print(listNode.val, end='->')
        listNode = listNode.next


def merge_lists(lists):

    min_heap = []

    # put the root of each list in the min heap
    for root in lists:
        if root is not None:
            heappush(min_heap, root)

    # take the smallest(top) element from the min_heap and add it to the result
    # if the top element has a next element add it to the heap

    result_head = None
    result_tail = None

    while min_heap:

        node = heappop(min_heap)
        if result_head is None:
            result_head = result_tail = node
        else:
            result_tail.next = node
            result_tail = result_tail.next

        if node.next:
            heappush(min_heap, node.next)

    return result_head


l1 = ListNode(2)
l1.next = ListNode(6)
l1.next.next = ListNode(8)

l2 = ListNode(3)
l2.next = ListNode(6)
l2.next.next = ListNode(7)

l3 = ListNode(1)
l3.next = ListNode(3)
l3.next.next = ListNode(4)

listNode = merge_lists([l1, l2, l3])
display(listNode)
