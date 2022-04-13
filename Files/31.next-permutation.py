#
# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#
# https://leetcode.com/problems/next-permutation/description/
#
# algorithms
# Medium (35.40%)
# Likes:    9417
# Dislikes: 3169
# Total Accepted:    740.1K
# Total Submissions: 2.1M
# Testcase Example:  '[1,2,3]'
#
# A permutation of an array of integers is an arrangement of its members into a
# sequence or linear order.
# 
# 
# For example, for arr = [1,2,3], the following are considered permutations of
# arr: [1,2,3], [1,3,2], [3,1,2], [2,3,1].
# 
# 
# The next permutation of an array of integers is the next lexicographically
# greater permutation of its integer. More formally, if all the permutations of
# the array are sorted in one container according to their lexicographical
# order, then the next permutation of that array is the permutation that
# follows it in the sorted container. If such arrangement is not possible, the
# array must be rearranged as the lowest possible order (i.e., sorted in
# ascending order).
# 
# 
# For example, the next permutation of arr = [1,2,3] is [1,3,2].
# Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
# While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does
# not have a lexicographical larger rearrangement.
# 
# 
# Given an array of integers nums, find the next permutation of nums.
# 
# The replacement must be in place and use only constant extra memory.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,2,3]
# Output: [1,3,2]
# 
# 
# Example 2:
# 
# 
# Input: nums = [3,2,1]
# Output: [1,2,3]
# 
# 
# Example 3:
# 
# 
# Input: nums = [1,1,5]
# Output: [1,5,1]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 100
# 
# 
#

# @lc code=start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        left = right = len(nums) - 1

        while left > 0 and nums[left - 1] >= nums[left]: # decrease the left pointer until you find the first ascending pair
            left -= 1

        if left == 0: # if the array is already in descending order, reverse it
            nums.reverse()
            return

        k = left - 1 # k is the index of the first ascending pair
        while nums[right] <= nums[k]: # find the smallest number that is larger than nums[k]
            right -= 1

        nums[k], nums[right] = nums[right], nums[k] # swap the smallest number with nums[k]

        nums[left:] = nums[left:][::-1] # reverse the rest of the array

        
                
# @lc code=end

