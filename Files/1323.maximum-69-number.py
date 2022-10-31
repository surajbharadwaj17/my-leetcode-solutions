#
# @lc app=leetcode id=1323 lang=python3
#
# [1323] Maximum 69 Number
#

# @lc code=start
class Solution:
    def maximum69Number (self, num: int) -> int:
        num = list(str(num))
        for i in range(len(num)):
            if num[i] == '6':
                num[i] = '9'
                return "".join(num)
        return "".join(num)
        
# @lc code=end

