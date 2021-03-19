'''
Given a binary tree and a number sequence, find if the sequence is present as a root-to-leaf path in the given tree.
'''


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def path_with_given_sequence(root, sequence):
    return find_numbers(root, [], sequence)


def find_numbers(current_node, path, sequence):

    if current_node is None:
        return 0

    # no need of further traversing if sequence dosen't match at early stage
    if sequence[len(path)] != current_node.val:
        return False

    path.append(current_node.val)

    if current_node.left is None and current_node.right is None:
        return path == sequence

    # traverse the left and the right sub-tree
    return find_numbers(current_node.left, path, sequence) or find_numbers(current_node.right, path, sequence)


def main():

    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)

    print(path_with_given_sequence(root, [1, 0, 5]))


main()
