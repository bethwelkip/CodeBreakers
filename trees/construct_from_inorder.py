'''
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.
#                  r l                     ls   rs---->
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
#                                             i
Output: [3,9,20,null,null,15,7]


Input: preorder = [-1], inorder = [-1]
Output: [-1]


'''
from collections import deque 
class TreeNode:
    def __init__(self, val, left=None, right = None):
        self.val = val
        self.right = right
        self.left = left
        
def buildTree(preorder, inorder):
    if len(inorder) == 0:
        return
    
    val = preorder[0]
    i = 0
    while i < len(inorder):
        if inorder[i] == val:
            break
        i += 1
    left = buildTree(preorder[1:i+1], inorder[:i])
    right = buildTree(preorder[i+1:], inorder[i+1:])
    
    return TreeNode(val, left, right)

root = buildTree([3,9,20,15,7], [9,3,15,20,7])

que = deque()
que.append(root)
ans = []
while que:
    curr = que.popleft()
    
    ans.append(curr.val)
    
    if not curr.left:
        if curr.right:
            ans.append('null')
    if not curr.right:
        if curr.left:
            ans.append('null')
    if curr.left:
        que.append(curr.left) 
    if curr.right:   
        que.append(curr.right)

print(ans)
        