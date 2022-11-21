#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#

# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while(stack and temperatures[stack[-1]] < temp):
                cur = stack.pop()
                res[cur] = i-cur

            stack.append(i)

        return res
        
# @lc code=end

