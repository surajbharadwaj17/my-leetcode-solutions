#
# @lc app=leetcode id=557 lang=python3
#
# [557] Reverse Words in a String III
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(" ")
        for i in range(len(s)):
            left, right = 0, len(s[i])-1
            s[i] = list(s[i])
            while left <= right:
                s[i][left], s[i][right] = s[i][right], s[i][left]
                left += 1
                right -= 1
            s[i] = "".join(s[i])
        return " ".join(s)
        
# @lc code=end

