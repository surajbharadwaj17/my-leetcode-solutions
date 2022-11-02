#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ret = []
        p = 1
        for i in range(len(nums)):
            ret.append(p)
            p *= nums[i]

        p = 1
        for i in range(len(nums)-1, -1, -1):
            ret[i] *= p
            p *= nums[i]

        return ret
        
# @lc code=end

