#
# @lc app=leetcode id=724 lang=python3
#
# [724] Find Pivot Index
#

# @lc code=start
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l_sum, r_sum = 0,sum(nums)

        for i in range(len(nums)):
            if l_sum == r_sum - nums[i]:
                return i
            l_sum += nums[i]
            r_sum -= nums[i]
        return -1
        
# @lc code=end

