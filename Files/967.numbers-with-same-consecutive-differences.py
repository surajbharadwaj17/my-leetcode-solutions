#
# @lc app=leetcode id=967 lang=python3
#
# [967] Numbers With Same Consecutive Differences
#

# @lc code=start
class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        cur = range(1,10)
        for i in range(2,n+1):
            cur2 = []
            for x in cur:
                y = x%10
                if y+k < 10:
                    cur2.append(10*x+y+k)
                if k>0 and y-k >= 0:
                    cur2.append(10*x+y-k)
            cur = cur2
        return cur
        
# @lc code=end

