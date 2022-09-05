#
# @lc app=leetcode id=1329 lang=python3
#
# [1329] Sort the Matrix Diagonally
#

# @lc code=start
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m,n = len(mat), len(mat[0])
        hmap = {}
        i = 0
        for j in range(n):
            hmap[(i,j)] = []
            p,q = i,j
            while(p<m and q<n):
                hmap[(i,j)].append(mat[p][q])
                p += 1
                q += 1

        j=0
        for i in range(m):
            hmap[(i,j)] = []
            p,q = i,j
            while(p<m and q<n):
                hmap[(i,j)].append(mat[p][q])
                p += 1
                q += 1
        
        for key in hmap:
            hmap[key] = sorted(hmap[key])
        
        for key in hmap:
            i,j,k = key[0], key[1], 0
            while(i<m and q<n and k<len(hmap[key])):
                mat[i][j] = hmap[key][k]
                i += 1
                j += 1
                k += 1

        return mat
        
# @lc code=end

