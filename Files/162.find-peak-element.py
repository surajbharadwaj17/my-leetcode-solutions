#
# @lc app=leetcode id=162 lang=python3
#
# [162] Find Peak Element
#

# @lc code=start
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        # nums = [0]+nums+[0]
        # for i in range(1, n):
        #     if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
        #         return i-1
        # return 0       
        # 
        left,right = 0, n-1
        while(left <= right):
            mid = (left+right)//2
            if nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]:
                return mid
            left += 1
            right -= 1
        return left
        print(left, right) 

# @lc code=end

