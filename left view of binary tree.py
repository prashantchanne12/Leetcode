'''
Given a binary tree, return an array containing nodes in its left view. The left view of a binary tree is the set of nodes visible when the tree is seen from the left side.
'''

from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def tree_left_view(root):
    res = []

    if root is None:
        return res

    q = deque()
    q.append(root)

    while q:
        levelSize = len(q)

        for i in range(0, levelSize):
            currentNode = q.popleft()

            # if it is the first node of this level, add it to the result
            if i == 0:
                res.append(currentNode.val)

            # insert the children of the current node in the queue
            if currentNode.left:
                q.append(currentNode.left)
            if currentNode.right:
                q.append(currentNode.right)

    return res


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)

    root.left.left = TreeNode(9)

    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)

    root.left.left.left = TreeNode(3)

    res = tree_left_view(root)
    print(res)


main()
