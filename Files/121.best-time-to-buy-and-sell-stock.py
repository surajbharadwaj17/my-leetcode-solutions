#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_cur, max_final = 0,0

        for i in range(1, len(prices)):
            max_cur += prices[i] - prices[i-1]

            max_cur = max(max_cur, 0)
            max_final = max(max_final, max_cur)

        return max_final
# @lc code=end

