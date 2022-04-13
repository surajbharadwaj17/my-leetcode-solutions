#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#
# https://leetcode.com/problems/spiral-matrix/description/
#
# algorithms
# Medium (40.76%)
# Likes:    6640
# Dislikes: 813
# Total Accepted:    697.6K
# Total Submissions: 1.7M
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# Given an m x n matrix, return all elements of the matrix in spiral order.
# 
# 
# Example 1:
# 
# 
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]
# 
# 
# Example 2:
# 
# 
# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
# 
# 
# 
# Constraints:
# 
# 
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 10
# -100 <= matrix[i][j] <= 100
# 
# 
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        
        ret = []
        r,c = 0,0
        m,n = len(matrix), len(matrix[0])

        while(r<m and c<n):

            #First row elements
            for i in range(c,n):
                ret.append(matrix[r][i])
            r += 1

            # Last column
            for i in range(r,m):
                ret.append(matrix[i][n-1])
            n -= 1

            # Last row
            if r < m:
                for i in range(n-1,c-1, -1):
                    ret.append(matrix[m-1][i])
                m -= 1

            # First column
            if c < n:
                for i in range(m-1,r-1,-1):
                    ret.append(matrix[i][c])
                c += 1            

        return(ret)

         
# @lc code=end

