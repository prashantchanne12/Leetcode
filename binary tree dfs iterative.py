class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def printInorder(root):
    current = root
    stack = []

    while stack or current:

        if current:
            stack.append(current)
            current = current.left

        else:
            current = stack.pop()
            print(current.val, end=' ')
            current = current.right


def printPostOrder(root):
    current = root
    stack = []
    previous = None

    while stack or current:

        if current:
            stack.append(current)
            current = current.left

        else:
            current = stack[-1]

            if current.right == None or current.right == previous:
                print(current.val, end=' ')
                stack.pop()
                previous = current
                current = None
            else:
                current = current.right


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
