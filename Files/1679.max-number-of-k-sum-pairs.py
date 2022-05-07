#
# @lc app=leetcode id=1679 lang=python3
#
# [1679] Max Number of K-Sum Pairs
#

# @lc code=start
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:

        nums = sorted(nums)
        ret = 0
        left, right = 0, len(nums)-1

        while(left < right):
            cur_sum = nums[left] + nums[right]

            if cur_sum == k:
                ret += 1
                left += 1
                right -= 1
            
            elif cur_sum < k:
                left += 1
            
            else:
                right -= 1

        return ret
# @lc code=end

