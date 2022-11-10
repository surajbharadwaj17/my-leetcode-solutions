#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n-1

        # finding the pivot point
        while(left < right):
            mid = (left+right)//2
            if nums[mid] > nums[right]:
                left = mid+1
            else:
                right = mid

        pivot = left
        left, right = 0, n-1

        # search with pivot in consideration
        while(left<=right):
            mid = (left+right)//2
            real_mid = (mid+pivot)%n

            if nums[real_mid] == target:
                return real_mid
            elif nums[real_mid] < target:
                left = mid+1
            else:
                right = mid-1

        return -1

        
# @lc code=end

