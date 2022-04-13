#
# @lc app=leetcode id=856 lang=python3
#
# [856] Score of Parentheses
#
# https://leetcode.com/problems/score-of-parentheses/description/
#
# algorithms
# Medium (65.40%)
# Likes:    3309
# Dislikes: 97
# Total Accepted:    102K
# Total Submissions: 156K
# Testcase Example:  '"()"'
#
# Given a balanced parentheses string s, return the score of the string.
# 
# The score of a balanced parentheses string is based on the following
# rule:
# 
# 
# "()" has score 1.
# AB has score A + B, where A and B are balanced parentheses strings.
# (A) has score 2 * A, where A is a balanced parentheses string.
# 
# 
# 
# Example 1:
# 
# 
# Input: s = "()"
# Output: 1
# 
# 
# Example 2:
# 
# 
# Input: s = "(())"
# Output: 2
# 
# 
# Example 3:
# 
# 
# Input: s = "()()"
# Output: 2
# 
# 
# 
# Constraints:
# 
# 
# 2 <= s.length <= 50
# s consists of only '(' and ')'.
# s is a balanced parentheses string.
# 
# 
#

# @lc code=start
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        score = 0

        for char in s:
            
            if char == '(':
                stack.append(score)
                score = 0

            if char == ')':

                score += stack.pop() + max(score, 1)
        print(stack)
        return score
        
# @lc code=end

