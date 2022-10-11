#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum, final_sum = 0, nums[0]
        for i in range(len(nums)):
            if cur_sum < 0:
                cur_sum = 0
            cur_sum += nums[i]
            final_sum = max(final_sum, cur_sum)
        return final_sum
        
# @lc code=end

