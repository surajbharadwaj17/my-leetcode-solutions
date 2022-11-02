#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#

# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        import collections
        count = collections.Counter(nums)

        i = 0
        while(i < count[0]):
            nums[i] = 0
            i += 1

        while(i < count[0]+count[1]):
            nums[i] = 1
            i += 1

        while(i < len(nums)):
            nums[i] = 2
            i += 1        
# @lc code=end

