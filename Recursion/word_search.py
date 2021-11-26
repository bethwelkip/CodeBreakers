'''
No 79 on leetcode
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are
 horizontally or vertically neighboring. The same letter cell may not be used more than once.
 
 Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
 
 
 '''


from typing import List


class Solution:
    def dfs(self, row, col, idx, word, board):
        if idx == len(word)-1:
            return True

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for i, j in directions:
            nr, nc = row + i, col + j
            if nr >= 0 and nc >= 0 and nr < len(board) and nc < len(board[0]):
                if board[nr][nc] == word[idx + 1]:
                    ch = board[nr][nc]
                    board[nr][nc] = ''
                    if self.dfs(nr, nc, idx+1, word, board):
                        board[nr][nc] = ch
                        return True
                    board[nr][nc] = ch
        return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0]:
                    ch = board[r][c]
                    board[r][c] = ""
                    res = self.dfs(r, c, 0, word, board)
                    board[r][c] = ch
                    if res:
                        return True
        return False


'''
Approach:
backtracking
keypoints:
    -  nullify options by modifying board



'''
