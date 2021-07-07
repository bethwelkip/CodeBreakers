# Zombie matrix 
'''
You are given an m x n grid where each cell can have one of three values:

    0 representing an empty cell,
    1 representing a human, or
    2 representing a zombie.

Every minute, any human that is 4-directionally adjacent to a zombie becomes infected.

Return the minimum number of minutes that must elapse until no cell has an unaffected human. If this is impossible, return -1.
# '''
# grid = [[2,1,1],
#         [1,1,0],
#         [0,1,1]]
# time = 0
# output = 4

from collections import deque
def zombie_matrix(arr):
    m, n = len(arr), len(arr[0])
    que = deque()
    count = 0
    time = 0

    # add zombies to que
    for row in range(len(arr)):
        for col in range(len(arr[0])):
            if arr[row][col] == 2:
                que.append((row, col))
            if arr[row][col] == 1:
                count += 1 #no. of humans
    
    # infect all, if possible
    while len(que) > 0:
        curr_zombie = que.popleft()
        row, col = curr_zombie[0], curr_zombie[1]
        directions = ((0,1), (1, 0), (0, -1), (-1, 0))
        num_infected = 0 

        for i, j in directions:
            new_row = row + i
            new_col = col + j
            if new_row >= 0 and new_row < m and new_col >= 0 and new_col < n:
                if arr[new_row][new_col] == 1:
                    count -= 1
                    num_infected += 1
                    que.append((new_row, new_col))
                    arr[new_row][new_col] = 2
        if num_infected > 0:
            time += 1
    if count > 0: return -1
    return time

grid = [[2,1,1],
        [1,1,0],
        [0,1,1]]

time = zombie_matrix(grid)
print(time)


