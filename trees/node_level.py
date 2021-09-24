"""
Given a binary tree, return the level of a given node value. 

                    1
                    
                3     10 
                
                
            5       11  
            
# value = int
"""
import collections


def node_level(root, value):
    que = collections.deque()
    level = 0
    que.append((root))
    level_hash = {}

    while len(que) > 0:
        for i in range(len(que)):
            curr_node = que.popleft()

            level_hash[curr_node.val] = level
            if curr_node.left:
                que.append((curr_node.left))
            if curr_node.right:
                que.append((curr_node.right))
        level += 1

    return level_hash[value] if value in level_hash else -1
