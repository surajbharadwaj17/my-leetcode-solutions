#
# @lc app=leetcode id=149 lang=python3
#
# [149] Max Points on a Line
#

# @lc code=start
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        ret = 0
        for i in range(n):
            for j in range(i+1, n):
                if(points[i][0] == points[j][0] and points[i][1] == points[j][1]):
                    continue
                sum = 0
                for k in range(n):
                    sum += self.same_line(points[i], points[j], points[k])

                ret = max(ret, sum)

        if ret == 0: return n
        return ret

    def same_line(self, x,y,z):
        if (x[0]-z[0])*(y[1]-z[1]) == (x[1]-z[1])*(y[0]-z[0]):
            return 1
        return 0

        
# @lc code=end

