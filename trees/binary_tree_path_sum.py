'''
Given a binary tree and a number ‘S’, find if the tree has a path from root-to-leaf such that the sum of all the node values of that path equals ‘S’.
'''

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left


def has_path(root, sumS):
    def recurse(root, sum):
        if root is None and sum == sumS:
            return True
        if root is None:
            return False

        return recurse(root.left, sum + root.val) or recurse(root.right, sum+root.val)

    return recurse(root, 0)


def main():
    root = Node(12)
    root.left = Node(7)
    root.right = Node(1)
    root.left.left = Node(9)
    root.right.left = Node(10)
    root.left.right = Node(5)
    print('Has Path? ' + str(has_path(root, 28)))
    print('Has Path? ' + str(has_path(root, 23)))


main()
