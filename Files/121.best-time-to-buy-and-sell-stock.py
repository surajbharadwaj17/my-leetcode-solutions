#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Kadane's Algorithm
        # max_cur, max_final = 0,0

        # for i in range(1, len(prices)):
        #     max_cur += prices[i] - prices[i-1]

        #     max_cur = max(max_cur, 0)
        #     max_final = max(max_final, max_cur)

        # return max_final

        # Sliding window
        left, right = 0, 1
        cur, final = 0,0
        while right < len(prices):
            cur = prices[right] - prices[left]
            if prices[left] < prices[right]:
                #final = max(final, cur)
                if cur > final:
                    final = cur
            else:
                left = right
            right += 1

        return final

# @lc code=end

