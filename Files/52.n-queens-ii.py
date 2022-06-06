#
# @lc app=leetcode id=52 lang=python3
#
# [52] N-Queens II
#

# @lc code=start
class Solution:
    def totalNQueens(self, n: int) -> int:
        self.ret = 0
        self.dfs([-1]*n, 0)
        return self.ret

    def dfs(self, nums, idx):
        if idx == len(nums):
            self.ret += 1
            return
        for i in range(len(nums)):
            nums[idx] = i
            if self.valid(nums, idx):
                temp = "."*len(nums)
                self.dfs(nums, idx+1)
                

    def valid(self, nums, n):
        for i in range(n):
            if abs(nums[i]- nums[n]) == n-i or nums[i] == nums[n]:
                return False
        return True
        
# @lc code=end

