#
# @lc app=leetcode id=948 lang=python3
#
# [948] Bag of Tokens
#

# @lc code=start
class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        score = 0
        cur = 0
        
        # Sort the tokens
        tokens = sorted(tokens)

        # Buy at the cheapest and sell at the most expensive
        while tokens and (tokens[0] <= power or cur):
            if tokens[0] <= power:
                power -= tokens.pop(0)
                cur += 1
            else:
                power += tokens.pop()
                cur -= 1
            score = max(score, cur)
        return score
        
        
# @lc code=end

