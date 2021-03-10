'''
Find the minimum depth of a binary tree. The minimum depth is the number of nodes along the shortest path from the root node to the nearest leaf node.
'''

from collections import deque


class TreeNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


def find_minmum_depth(root):

    if not root:
        return 0

    q = deque()
    q.append(root)
    min_depth = 0

    while q:
        min_depth += 1
        levelSize = len(q)

        currentNode = q.popleft()

        # check if this is a leaf node
        if not currentNode.left and not currentNode.right:
            return min_depth

        if currentNode.left:
            q.append(currentNode.left)

        if currentNode.right:
            q.append(currentNode.right)


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)

    root.left.left = TreeNode(9)
    root.left.right = TreeNode(2)

    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)

    print(find_minmum_depth(root))


main()
