'''
No. 212 on Leetcode

Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

 

Example 1:
Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]
Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []
'''

# Trie Nodes

from typing import List
class Node:
    def __init__(self, val=None):
        self.neighbors = {}
        self.key = val
        self.isWord = False


class Solution:
    # build trie first then do dfs on it
    def buildTrie(self, word):
        root = self.trie
        for ch in word:
            if ch in root.neighbors:
                root = root.neighbors[ch]
            else:
                root.neighbors[ch] = Node(ch)
                root = root.neighbors[ch]
        root.isWord = word
        return

    # loop through the matrix and do dfs is ch is a potential start point for a word
    def findWord(self, board):
        root = self.trie

        def dfs(row, col, root, board):
            # if the word exists, add it to result and then remove from trie to avoid re-additions
            if root.isWord:
                self.res.append(root.isWord)
                root.isWord = False

            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for i, j in directions:
                nr, nc = row+i, col+j
                if nr < len(board) and nc < len(board[0]) and nr >= 0 and nc >= 0:
                    if board[nr][nc] in root.neighbors:
                        ch = board[nr][nc]
                        board[nr][nc] = ''
                        dfs(nr, nc, root.neighbors[ch], board)
                        board[nr][nc] = ch

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] in root.neighbors:
                    ch = board[r][c]
                    board[r][c] = ''
                    dfs(r, c, root.neighbors[ch], board)
                    board[r][c] = ch

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.res = []
        self.trie = Node()
        for word in words:
            self.buildTrie(word)
        self.findWord(board)
        return self.res


'''

Approach:
use trie and backtracking

Errors:
with Trie:
    - not removing word from trie
    - decide on better way to initialize isWord

with Backtracking:
    - row + j instead of col + j
    - not removing current ch being considered


'''
