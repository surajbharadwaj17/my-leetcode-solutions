"""
Given an array of intervals intervals where intervals[i] = [starti, endi],
 return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

 

Example 1:

Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
"""

class Solution:

    def isOverlapping(self, starts, ends):
        front = max(starts)
        back = min(ends)
        return back - front > 0

    def eraseOverlapIntervals(self, intervals):

        ret = 0

        intervals = sorted(intervals, key = lambda x: x[0])
        start = intervals[0][0]
        end = intervals[0][1]
        
        for i in range(1,len(intervals)):
            print(intervals[i], (start,end))
            if self.isOverlapping([intervals[i][0], start],[intervals[i][1], end]):
                ret += 1

            start, end = min(start, intervals[i][0]), max(end, intervals[i][1])
        return ret


    def eraseOverlapIntervals_v2(self, intervals):
        ret = 0
        end = float('-inf')
        
        intervals = sorted(intervals, key = lambda x: x[1])
        for interval in intervals:
            start = interval[0]

            if start >= end:
                end = interval[1]
            else:
                ret += 1

        return ret


soln = Solution()
#intervals = [[1,2],[2,3],[3,4],[1,3]]
intervals = [[1,100],[11,22],[1,11],[2,12]]
print(soln.eraseOverlapIntervals_v2(intervals))