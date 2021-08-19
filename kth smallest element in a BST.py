'''
Given the root of a binary search tree, and an integer k, return the kth (1-indexed) smallest element in the tree.

 

Example 1:


Input: root = [3,1,4,null,2], k = 1
Output: 1
Example 2:


Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
'''

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """

        def inorder(root, res):

            if root is None:
                return

            inorder(root.left, res)
            res.append(root.val)
            inorder(root.right, res)

        res = []
        inorder(root, res)
        return res[k-1]


# Solution - 2
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """

        n = 0
        stack = []
        current = root

        while current or stack:

            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            n += 1

            if n == k:
                return current.val

            current = current.right
