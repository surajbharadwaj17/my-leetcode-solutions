#
# @lc app=leetcode id=216 lang=python3
#
# [216] Combination Sum III
#
# https://leetcode.com/problems/combination-sum-iii/description/
#
# algorithms
# Medium (63.61%)
# Likes:    2699
# Dislikes: 73
# Total Accepted:    281.9K
# Total Submissions: 441.9K
# Testcase Example:  '3\n7'
#
# Find all valid combinations of k numbers that sum up to n such that the
# following conditions are true:
# 
# 
# Only numbers 1 through 9 are used.
# Each number is used at most once.
# 
# 
# Return a list of all possible valid combinations. The list must not contain
# the same combination twice, and the combinations may be returned in any
# order.
# 
# 
# Example 1:
# 
# 
# Input: k = 3, n = 7
# Output: [[1,2,4]]
# Explanation:
# 1 + 2 + 4 = 7
# There are no other valid combinations.
# 
# Example 2:
# 
# 
# Input: k = 3, n = 9
# Output: [[1,2,6],[1,3,5],[2,3,4]]
# Explanation:
# 1 + 2 + 6 = 9
# 1 + 3 + 5 = 9
# 2 + 3 + 4 = 9
# There are no other valid combinations.
# 
# 
# Example 3:
# 
# 
# Input: k = 4, n = 1
# Output: []
# Explanation: There are no valid combinations.
# Using 4 different numbers in the range [1,9], the smallest sum we can get is
# 1+2+3+4 = 10 and since 10 > 1, there are no valid combination.
# 
# 
# 
# Constraints:
# 
# 
# 2 <= k <= 9
# 1 <= n <= 60
# 
# 
#

# @lc code=start
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ret = []
        path = []
        nums = list(range(1,10))
        self.dfs(nums, ret, k, path, n)
        return ret

    def dfs(self, nums, ret, k, path, target):
        if target < 0 or k < 0:
            return      # Backtrack
        
        if target == 0 and k == 0:
            ret.append(path)
            return

        for i in range(len(nums)):
            self.dfs(nums[i+1:], ret, k-1, path + [nums[i]], target-nums[i])

# @lc code=end

