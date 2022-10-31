#
# @lc app=leetcode id=1317 lang=python3
#
# [1317] Convert Integer to the Sum of Two No-Zero Integers
#

# @lc code=start
class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        
        for a in range(n):
            left, right = a, n-a
            if "0" not in str(left) and "0" not in str(right):
                return [a, n-a]
        

# @lc code=end

