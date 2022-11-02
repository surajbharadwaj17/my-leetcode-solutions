#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#

# @lc code=start
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        # Finding the left and right subparts at the newInterval

        left, right = [], []
        start, end = newInterval[0], newInterval[1]     # Very imp to keep track of the current minimum start and end 
        for interval in intervals:
            if interval[1] < newInterval[0]:
                left.append(interval)
            elif interval[0] > newInterval[1]:
                right.append(interval)
            else:
                start = min(interval[0], start)
                end = max(interval[1], end)

        return (left + [[start, end]] + right)

# @lc code=end

