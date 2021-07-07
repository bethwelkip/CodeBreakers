'''
Explores tree traversals and problems associated with tree traversals

Outline:
    1. common traversals:
        a. pre-order traversal
            - process root node, then left childnode and its right childnode
            - use stack(LIFO) coz its possible to get the right subtrees in reverse order
        b. in-order traversal
        c. post-order traversal
        d. level-order traversal

    2. beginner problems solved by traversal
        a. Give an algorithm for finding the maximum element in a binary tree
            - with recursion(can use recursive postorder or any orders)
            - without recursion(uses level-order)
        b. Give an algorithm for finding the number of full nodes
        c. 
        d. 
        e.

    3. intermediate problems solved by traversal
        a. 
        b. 
        c.
        d. 
        e.

    4. advanced problems solved by traversal
        a.
        b.
        c.
        d.
        e.

'''

# node class to represent a tree node. 
class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.right = right
        self.left = left


# Pre-order traversal(Root, Left, Right)
def recursive_preorder(root, result):
    if not root:
        return

    result.append(root.val)
    recursive_preorder(root.left, result)
    recursive_preorder(root.right, result)
    # note the order: (1) process root node (2) explore left subtree (3) explore right subtree

def iterative_preorder(root):
    if not root:
        return
    stack = [] # LIFO stack determines how we traverse the tree(preorder)
    result = [] # where we will store our preorder 
    stack.append(root)
    while stack:
        node = stack.pop()
        result.append(node.val)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return result



# In-order traversal (Left, Root, Right)
def recursive_inorder(root, result):
    if not root:
        return
    recursive_inorder(root.left, result) # explore left subtree
    result.append(root.val) # process root node. Here we store the values but you can do anything you need to do to the node
    recursive_inorder(root.right, result)

def iterative_inorder(root):
    if not root:
        return
    stack = []
    result = []
    node = root
    while stack or node:
        if node: # if we have a node, keep going to the left subtrees
            stack.append(node)
            node = node.left
        else: # otherwise, process the root node and go to the right subtree
            node = stack.pop()
            result.append(node.val)
            node = node.right
    return result

# Post-order traversal(Left, Right, Root)

def recursive_postorder(root, result):
    if not root:
        return
    recursive_postorder(root.left, result)
    recursive_postorder(root.right, result)
    result.append(root.val) # process root node

def iterative_postorder(root): # need to do more to understand this
    if not root:
        return 
    stack = []
    result = []
    visited = set()
    node = root
    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            if node.right and not node.right in visited:
                stack.append(node)
                node = node.right
            else:
                result.append(node.val)
                visited.add(node)
                node = Node
    return result
# all traversals have:
#                time complexity 0(n), space complexity 0(n)
from collections import deque
def iterative_levelorder(root): # i doubt a recursive one is possible
    if not root:
        return
    que = deque()
    result = []
    que.append(root)
    while len(que)>0:
        node = que.popleft()
        if root.left:
            que.append(root.left)
        if root.right:
            que.append(root.right)
        result.append(node.val)
    return result

# 2
# Give an algorithm for finding the maximum element in a binary tree

# a. with recursion
def find_max(root):
    if not root:
        return
    global_max = float('-inf')

    def dfs(root):
        if root:
            return
        if root.val > global_max:
            global_max = root.val
        dfs(root.left)
        dfs(root.right)
    dfs(root)
    return global_max
    #time 0(n), space 0(n)
#  not sure if this will work
Global_Max = float('-inf')
def find_max_2(root):
    if not root:
        return Global_Max
    if root.val > Global_Max:
        Global_Max = root.val
    find_max_2(root.right)
    find_max_2(root.left)
    return Global_Max

# b. without recursion
def find_max(root):
    que = deque()
    global_max = float('-inf')
    que.append(root)
    while len(que)> 0:
        node = que.popleft()
        if node.val > global_max:
            global_max = node.val
        if node.left:
            que.append(node.left)
        if node.right:
            que.append(node.right)
    return global_max

def find_full_nodes(root):
    que = deque()
    que.append(root)
    count = 0
    while len(que) >0:
        node = que.popleft()
        if node.left and node.right:
            count += 1
        if node.left:
            que.append(node.left)
        if node.right:
            que.append(node.right)
    return count

def find_half_nodes(root):
    count = 0
    que = deque()
    que.append(root)
    while len(que) > 0:
        node = que.popleft()
        if all([node.left, not node.right]) or all([node.right, not node.left]):
            count += 2
        if node.left:
            que.append(node.left)
        if node.right:
            que.append(node.right)

    return count

# Given two binary trees, return true if they are structurally identical

def identical_trees(root1, root2): # will have to test this a lot
    if not root1 and not root2:
        return True
    if not root1 or not root2:
        return False
    if root1.val != root2.val:
        return False
    return identical_trees(root1.left, root2.left) and identical_trees(root1.right, root2.right)





def tree_diameter(root):
    pass


            
