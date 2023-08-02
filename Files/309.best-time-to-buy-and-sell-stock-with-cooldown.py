#
# @lc app=leetcode id=309 lang=python3
#
# [309] Best Time to Buy and Sell Stock with Cooldown
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) < 2: return 0

        hold, no_hold, no_hold_cd = float('-inf'), 0, float('-inf')

        for price in prices:
            hold, no_hold, no_hold_cd = max(hold, no_hold-price), max(no_hold, no_hold_cd), hold+price
        return max(no_hold, no_hold_cd)
        
        
# @lc code=end

