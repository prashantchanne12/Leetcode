'''
Given two integer arrays `inorder` and `postorder` where `inorder` is the inorder traversal of a binary tree and `postorder` is the postorder traversal of the same tree, construct and return *the binary tree*.

**Example 1:**

!https://assets.leetcode.com/uploads/2021/02/19/tree.jpg

```
Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]

```

**Example 2:**

```
Input: inorder = [-1], postorder = [-1]
Output: [-1]
```
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        if not inorder:
            return None

        root = TreeNode(postorder.pop())

        index = inorder.index(root.val)
    
        root.right = self.buildTree(inorder[index+1: ], postorder)
        root.left = self.buildTree(inorder[: index], postorder)

        return root
    

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {v:i for i, v in enumerate(inorder)}

        def helper(left, right):
            if left > right:
                return None

            root = TreeNode(postorder.pop())

            index = inorder_map[root.val]
        
            root.right = helper(index+1, right)
            root.left = helper(left, index-1)

            return root

        return helper(0, len(inorder) -1)