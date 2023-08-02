#
# @lc app=leetcode id=452 lang=python3
#
# [452] Minimum Number of Arrows to Burst Balloons
#

# @lc code=start
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:

        points = sorted(points, key=lambda x:x[1])
        ret = 0
        end = float('-inf')

        for point in points:
            if point[0] > end:
                ret += 1
                end = point[1]

        return ret
        
# @lc code=end

