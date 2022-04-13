#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#
# https://leetcode.com/problems/subsets-ii/description/
#
# algorithms
# Medium (52.75%)
# Likes:    4728
# Dislikes: 147
# Total Accepted:    484.4K
# Total Submissions: 914.6K
# Testcase Example:  '[1,2,2]'
#
# Given an integer array nums that may contain duplicates, return all possible
# subsets (the power set).
# 
# The solution set must not contain duplicate subsets. Return the solution in
# any order.
# 
# 
# Example 1:
# Input: nums = [1,2,2]
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
# Example 2:
# Input: nums = [0]
# Output: [[],[0]]
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
# 
# 
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        # res = set([[]])
        # ret = [[]]
        # for num in nums:
        #     ret += [item+[num] for item in ret]
        #     res.add(ret)

        # return list(res)

        #DFS
        ret = []
        self.dfs(sorted(nums), [], ret)

        return ret

    
    def dfs(self, nums, path, ret):
        ret.append(path)

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            self.dfs(nums[i+1:], path+[nums[i]], ret)    

# @lc code=end

