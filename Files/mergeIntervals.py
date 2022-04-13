"""
Given an array of intervals where intervals[i] = [starti, endi], 
merge all overlapping intervals, and return an array of the non-overlapping intervals 
that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
"""

class Solution:
    def mergeIntervals(self, intervals):
        ret = []
        intervals = sorted(intervals, key = lambda x: x[0])
        for interval in intervals:
            if not ret or ret[-1][-1] < interval[0]:
                ret.append(interval)
            else:
                ret[-1][-1] = max(ret[-1][-1], interval[-1]) 

        return ret


soln = Solution()
#intervals = [[1,3],[2,6],[8,10],[15,18]]
intervals = [[1,4],[5,6]]
print(soln.mergeIntervals(intervals=intervals))