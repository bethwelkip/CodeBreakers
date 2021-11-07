'''
You are given an n x n integer matrix grid where each value grid[i][j] represents the elevation at that point (i, j).

The rain starts to fall. At time t, the depth of the water everywhere is t. You can swim from a square to another 4-directionally adjacent square if and only if the elevation of both squares individually are at most t. You can swim infinite distances in zero time. Of course, you must stay within the boundaries of the grid during your swim.

Return the least time until you can reach the bottom right square (n - 1, n - 1) if you start at the top left square (0, 0).

Input: grid = [[0,2],[1,3]]
Output: 3
Input: grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
Output: 16
Explanation: The final route is shown.
We need to wait until time 16 so that (0, 0) and (4, 4) are connected.

'''

from collections import deque
import heapq as heap


class Solution:
    def swimInWater(self, grid: list(list())) -> int:
        n = len(grid)
        min_heap = []
        min_heap.append((grid[0][0], 0, 0))
        visited = set()
        visited.add((0, 0))
        min_cost = 0

        while min_heap:
            (cost, row, col) = heap.heappop(min_heap)
            directions = [(1, 0), (0, 1), (0, -1), (-1, 0)]
            if row == col and col == n-1:
                return cost
            for i, j in directions:
                new_row = row+i
                new_col = col+j
                if new_row >= 0 and new_row < n and new_col < n and new_col >= 0:
                    if (new_row, new_col) not in visited:
                        min_cost = max(cost, grid[new_row][new_col])
                        visited.add((new_row, new_col))
                        heap.heappush(min_heap, (min_cost, new_row, new_col))

        return min_cost


if __name__ == '__main__':
    sol = Solution()
    arr_a = [[0, 1, 2, 3, 4], [24, 23, 22, 21, 5], [
        12, 13, 14, 15, 16], [11, 17, 18, 19, 20], [10, 9, 8, 7, 6]]
    arr_b = [[0, 2], [1, 3]]
    print(sol.swimInWater(arr_b))
    print(sol.swimInWater(arr_a))
