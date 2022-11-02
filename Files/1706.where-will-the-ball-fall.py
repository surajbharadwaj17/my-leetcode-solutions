#
# @lc app=leetcode id=1706 lang=python3
#
# [1706] Where Will the Ball Fall
#

# @lc code=start
from typing import List

class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        self.ret = []
        self.m,self.n = len(grid), len(grid[0])
        for j in range(self.n):
            self.ret.append(self.dfs(i=0, j=j, grid=grid))

        return self.ret

    def dfs(self, i,j,grid):

        if i == self.m:
            return j

        elif grid[i][j] == 1 and j+1 < self.n and grid[i][j+1] == 1:     
            return self.dfs(i+1, j+1, grid)
        elif grid[i][j] == -1 and j-1>= 0 and grid[i][j-1] == -1:
            return self.dfs(i+1, j-1, grid)
        else:
            return -1

   

        
# @lc code=end

