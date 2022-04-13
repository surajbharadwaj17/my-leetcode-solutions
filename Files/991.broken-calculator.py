#
# @lc app=leetcode id=991 lang=python3
#
# [991] Broken Calculator
#
# https://leetcode.com/problems/broken-calculator/description/
#
# algorithms
# Medium (50.06%)
# Likes:    1385
# Dislikes: 164
# Total Accepted:    55.8K
# Total Submissions: 108.9K
# Testcase Example:  '2\n3'
#
# There is a broken calculator that has the integer startValue on its display
# initially. In one operation, you can:
# 
# 
# multiply the number on display by 2, or
# subtract 1 from the number on display.
# 
# 
# Given two integers startValue and target, return the minimum number of
# operations needed to display target on the calculator.
# 
# 
# Example 1:
# 
# 
# Input: startValue = 2, target = 3
# Output: 2
# Explanation: Use double operation and then decrement operation {2 -> 4 ->
# 3}.
# 
# 
# Example 2:
# 
# 
# Input: startValue = 5, target = 8
# Output: 2
# Explanation: Use decrement and then double {5 -> 4 -> 8}.
# 
# 
# Example 3:
# 
# 
# Input: startValue = 3, target = 10
# Output: 3
# Explanation: Use double, decrement and double {3 -> 6 -> 5 -> 10}.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= x, y <= 10^9
# 
# 
#

# @lc code=start
class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:

        # cnt = 0 

        # while(target != startValue):
        #     if target > startValue:
        #         startValue = startValue * 2
        #     elif target < startValue:
        #         startValue = startValue - 1

        #     cnt += 1

        # return(cnt)  

        # ret = 0
        # while(startValue < target):
        #     ret += target %2 +1
        #     target = (target+1)/2

        # return int(ret + startValue - target) 


        if startValue > target:
            return startValue - target

        if startValue == target:
            return 0

        if target %2 == 0:
            return self.brokenCalc(startValue, target//2) + 1
        else:
            return self.brokenCalc(startValue, target+1) + 1
            



        
# @lc code=end

