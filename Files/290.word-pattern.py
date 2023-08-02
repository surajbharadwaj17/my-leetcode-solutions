#
# @lc app=leetcode id=290 lang=python3
#
# [290] Word Pattern
#

# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        hmap = {}

        if len(words) != len(pattern): return False
        if len(set(words)) != len(set(pattern)): return False

        for i in range(len(words)):
            if words[i] not in hmap:
                hmap[words[i]] = pattern[i]
            elif hmap[words[i]] != pattern[i]:
                    return False
        
        return True
        
# @lc code=end

