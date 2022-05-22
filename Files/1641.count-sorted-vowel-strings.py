#
# @lc app=leetcode id=1641 lang=python3
#
# [1641] Count Sorted Vowel Strings
#

# @lc code=start
class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp = [ [1]* 6 ] + [[0] * 6 for _ in range(n)]
        
        for i in range(1, n+1):
            for j in range(1,6):
                dp[i][j] = dp[i][j-1] + dp[i-1][j]

        return dp[n][-1]
        
# @lc code=end

