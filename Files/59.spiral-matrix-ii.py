#
# @lc app=leetcode id=59 lang=python3
#
# [59] Spiral Matrix II
#
# https://leetcode.com/problems/spiral-matrix-ii/description/
#
# algorithms
# Medium (61.94%)
# Likes:    2867
# Dislikes: 166
# Total Accepted:    322.1K
# Total Submissions: 512.7K
# Testcase Example:  '3'
#
# Given a positive integer n, generate an n x n matrix filled with elements
# from 1 to n^2 in spiral order.
# 
# 
# Example 1:
# 
# 
# Input: n = 3
# Output: [[1,2,3],[8,9,4],[7,6,5]]
# 
# 
# Example 2:
# 
# 
# Input: n = 1
# Output: [[1]]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 20
# 
# 
#

# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
         # Create an empty grid
        grid = [[0]*n for _ in range(n) ]


        rowStart, colStart = 0,0
        rowEnd, colEnd = n-1, n-1

        ele = 1

        while(rowStart <= rowEnd and colStart <= colEnd):

            # first row
            i=colStart
            while(i <= colEnd):
                grid[rowStart][i] = ele
                ele += 1
                i += 1

            rowStart += 1

            # Last column
            i = rowStart
            while(i <= rowEnd):
                grid[i][colEnd] = ele
                ele += 1
                i += 1

            colEnd -= 1

            # last row
            i = colEnd
            while (i >= colStart):
                if rowStart <= rowEnd:    
                    grid[rowEnd][i] = ele
                    ele += 1
                i -= 1

            rowEnd -= 1

            # First column
            i = rowEnd
            while(i >= rowStart):
                if colStart <= colEnd:
                    grid[i][colStart] = ele
                    ele += 1
                i -= 1

            colStart += 1

        return grid   
        
# @lc code=end

