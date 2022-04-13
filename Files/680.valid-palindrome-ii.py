#
# @lc app=leetcode id=680 lang=python3
#
# [680] Valid Palindrome II
#
# https://leetcode.com/problems/valid-palindrome-ii/description/
#
# algorithms
# Easy (38.51%)
# Likes:    4308
# Dislikes: 256
# Total Accepted:    428K
# Total Submissions: 1.1M
# Testcase Example:  '"aba"'
#
# Given a string s, return true if the s can be palindrome after deleting at
# most one character from it.
# 
# 
# Example 1:
# 
# 
# Input: s = "aba"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: s = "abca"
# Output: true
# Explanation: You could delete the character 'c'.
# 
# 
# Example 3:
# 
# 
# Input: s = "abc"
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 10^5
# s consists of lowercase English letters.
# 
# 
#

# @lc code=start
class Solution:
    def validPalindrome(self, s: str) -> bool:
        # 2 pointer technique
        left, right = 0, len(s)-1

        # move left and right pointer until you find the first non-equal elements
        while (left <= right and s[left] == s[right]):
            left += 1
            right -= 1

        # consider only the remaining part of s
        s = s[left:right+1]

        # return true if the remaining part is a palindrome
        return s[1:] == s[1:][::-1] or s[:-1] == s[:-1][::-1]

        
# @lc code=end

