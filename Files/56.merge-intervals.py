#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ret = []

        intervals.sort(key = lambda x:x[0])

        for i in range(len(intervals)):
            if not ret or ret[-1][1] < intervals[i][0]: # Non Overlapping
                ret.append(intervals[i])
            else:
                ret[-1][1] = max(ret[-1][1], intervals[i][1])

        return ret
        
# @lc code=end

