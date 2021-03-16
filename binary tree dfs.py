class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def printInorder(root):

    if root:

        printInorder(root.left)
        print(root.val, end=' ')
        printInorder(root.right)


def printPostOrder(root):

    if root:
        printPostOrder(root.left)
        printPostOrder(root.right)
        print(root.val, end=' ')


def printPreOrder(root):

    if root:
        print(root.val, end=' ')
        printPreOrder(root.left)
        printPreOrder(root.right)


def main():

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    print('\nInorder Traversal')
    printInorder(root)
    print()

    print('\nPostorder Traversal')
    printPostOrder(root)
    print()

    print('\nPreorder Traversal')
    printPreOrder(root)
    print()


main()
