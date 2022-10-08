#
# @lc app=leetcode id=1004 lang=python3
#
# [1004] Max Consecutive Ones III
#

# @lc code=start
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        start = 0
        for end in range(len(nums)):
            k -= 1-nums[end]
            if k<0:
                k += 1-nums[start]
                start += 1
        return end-start+1


        
        
# @lc code=end

