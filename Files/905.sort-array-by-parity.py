#
# @lc app=leetcode id=905 lang=python3
#
# [905] Sort Array By Parity
#

# @lc code=start
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        ret1, ret2 = [],[]

        for i in nums:
            if i % 2 == 0:
                ret1.append(i)
            else:
                ret2.append(i)
        
        return ret1 + ret2
        

# @lc code=end

