from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m,n=len(board),len(board[0])
        word_len=len(word)
        def dfs(r,c,k):
            if k==word_len:
                return True
            if not(0<=r<m and 0<=c<n):
                return False
            if board[r][c]!=word[k]:
                return False
            if board[r][c]=='#':
                return False
            org_char=board[r][c]
            board[r][c]='#'
            found=(dfs(r+1,c,k+1) or dfs(r-1,c,k+1) or dfs(r,c+1,k+1) or dfs(r,c-1,k+1))
            board[r][c]=org_char
            return found
        for i in range(m):
            for j in range(n):
                if board[i][j]==word[0]:
                    if dfs(i,j,0):
                        return True
        return False
    

'''
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, 
where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once

'''