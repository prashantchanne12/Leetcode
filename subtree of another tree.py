'''
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def isSubtree(self, s, t):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """

        if not s:
            return False

        # checks if same two trees
        def isSame(s, t):
            if not s and not t:
                return True
            if not s or not t:
                return False
            if s.val != t.val:
                return False
            return isSame(s.left, t.left) and isSame(s.right, t.right)

        # check current tree,subtreee combination
        if s.val == t.val and isSame(s, t):
            return True

        # test for all combinations
        left = self.isSubtree(s.left, t)
        right = self.isSubtree(s.right, t)

        return left or right
