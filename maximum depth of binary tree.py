'''
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2
Example 3:

Input: root = []
Output: 0
Example 4:

Input: root = [0]
Output: 1
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):

    def __init__(self):
        self.max_depth = 0

    def dfs(self, root, depth):

        if root is None:
            return

        self.max_depth = max(self.max_depth, depth)

        if root.left:
            self.dfs(root.left, depth + 1)

        if root.right:
            self.dfs(root.right, depth + 1)

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        self.dfs(root, 1)

        return self.max_depth
