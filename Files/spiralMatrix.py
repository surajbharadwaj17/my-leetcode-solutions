"""
Given a mxn matrix, return all elements of the matrix in spiral order.
"""

class Solution:
    def spiralOrder_x(self, matrix):
        if not matrix:
            return []
        
        m, n = len(matrix), len(matrix[0])
        res = []
        
        i, j = 0, 0
        while m > 0 and n > 0:
            if n == 1:
                res += matrix[i][j:j+n]
                break
            if m == 1:
                res += matrix[i][j:j+m]
                break
            
    def spiralOrder(self, matrix):
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
        
    
soln = Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
soln.spiralOrder(matrix)