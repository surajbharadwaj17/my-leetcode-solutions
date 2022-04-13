#
# @lc app=leetcode id=81 lang=python3
#
# [81] Search in Rotated Sorted Array II
#
# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/
#
# algorithms
# Medium (34.44%)
# Likes:    4093
# Dislikes: 698
# Total Accepted:    402.5K
# Total Submissions: 1.1M
# Testcase Example:  '[2,5,6,0,0,1,2]\n0'
#
# There is an integer array nums sorted in non-decreasing order (not
# necessarily with distinct values).
# 
# Before being passed to your function, nums is rotated at an unknown pivot
# index k (0 <= k < nums.length) such that the resulting array is [nums[k],
# nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For
# example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become
# [4,5,6,6,7,0,1,2,4,4].
# 
# Given the array nums after the rotation and an integer target, return true if
# target is in nums, or false if it is not in nums.
# 
# You must decrease the overall operation steps as much as possible.
# 
# 
# Example 1:
# Input: nums = [2,5,6,0,0,1,2], target = 0
# Output: true
# Example 2:
# Input: nums = [2,5,6,0,0,1,2], target = 3
# Output: false
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 5000
# -10^4 <= nums[i] <= 10^4
# nums is guaranteed to be rotated at some pivot.
# -10^4 <= target <= 10^4
# 
# 
# 
# Follow up: This problem is similar to Search in Rotated Sorted Array, but
# nums may contain duplicates. Would this affect the runtime complexity? How
# and why?
# 
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # find the index of the pivot
        # nums = [1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1]

        # target = 2
        n = len(nums)
        lo,hi = 0,n-1
        print(nums)
        # while(lo <= hi):
        #     mid = (lo+hi)//2
            
        #     if nums[mid] >= nums[hi]:
        #         lo = mid+1
        #     else:
        #         hi = mid-1
        
        # rot = lo
        # print(rot)

        # # Binary search accounting the rotation
        # lo, hi = 0, n-1
        
        # while(lo <= hi):
        #     mid = (lo+hi)//2
        #     real_mid = (mid+rot)%n
            
        #     if target == nums[real_mid]:
        #         return True
            
        #     if target > nums[real_mid]:
        #         lo = mid+1
        #     else:
        #         hi = mid-1
                
        # return False

        while(lo <= hi):
            mid = lo + (hi-lo)//2
            if nums[mid] == target:
                return True

            while ( lo < mid and nums[lo] == nums[mid]):
                lo += 1

            if nums[lo] <= nums[mid]:
                # Target is in first half
                if nums[lo] <= target < nums[mid]:
                    hi = mid-1
                else:
                    lo = mid+1

            else:
                # target is in second half
                if nums[mid] < target <= nums[hi]:
                    lo = mid+1
                else:
                    hi = mid-1

        return False 

# @lc code=end

