#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#
# https://leetcode.com/problems/combination-sum/description/
#
# algorithms
# Medium (64.85%)
# Likes:    10320
# Dislikes: 221
# Total Accepted:    1M
# Total Submissions: 1.6M
# Testcase Example:  '[2,3,6,7]\n7'
#
# Given an array of distinct integers candidates and a target integer target,
# return a list of all unique combinations of candidates where the chosen
# numbers sum to target. You may return the combinations in any order.
# 
# The same number may be chosen from candidates an unlimited number of times.
# Two combinations are unique if the frequency of at least one of the chosen
# numbers is different.
# 
# It is guaranteed that the number of unique combinations that sum up to target
# is less than 150 combinations for the given input.
# 
# 
# Example 1:
# 
# 
# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple
# times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.
# 
# 
# Example 2:
# 
# 
# Input: candidates = [2,3,5], target = 8
# Output: [[2,2,2,2],[2,3,3],[3,5]]
# 
# 
# Example 3:
# 
# 
# Input: candidates = [2], target = 1
# Output: []
# 
# 
# 
# Constraints:
# 
# 
# 1 <= candidates.length <= 30
# 1 <= candidates[i] <= 200
# All elements of candidates are distinct.
# 1 <= target <= 500
# 
# 
#

# @lc code=start
class Solution:

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []
        self.dfs(candidates, target, ret, [])
        return ret

    def dfs(self, nums, target, ret, path):
        # Base case
        if target < 0: return 

        if target == 0:     # Success case - Add the current path to result 
            ret.append(path)
            return
        
        for i in range(len(nums)):
            self.dfs(nums[i:], target-nums[i], ret, path+[nums[i]])

                # for each occurence of i, we have n-i possible paths

    # I think the time complexity is O(N + N)





    
# @lc code=end

