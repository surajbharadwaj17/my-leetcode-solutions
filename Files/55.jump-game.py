#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:

        # ptr, i = 0,0
    
        # if len(nums) == 1:
        #     return True

        # while(ptr < len(nums)):
        #     if nums[ptr] == 0:
        #         if ptr == len(nums)-1:
        #             return True
        #         else:
        #             return False
        #     else:
        #         ptr += nums[i]

        #     i += 1
        # if ptr == len(nums):
        #     return True 
        # return True
        

        ub, idx = 0,0
        n = len(nums)-1

        while(idx <= ub):
            ub = max(idx+nums[idx], ub)

            if idx >= n:
                return True
            idx += 1

        return False


# @lc code=end


