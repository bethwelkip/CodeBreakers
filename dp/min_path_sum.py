'''
Given a grid, find a path from the top-left to the
bottom right corner that minimizes the sum of the
numbers along the path. you can only move down or right

[
    [3,2,1,3],
    [1,9,2,3],
    [9,1,5,4]

]


'''
import heapq


def min_path(arr):
    if len(arr) == 0 or len(arr[0]) == 0:
        return 0

    m, n = len(arr)-1, len(arr[0])-1
    hp = []
    visited = set()

    heapq.heappush(hp, (arr[0][0], 0, 0))
    while hp:
        (cost, row, col) = heapq.heappop(hp)
        if row == m and col == n:
            return cost
        visited.add((row, col))
        for i, j in [(0, 1), (1, 0)]:
            n_row = row + i
            n_col = col + j
            if n_row <= m and n_col <= n and (n_row, n_col) not in visited:
                heapq.heappush(hp, (cost+arr[n_row][n_col], n_row, n_col))
    return cost


arr = [
    [3, 2, 1, 3],
    [1, 9, 2, 3],
    [9, 1, 5, 4]

]
print(min_path(arr))
