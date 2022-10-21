#
# @lc app=leetcode id=1832 lang=python3
#
# [1832] Check if the Sentence Is Pangram
#

# @lc code=start
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        import collections

        alpha = "abcdefghijklmnopqrstuvwxyz"
        s_count = collections.Counter(sentence)
        for char in alpha:
            if char not in s_count:
                return False
        return True

        
# @lc code=end

