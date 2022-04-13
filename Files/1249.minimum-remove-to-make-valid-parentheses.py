#
# @lc app=leetcode id=1249 lang=python3
#
# [1249] Minimum Remove to Make Valid Parentheses
#
# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/description/
#
# algorithms
# Medium (65.23%)
# Likes:    4507
# Dislikes: 75
# Total Accepted:    394.4K
# Total Submissions: 599.6K
# Testcase Example:  '"lee(t(c)o)de)"'
#
# Given a string s of '(' , ')' and lowercase English characters.
# 
# Your task is to remove the minimum number of parentheses ( '(' or ')', in any
# positions ) so that the resulting parentheses string is valid and return any
# valid string.
# 
# Formally, a parentheses string is valid if and only if:
# 
# 
# It is the empty string, contains only lowercase characters, or
# It can be written as AB (A concatenated with B), where A and B are valid
# strings, or
# It can be written as (A), where A is a valid string.
# 
# 
# 
# Example 1:
# 
# 
# Input: s = "lee(t(c)o)de)"
# Output: "lee(t(c)o)de"
# Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
# 
# 
# Example 2:
# 
# 
# Input: s = "a)b(c)d"
# Output: "ab(c)d"
# 
# 
# Example 3:
# 
# 
# Input: s = "))(("
# Output: ""
# Explanation: An empty string is also valid.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 10^5
# s[i] is either'(' , ')', or lowercase English letter.
# 
# 
#

# @lc code=start
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        ret,open_cnt,close_cnt = '',0,0

        for char in s:

            if char == '(':
                open_cnt += 1
            if char == ')':
                close_cnt += 1

            if open_cnt < close_cnt:
                close_cnt -= 1

            else:
                ret = ret + char

        s = ret

        ret,open_cnt,close_cnt = '',0,0

        for char in reversed(s):

            if char == '(':
                open_cnt += 1
            if char == ')':
                close_cnt += 1

            if close_cnt < open_cnt:
                open_cnt -= 1

            else:
                ret =  char + ret

        return ret




# @lc code=end

