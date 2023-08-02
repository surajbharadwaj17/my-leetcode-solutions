#
# @lc app=leetcode id=997 lang=python3
#
# [997] Find the Town Judge
#

# @lc code=start
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        count = [0] * (n+1)
        for i,j in trust:
            count[j] += 1
            count[i] -= 1
        
        for i in range(1, n+1):
            if count[i] == n-1:
                return i
        return -1
        
# @lc code=end

