#
# @lc app=leetcode id=456 lang=python3
#
# [456] 132 Pattern
#

# @lc code=start
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        import math
        stack = []

        s3 = -math.inf
        
        for i in range(len(nums)-1,-1,-1):
            if nums[i] < s3:
                return True
            else:
                while(stack and nums[i] > stack[-1]):
                    s3 = stack[-1]
                    stack.pop()
            stack.append(nums[i])

        return False

# @lc code=end

