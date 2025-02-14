#
# @lc app=leetcode id=278 lang=python3
#
# [278] First Bad Version
#

# @lc code=start
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        nums = range(1, n+1)

        while left<=right:
            mid = (left+right)//2
            if isBadVersion(mid):
                right = mid-1
            else:
                left = mid+1

        return left
        
# @lc code=end

