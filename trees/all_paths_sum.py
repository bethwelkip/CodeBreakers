'''
Given a binary tree and a number ‘S’, find all paths from root-to-leaf such that the sum of all the node values of each path equals ‘S’.
'''


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left


def find_paths(root, sumS):
    all_paths = []

    def is_path(root, path, sum):
        if root is None and sum == sumS:
            return (True, path)
        if root is None:
            return (False, [])
        path.append(root.val)
        return [is_path(root.left, path, sum + root.val), is_path(root.right, path, sum+root.val)]

    def paths(root):
        if root is None:
            return
        left_path = is_path(root.left, [], 0)[0]
        right_path = is_path(root.right, [], 0)[1]
        if right_path[0]:
            all_paths.append(right_path)
        if left_path[0]:
            all_paths.append(left_path)

        paths(root.right)
        paths(root.left)

    return all_paths


def main():
    root = Node(12)
    root.left = Node(7)
    root.right = Node(1)
    root.left.left = Node(9)
    root.right.left = Node(10)
    root.left.right = Node(5)
    print('Has Path? ' + str(find_paths(root, 28)))
    print('Has Path? ' + str(find_paths(root, 23)))


main()
