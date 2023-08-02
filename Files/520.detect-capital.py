#
# @lc app=leetcode id=520 lang=python3
#
# [520] Detect Capital
#

# @lc code=start
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        caps = 0
        n = len(word)

        for letter in word:
            if letter.isupper():
                caps += 1
        
        if caps == 0 or caps == n or caps == 1 and word[0].isupper():
            return True
        return False

        
# @lc code=end

