#
# @lc app=leetcode id=151 lang=python3
#
# [151] Reverse Words in a String
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(" ")  # O(N)
        ret = []
        for ele in s[::-1]:
            if ele:
                ret.append(ele)

        return " ".join(ret)

        
# @lc code=end

