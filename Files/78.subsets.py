#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#
# https://leetcode.com/problems/subsets/description/
#
# algorithms
# Medium (70.78%)
# Likes:    9525
# Dislikes: 153
# Total Accepted:    1M
# Total Submissions: 1.5M
# Testcase Example:  '[1,2,3]'
#
# Given an integer array nums of unique elements, return all possible subsets
# (the power set).
# 
# The solution set must not contain duplicate subsets. Return the solution in
# any order.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# 
# 
# Example 2:
# 
# 
# Input: nums = [0]
# Output: [[],[0]]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
# All the numbers of nums are unique.
# 
# 
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        # DFS
    #     ret = []
    #     self.dfs(nums, [], ret)
    #     return ret


    # def dfs(self, nums, path, ret):
    #     ret.append(path)
    #     for i in range(len(nums)):
            # self.dfs(nums[i+1:], path + [nums[i]], ret)


        #Iterative
        ret = [[]]
        for num in nums:
            ret += [item+[num]  for item in ret]


        return ret        

        
# @lc code=end

