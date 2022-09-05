#
# @lc app=leetcode id=299 lang=python3
#
# [299] Bulls and Cows
#

# @lc code=start
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls, cows = 0,0
        ret = f"{bulls}A{cows}B"
        hmap = {}
        for i in range(len(secret)):
            if guess[i] == secret[i]:
                bulls += 1
                continue
            if guess[i] in hmap:
                cows += 1
            else:
                hmap[secret[i]] = True
        return ret

            
        
# @lc code=end

