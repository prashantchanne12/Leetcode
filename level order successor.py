'''
Given a binary tree and a node, find the level order successor of the given node in the tree. The level order successor is the node that appears right after the given node in the level order traversal.
'''

from collections import deque


class TreeNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


def find_successor(root, key):

    if not root:
        return 0

    q = deque()
    q.append(root)

    while q:
        currentNode = q.popleft()

        if currentNode.left:
            q.append(currentNode.left)

        if currentNode.right:
            q.append(currentNode.right)

        if currentNode.val == key:
            break

    return q[0].val if q else None


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)

    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)

    root.right.right = TreeNode(5)

    print(find_successor(root, 12))


main()
