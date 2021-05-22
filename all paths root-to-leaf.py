# Given a binary tree, return all root-to-leaf paths.


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def all_root_to_leaf(root):
    all_paths = []

    find_root_leaf_recursively(root, [], all_paths)

    return all_paths


def find_root_leaf_recursively(current_node, current_path, all_paths):

    if current_node is None:
        return

    current_path.append(current_node.val)

    if current_node.left is None and current_node.right is None:
        all_paths.append(list(current_path))
    else:

        find_root_leaf_recursively(current_node.left, current_path, all_paths)
        find_root_leaf_recursively(current_node.right, current_path, all_paths)

    del current_path[-1]


#     12
#    /  \
#   7    1
#  /    / \
# 4    10  5
# paths root-to-leaf
# 12 -> 7 -> 4
# 12 -> 1 -> 10
# 12 -> 1 -> 5


root = TreeNode(12)

root.left = TreeNode(7)
root.right = TreeNode(1)

root.left.left = TreeNode(4)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)

print(all_root_to_leaf(root))
