#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#
# https://leetcode.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (40.61%)
# Likes:    11617
# Dislikes: 513
# Total Accepted:    2M
# Total Submissions: 5M
# Testcase Example:  '"()"'
#
# Given a string s containing just the characters '(', ')', '{', '}', '[' and
# ']', determine if the input string is valid.
# 
# An input string is valid if:
# 
# 
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# 
# 
# 
# Example 1:
# 
# 
# Input: s = "()"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: s = "()[]{}"
# Output: true
# 
# 
# Example 3:
# 
# 
# Input: s = "(]"
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 10^4
# s consists of parentheses only '()[]{}'.
# 
# 
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hmap = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }
        
        for char in s:
            if char in hmap.values():
                stack.append(char)
            elif char in hmap:
                if stack and stack[-1] == hmap[char]:
                    stack.pop()
                else:
                    return False

        return len(stack) == 0
        
        
# @lc code=end

