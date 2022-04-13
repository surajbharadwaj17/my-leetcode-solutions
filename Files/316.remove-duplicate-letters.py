#
# @lc app=leetcode id=316 lang=python3
#
# [316] Remove Duplicate Letters
#
# https://leetcode.com/problems/remove-duplicate-letters/description/
#
# algorithms
# Medium (41.41%)
# Likes:    4082
# Dislikes: 286
# Total Accepted:    158.8K
# Total Submissions: 380.7K
# Testcase Example:  '"bcabc"'
#
# Given a string s, remove duplicate letters so that every letter appears once
# and only once. You must make sure your result is the smallest in
# lexicographical order among all possible results.
# 
# 
# Example 1:
# 
# 
# Input: s = "bcabc"
# Output: "abc"
# 
# 
# Example 2:
# 
# 
# Input: s = "cbacdcbc"
# Output: "acdb"
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 10^4
# s consists of lowercase English letters.
# 
# 
# 
# Note: This question is the same as 1081:
# https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/
# 
#

# @lc code=start
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = ['.']
        visited = set()
        last_idx = {c:i for i,c in enumerate(s) }

        for i, char in enumerate(s):
            if char in visited:
                continue
            
            while(char < stack[-1] and last_idx[stack[-1]] > i ):
                visited.remove(stack.pop())

            stack.append(char)
            visited.add(char)

        return ''.join(stack[1:])


# @lc code=end

