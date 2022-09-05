#
# @lc app=leetcode id=673 lang=python3
#
# [673] Number of Longest Increasing Subsequence
#

# @lc code=start
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        self.ret = 0


    def dfs(self,nums, idx):
        if nums[idx] < nums[idx-1]:
            return # Backtracking

        # success case
        
        
        
# @lc code=end

