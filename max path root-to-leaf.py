class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_max_root_to_leaf(root):
    all_paths = []
    find_max_root_to_leaf_recursively(root, 0, all_paths)
    return max(all_paths)


def find_max_root_to_leaf_recursively(root, current_sum, all_paths):

    if root is None:
        return

    current_sum += root.val

    if root.left is None and root.right is None:
        all_paths.append(current_sum)
    else:

        find_max_root_to_leaf_recursively(root.left, current_sum, all_paths)
        find_max_root_to_leaf_recursively(root.right, current_sum, all_paths)

    current_sum -= root.val

#       12
#      /  \
#     7    1
#    /    / \
#   4    10  5
#  /
# 10
# paths & sum
# 12 -> 7 -> 4 = 23
# 12 -> 1 -> 10 = 23
# 12 -> 1 -> 5 = 18
# 12 -> 7 -> 4 -> 10 = 33
# max_sum = 33


root = TreeNode(12)

root.left = TreeNode(7)
root.right = TreeNode(1)

root.left.left = TreeNode(4)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)

root.left.left.left = TreeNode(10)


print(find_max_root_to_leaf(root))
