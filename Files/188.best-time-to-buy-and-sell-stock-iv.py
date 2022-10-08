#
# @lc app=leetcode id=188 lang=python3
#
# [188] Best Time to Buy and Sell Stock IV
#

# @lc code=start
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        
        if k >= n//2: 
            maxPro = 0
            for i in range(1, n):
                if prices[i] > prices[i-1]:
                    maxPro += prices[i] - prices[i-1]
            return maxPro

        dp = [[0 for _ in range(n)] for x in range(k+1) ]
        for i in range(1,k+1):
            curPro = -prices[0]
            for j in range(1, n):
                dp[i][j] = max(dp[i][j-1], prices[j]+curPro)
                curPro = max(curPro, dp[i-1][j-1] - prices[j])
        return dp[k][n-1]
        
# @lc code=end

