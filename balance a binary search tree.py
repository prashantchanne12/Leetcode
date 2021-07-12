'''
Given a binary search tree, return a balanced binary search tree with the same node values.

A binary search tree is balanced if and only if the depth of the two subtrees of every node never differ by more than 1.

If there is more than one answer, return any of them.

Example 1:

Input: root = [1,null,2,null,3,null,4,null,null]
Output: [2,1,3,null,null,null,4]
Explanation: This is not the only correct answer, [3,1,4,null,2,null,null] is also correct.
 
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def __init__(self):
        self.arr = []

    def inorder(self, root):

        if root is not None:
            self.inorder(root.left)
            self.arr.append(root)
            self.inorder(root.right)

    def balanceBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        self.inorder(root)

        def solve(left, right):

            if left > right:
                return

            mid = (left + right) // 2

            node = self.arr[mid]

            node.left = solve(left, mid-1)
            node.right = solve(mid+1, right)

            return node

        left = 0
        right = len(self.arr) - 1

        return solve(left, right)
