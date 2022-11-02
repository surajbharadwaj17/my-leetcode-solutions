#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Kadane's Algorithm
        """
        max_cur, max_final = 0,0

        for i in range(1, len(prices)):
            max_cur += prices[i] - prices[i-1]

            max_cur = max(max_cur, 0)
            max_final = max(max_final, max_cur)

        return max_final
        """

        # Sliding window : 
        # * Move the left pointer only if the current profit becomes negative -> Time to find a new day to buy
        # * Update the final max in each iteration
        # * Move the right pointer
        # Mem - O(1), Time - O(N)
        left, right = 0, 1
        final = 0
        while right < len(prices):
            cur = prices[right] - prices[left]
            if prices[left] < prices[right]:
                final = max(final, cur)
            
            else:
                left = right
            right += 1

        return final

# @lc code=end

