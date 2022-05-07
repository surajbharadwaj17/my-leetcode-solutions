#
# @lc app=leetcode id=581 lang=python3
#
# [581] Shortest Unsorted Continuous Subarray
#

# @lc code=start
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1

        while left < len(nums)-1 and nums[left+1] >= nums[left]:
            left += 1
        
        while right > 0 and nums[right-1] <= nums[right]:
            right -= 1
            
        if left >= right:
            return 0

        minTemp = min(nums[left:right+1])
        maxTemp = max(nums[left:right+1])

        while left >= 0 and nums[left] > minTemp:
            left -= 1

        while right < len(nums) and nums[right] < maxTemp:
            right += 1

        return right - left - 1

        
# @lc code=end

