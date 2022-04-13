"""
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.
"""

from operator import itemgetter


class Solution:
    def insert(self, intervals, newInterval):
        flag = False
        ret = []
        abs_min, abs_max = intervals[0][1], intervals[-1][1]
        ref = [False] * len(range(0,abs_max))
        print(ref)
        for interval in intervals:
            if not flag:
                start = min(newInterval[0], interval[0])
                end = max(newInterval[1], interval[1])

                if start == newInterval[0] or end == newInterval[1]:
                    flag = True

                ret.append([start, end])

            else:
                ret.append(interval)

        return ret

    def insert_v2(self, intervals, newInterval):
        start, end = newInterval[0], newInterval[1]

        left, right = [],[]

        for interval in intervals:
            if interval[1] < start:
                left += interval,
            elif interval[0] >  end:
                right += interval,
            else:
                start = min(start, interval[0])
                end = max(end, interval[1])

        
        print(left + [[start,end]] + right)

soln = Solution()
intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
print(soln.insert_v2(intervals, [4,8]))
