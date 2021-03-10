'''
Given a binary tree, populate an array to represent the averages of all of its levels.
'''

from collections import deque


class TreeNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


def traverse(root):

    res = []

    if not root:
        return res

    q = deque()
    q.append(root)

    while q:
        levelSize = len(q)
        currentLevel = []

        for _ in range(levelSize):

            currentNode = q.popleft()

            currentLevel.append(currentNode.val)

            if currentNode.left:
                q.append(currentNode.left)

            if currentNode.right:
                q.append(currentNode.right)

        res.append(sum(currentLevel)/levelSize)

    return res


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)

    root.left.left = TreeNode(9)
    root.left.right = TreeNode(2)

    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)

    print(traverse(root))


main()
