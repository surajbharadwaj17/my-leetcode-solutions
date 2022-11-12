#
# @lc app=leetcode id=696 lang=python3
#
# [696] Count Binary Substrings
#

# @lc code=start
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        temp, consec, ret = [], 1, 0

        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                consec += 1
            else:
                temp.append(consec)
                consec = 1

        temp.append(consec)

        for i in range(1, len(temp)):
            ret += min(temp[i], temp[i-1])

        return ret
# @lc code=end

