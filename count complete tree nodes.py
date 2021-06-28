'''
Given the root of a complete binary tree, return the number of the nodes in the tree.

According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Design an algorithm that runs in less than O(n) time complexity.

 

Example 1:


Input: root = [1,2,3,4,5,6]
Output: 6
Example 2:

Input: root = []
Output: 0
Example 3:

Input: root = [1]
Output: 1
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if root is None:
            return 0

        left_levels = 0
        left_depth = root

        while left_depth is not None:
            left_levels += 1
            left_depth = left_depth.left

        right_levels = 0
        right_depth = root

        while right_depth is not None:
            right_levels += 1
            right_depth = right_depth.right

        if left_levels == right_levels:
            return pow(2, left_levels) - 1

        return self.countNodes(root.left) + self.countNodes(root.right) + 1
