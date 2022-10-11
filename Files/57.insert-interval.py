#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#

# @lc code=start
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left, right = [], []
        start, end = newInterval[0], newInterval[1]
        for interval in intervals:
            if interval[1] < start:
                 left.append(interval)
            elif interval[0] > end:
                right.append(interval)
            else:
                start = min(start, interval[0])
                end = max(end, interval[1])

        return (left + [[start, end]] + right)

        # start, end = newInterval[0], newInterval[1]

        # left, right = [],[]

        # for interval in intervals:
        #     if interval[1] < start:
        #         left += interval,
        #     elif interval[0] >  end:
        #         right += interval,
        #     else:
        #         start = min(start, interval[0])
        #         end = max(end, interval[1])

        
        # return(left + [[start,end]] + right)
        
# @lc code=end

