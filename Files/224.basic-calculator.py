#
# @lc app=leetcode id=224 lang=python3
#
# [224] Basic Calculator
#

# @lc code=start
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        res = 0
        for char in s:
            if char.isdigit():
                num = 10*num + int(char)
            elif char == "+":
                res += num
            elif char == '-':
                res -= num
            elif char == "(":
                stack.append(res)
                

# @lc code=end

