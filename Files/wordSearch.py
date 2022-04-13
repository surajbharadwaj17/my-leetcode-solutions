"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, 
where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
"""


class Solution:

    def dfs(self,word, i,j,board):
        
        if len(word) == 0:
            return True

        if i<0 or i >= len(board) or j<0 or j >= len(board[0]) or word[0] != board[i][j]:
            return False

        temp = board[i][j]
        board[i][j] = '*'
        ret = self.dfs(word[1:], i+1, j, board) or self.dfs(word[1:], i-1, j, board) or self.dfs(word[1:], i, j+1, board) or self.dfs(word[1:], i, j-1, board)

        board[i][j] = temp
        return ret        

    def exist(self, board, word):
        if not board:
            return

        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(word, i,j,board):
                    return True

        return False


soln = Solution()
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"


print(soln.exist(board, word))