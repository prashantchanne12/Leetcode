'''
Given a binary tree, find the length of its diameter. The diameter of a tree is the number of nodes on the longest path between any two leaf nodes. The diameter of a tree may or may not pass through the root.

Note: You can always assume that there are at least two leaf nodes in the given tree.
'''


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left,
        self.right = right


class TreeDiameter:

    def __init__(self):
        self.treeDiameter = 0

    def find_diameter(self, root):
        self.calculate_height(root)
        return self.treeDiameter

    def calculate_height(self, currentNode):

        if currentNode is None:
            return 0

        leftTreeHeight = self.calculate_height(currentNode.left)

        rightTreeHeight = self.calculate_height(currentNode.right)

        # diameter at the current node will be equal to the height of left subtree + the height of right subtree + '1' for the current node
        diameter = leftTreeHeight + rightTreeHeight + 1

        # update the global tree diameter
        self.treeDiameter = max(self.treeDiameter, diameter)

        # height of the current node will be equal to the maximum of both the heightd of left or right subtrees + '1' for the current node
        return max(leftTreeHeight, rightTreeHeight) + 1


def main():
    treeDiameter = TreeDiameter()

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)

    print(treeDiameter.find_diameter(root))


main()
