'''
Given a binary tree, connect each node with its level order successor. The last node of each level should point to a null node.
'''

from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.next = None

    # level order traversal using 'next' pointer
    def print_level_order(self):
        nextLevelRoot = self

        while nextLevelRoot:

            current = nextLevelRoot
            nextLevelRoot = None

            while current:

                print(str(current.val) + ' ', end='')

                if not nextLevelRoot:
                    if current.left:
                        nextLevelRoot = current.left
                    elif current.right:
                        nextLevelRoot = current.right

                current = current.next

            print()


def connect_level_order_siblings(root):

    if root is None:
        return

    q = deque()
    q.append(root)

    while q:
        prevNode = None
        levelSize = len(q)

        # connect all nodes of this level
        for _ in range(levelSize):
            currentNode = q.popleft()

            if prevNode:
                prevNode.next = currentNode

            prevNode = currentNode

        # insert the children of current node in the queue
        if currentNode.left:
            q.append(currentNode.left)
        if currentNode.right:
            q.append(currentNode.right)


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)

    root.left.left = TreeNode(9)

    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)

    connect_level_order_siblings(root)
    root.print_level_order()


main()
