#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        if len(s) == 0:
            return True
        i,j = 0,0
        while(i<len(s) and j<len(t)):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)

        
# @lc code=end

