#
# @lc app=leetcode id=867 lang=python3
#
# [867] Transpose Matrix
#

# @lc code=start
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m,n = len(matrix), len(matrix[0])
        ret = []
        for j in range(n):
            new_row = []
            for i in range(m):
                new_row.append(matrix[i][j])

            ret.append(new_row)

        return ret

        
# @lc code=end

