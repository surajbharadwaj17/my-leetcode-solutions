#
# @lc app=leetcode id=1235 lang=python3
#
# [1235] Maximum Profit in Job Scheduling
#

# @lc code=start
import bisect
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:

        jobs = zip(startTime, endTime, profit)
        jobs = sorted(jobs, key=lambda x:x[1])

        dp = [[0,0]]

        for start, end, profit in jobs:
            i = bisect.bisect(dp, [start+1]) -1
            if dp[i][1] + profit > dp[-1][1]:
                dp.append([end, dp[i][1]+profit])
        print(dp)
        return dp[-1][1]

        
# @lc code=end

