'''
Given a binary tree where each node can only have a digit (0-9) value, each root-to-leaf path will represent a number. Find the total sum of all the numbers represented by all paths.
'''


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_sum_of_path_numbers(root):
    all_paths = []
    total = 0

    find_paths_recursive(root, [], all_paths)

    for num in all_paths:
        total += int(''.join(num))

    return total


def find_paths_recursive(current_node, current_path, all_paths):

    if current_node is None:
        return

    current_path.append(str(current_node.val))

    if current_node.left is None and current_node.right is None:
        all_paths.append(list(current_path))
    else:

        find_paths_recursive(current_node.left, current_path, all_paths)

        find_paths_recursive(current_node.right, current_path, all_paths)

    del current_path[-1]


def main():

    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)

    print(find_sum_of_path_numbers(root))


main()
