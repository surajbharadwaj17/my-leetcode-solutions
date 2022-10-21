#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#

# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        import collections 
        r_count, m_count = collections.Counter(ransomNote), collections.Counter(magazine)

        for key,val in r_count.items():
            if m_count[key] < val:
                return False
        return True

# @lc code=end

