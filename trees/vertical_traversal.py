"""
Given the root of a binary tree, calculate the vertical order traversal of the binary tree.

For each node at position (row, col), its left and right children will be at positions (row + 1, col - 1) and (row + 1, col + 1) respectively. The root of the tree is at (0, 0).

The vertical order traversal of a binary tree is a list of top-to-bottom orderings for each column index starting from the leftmost column and ending on the rightmost column. There may be multiple nodes in the same row and same column. In such a case, sort these nodes by their values.

Return the vertical order traversal of the binary tree.

                                            3   (0,0)
                                    9(1,-1)      20   (1,1)
                                    
                                             15(2,0)      7 (2,2)
                        7
Input: root = [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
Explanation:
Column -1: Only node 9 is in this column.
Column 0: Nodes 3 and 15 are in this column in that order from top to bottom.
Column 1: Only node 20 is in this column.
Column 2: Only node 7 is in this column.


Input: root = [1,2,3,4,5,6,7]
Output: [[4],[2],[1,5,6],[3],[7]]
"""
from collections import defaultdict, deque

class Node:
    def __init__(self,val,left=None, right=None):
        self.val = val
        self.right = right
        self.left = left
        
def vertical_order(root):
    res = []
    vert_hash = defaultdict(list)
    que = deque()
    
    que.append((root,0,0))
    
    while len(que)>0:
        for i in range(len(que)):
            node, r, c = que.popleft()
            vert_hash[c].append((r,node.val))
            if node.left:
                que.append((node.left, r+1, c-1))
            if node.right:
                que.append((node.right, r+1, c+1))
    keys = sorted(vert_hash.keys())
    for key in keys:     
        res.append([v[1] for v in sorted(vert_hash[key])])
    return res

 # [1,2,3,4,5,6,7] 
a,b,c,d,e,f,g= Node(1),Node(2),Node(3),Node(4),Node(5),Node(6),Node(7)
a.left= b
a.right= c
b.left = d
b.right = e
c.left = f
c.right = g
print(vertical_order(a))