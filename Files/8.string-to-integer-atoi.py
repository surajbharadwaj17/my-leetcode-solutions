#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int: 
        # leading whitespace
        s = s.strip()
        t_res = []
        for i in range(len(s)):
            if (i==0) and (s[0] == '+' or s[0] == '-'):
                continue
            if s[i].isdigit():
                t_res.append(s[i])
            else:
                break
        
        res = 0
        if t_res:
            res = int("".join(t_res))
            if s[0] == '-': 
                res *= -1
            
            res = max(-2**31, res)
            res = min(2**31-1, res)

        return res


# @lc code=end

