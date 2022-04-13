#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#
# https://leetcode.com/problems/permutations/description/
#
# algorithms
# Medium (71.61%)
# Likes:    9766
# Dislikes: 178
# Total Accepted:    1.1M
# Total Submissions: 1.6M
# Testcase Example:  '[1,2,3]'
#
# Given an array nums of distinct integers, return all the possible
# permutations. You can return the answer in any order.
# 
# 
# Example 1:
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# Example 2:
# Input: nums = [0,1]
# Output: [[0,1],[1,0]]
# Example 3:
# Input: nums = [1]
# Output: [[1]]
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 6
# -10 <= nums[i] <= 10
# All the integers of nums are unique.
# 
# 
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ret = []

        self.dfs(nums, [], ret)
        return ret

    def dfs(self, nums, path, ret):
        if not nums:
            ret.append(path)

        for i in range(len(nums)):
            rest = nums[:i] + nums[i+1:]
            self.dfs(rest, path + [nums[i]], ret)


# @lc code=end

