#
# @lc app=leetcode id=51 lang=python3
#
# [51] N-Queens
#

# @lc code=start
class Solution:
    
    def solveNQueens(self, n: int) -> List[List[str]]:
        ret = []
        self.dfs([-1]*n, [], 0, ret)
        return ret

    def dfs(self, nums, path, idx, ret):
        if idx == len(nums):
            ret.append(path)
            return
        for i in range(len(nums)):
            nums[idx] = i
            if self.valid(nums, idx):
                temp = "."*len(nums)
                self.dfs(nums, path+[temp[:i]+"Q"+ temp[i+1:]], idx+1, ret)
                

    def valid(self, nums, n):
        for i in range(n):
            if abs(nums[i]- nums[n]) == n-i or nums[i] == nums[n]:
                return False
        return True
                
        
# @lc code=end

