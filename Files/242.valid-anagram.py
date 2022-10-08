#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        import collections

        count = collections.Counter(s)
        for char in t:
            if char not in t:
                return False
            else:
                count[char] -= 1

        for key in count:
            if count[key] != 0:
                return False
        return True

        
# @lc code=end

