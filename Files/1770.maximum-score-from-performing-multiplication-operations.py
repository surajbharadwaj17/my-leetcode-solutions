#
# @lc app=leetcode id=1770 lang=python3
#
# [1770] Maximum Score from Performing Multiplication Operations
#

# @lc code=start


class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n,m = len(nums), len(multipliers)
        dp = [ [0] * (m+1) for _ in range(m+1)]

        for l in range(m-1, -1, -1):
            for i in range(m-1, -1, -1):
                r = n - (i-l) - 1
                if r < 0 or r >= n:
                    break
                left = dp[l+1][i+1] + nums[l] * multipliers[i]
                right = dp[l][i+1] + nums[r] * multipliers[i]
                dp[l][i] = max(left, right)

        return dp[0][0]
# @lc code=end

