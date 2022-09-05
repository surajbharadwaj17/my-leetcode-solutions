#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hmap1, hmap2 = {}, {}
        for i in range(len(s)):
            if s[i] in hmap1 and hmap1[s[i]] != t[i]:
                return False
            if t[i] in hmap2 and hmap2[t[i]] != s[i]:
                return False
            hmap1[s[i]] = t[i]
            hmap2[t[i]] = s[i]
        return True
        
# @lc code=end

