'''
Given a binary tree, populate an array to represent its level-by-level traversal. You should populate the values of all nodes of each level from left to right in separate sub-arrays.
'''

from collections import deque


class TreeNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


def traverse(root):
    res = []

    if root is None:
        return res

    q = deque()
    q.append(root)

    while q:
        levelSize = len(q)
        currentLevel = []

        for _ in range(levelSize):
            currentNode = q.popleft()

            # add the node to current level
            currentLevel.append(currentNode.val)

            # insert the children of current node in the queue
            if currentNode.left:
                q.append(currentNode.left)

            if currentNode.right:
                q.append(currentNode.right)

        res.append(currentLevel)

    return res


def main():
    root = TreeNode(12)
    root.left = TreeNode(17)
    root.right = TreeNode(1)

    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)

    print(traverse(root))


main()
