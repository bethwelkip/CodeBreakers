'''
Given a matrix with only characters 'X' and 'O', return a matrix with all enclosed 'O's marked to an 'X'.
A region of 'O's is "enclosed" if the region does not reach an 'O' that touches any edge of the matrix. All 'O's on the edge of the matrix are safe from being marked to an 'X'.

Example 1:
Input:
[
  ['O', 'O'],
  ['O', 'O']
]
Output:
[
  ['O', 'O'],
  ['O', 'O']
]
Explanation: All O's touch the edge of the matrix and are therefore safe.

Example 2:
Input:
[
  ['X', 'X', 'O', 'X', 'X'],
  ['X', 'X', 'O', 'X', 'X'],
  ['X', 'X', 'O', 'X', 'X'],
  ['X', 'X', 'X', 'O', 'X'],
  ['X', 'X', 'O', 'X', 'X'],
  ['X', 'X', 'O', 'X', 'X']
]

Output:
[
  ['X', 'X', 'O', 'X', 'X'],
  ['X', 'X', 'O', 'X', 'X'],
  ['X', 'X', 'O', 'X', 'X'],
  ['X', 'X', 'X', 'X', 'X'],
  ['X', 'X', 'O', 'X', 'X'],
  ['X', 'X', 'O', 'X', 'X']
]

Explanation: The 2 regions of O's connect to O's that reach the edge so they are not enclosed regions. One of the O's did not reach the edge by being in a non-enclosed region so it became an 'X'.

Constraints:
The matrix will be m x n
2 <= m <= n <= 100

'''

from collections import deque


class Solution:
    def computeEnclosedRegionsBFS(self, board):
        '''
        :type board: list of list of str
        :rtype: list of list of str
        '''
        def valid(x, y):
            return x < m and x >= 0 and y < n and y >= 0 and board[x][y] == 'O' and (x, y) not in visited
        que = deque()
        visited = set()
        m, n = len(board), len(board[0])
        for r in [0, m-1]:
            for c in range(n):
                if board[r][c] == 'O':
                    que.append((r, c))
                    visited.add((r, c))
        for r in range(m):
            for c in [0, n-1]:
                if board[r][c] == 'O':
                    que.append((r, c))
                    visited.add((r, c))
        while que:
            (r, c) = que.popleft()
            directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
            for (i, j) in directions:
                x, y = r + i, c+j
                if valid(x, y):
                    que.append((x, y))
                    visited.add((x, y))
        for r in range(m):
            for c in range(n):
                if board[r][c] == 'O' and (r, c) not in visited:
                    board[r][c] = 'X'

        return board

    def computeEnclosedRegionsDFS(self, board):
        m, n = len(board), len(board[0])
        visited = set()

        def explore(x, y):

            directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
            for x, y in directions:
                pass  # still have to handle edges either way

        def edge(x, y):
            return x == 0 or y == 0 or x == m-1 or y == n-1

        for r in range(m):
            for c in range(n):
                if board[r][c] == 'O':
                    if edge(r, c):
                        explore(r, c, 'O')
                    else:
                        explore(r, c, 'X')
        return board
