'''
Given a binary tree, connect each node with its level order successor. The last node of each level should point to the first node of the next level.


'''

from __future__ import print_function
from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.next = None

    # tree travsersal using 'next' pointer
    def print_tree(self):

        print('Traversal using next pointer: ', end='')
        current = self

        while current:
            print(str(current.val) + ' ', end='')
            current = current.next


def connect_all_siblings(root):

    if root is None:
        return

    q = deque()
    q.append(root)

    while q:
        levelSize = len(q)

        for _ in range(levelSize):
            currentNode = q.popleft()
            nextNode = None

            if currentNode.left:
                q.append(currentNode.left)

            if currentNode.right:
                q.append(currentNode.right)

            if len(q) > 0:
                nextNode = q[0]
                currentNode.next = nextNode


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)

    root.left.left = TreeNode(9)

    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)

    connect_all_siblings(root)

    root.print_tree()


main()
