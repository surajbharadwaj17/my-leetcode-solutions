#
# @lc app=leetcode id=32 lang=python3
#
# [32] Longest Valid Parentheses
#

# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        
        if not s:
            return 0

        stack = []
        dp = [0]* (len(s))      # represents the longest valid parentheses ending at i

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                if stack:
                    pos = stack.pop()
                    dp[i] = dp[pos-1] + i - pos + 1
                    
        return max(dp)
        
# @lc code=end


