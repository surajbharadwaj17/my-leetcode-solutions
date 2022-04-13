#
# @lc app=leetcode id=844 lang=python3
#
# [844] Backspace String Compare
#
# https://leetcode.com/problems/backspace-string-compare/description/
#
# algorithms
# Easy (47.35%)
# Likes:    3703
# Dislikes: 172
# Total Accepted:    396.7K
# Total Submissions: 838.4K
# Testcase Example:  '"ab#c"\n"ad#c"'
#
# Given two strings s and t, return true if they are equal when both are typed
# into empty text editors. '#' means a backspace character.
# 
# Note that after backspacing an empty text, the text will continue empty.
# 
# 
# Example 1:
# 
# 
# Input: s = "ab#c", t = "ad#c"
# Output: true
# Explanation: Both s and t become "ac".
# 
# 
# Example 2:
# 
# 
# Input: s = "ab##", t = "c#d#"
# Output: true
# Explanation: Both s and t become "".
# 
# 
# Example 3:
# 
# 
# Input: s = "a#c", t = "b"
# Output: false
# Explanation: s becomes "c" while t becomes "b".
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length, t.length <= 200
# s and t only contain lowercase letters and '#' characters.
# 
# 
# 
# Follow up: Can you solve it in O(n) time and O(1) space?
# 
#

# @lc code=start
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1, stack2 = [], []

        for i in range(len(s)):
            if s[i] == '#':
                if stack1:
                    stack1.pop()
            else:
                stack1.append(s[i])

        for i in range(len(t)):
            if t[i] == '#':
                if stack2:
                    stack2.pop()
            else:
                stack2.append(t[i])

        return stack1 == stack2
        
        
# @lc code=end

