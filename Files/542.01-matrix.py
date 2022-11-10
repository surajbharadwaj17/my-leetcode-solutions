#
# @lc app=leetcode id=542 lang=python3
#
# [542] 01 Matrix
#

# @lc code=start
import collections
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m,n = len(mat), len(mat[0])
        dirs = ((0,1), (0,-1), (-1,0), (1,0))
        q = collections.deque()
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i,j))
                else:
                    mat[i][j] = -1

        while(q):
            cur_i, cur_j = q.popleft()

            for dir in dirs:
                next_i, next_j = cur_i+dir[0], cur_j+dir[1]
                if next_i < 0 or next_i >= m \
                    or next_j < 0 or next_j >= n \
                                or mat[next_i][next_j] != -1:
                    continue
                mat[next_i][next_j] = mat[cur_i][cur_j]+1
                q.append((next_i, next_j))
        
        return mat
       
                        
                             
                    

# @lc code=end

