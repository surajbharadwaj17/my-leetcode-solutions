#
# @lc app=leetcode id=326 lang=python3
#
# [326] Power of Three
#

# @lc code=start
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        i, power = 0,1
        while(power < n):
            power = 3**i
            i += 1
        return power == n
        
# @lc code=end

