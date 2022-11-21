#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_max, cur_min, total = nums[0], nums[0], nums[0]
        n = len(nums)
        if n==0: return 0
        if n==1: return nums[0]

        for i in range(1, n):
            if nums[i] >= 0:
                cur_max = max(cur_max*nums[i], nums[i])
                cur_min = min(cur_min*nums[i], nums[i])
            else:
                t = cur_max
                cur_max = max(cur_min*nums[i], nums[i])
                cur_min = min(t*nums[i], nums[i])
            total = max(total, cur_max)

        return total
        
# @lc code=end

