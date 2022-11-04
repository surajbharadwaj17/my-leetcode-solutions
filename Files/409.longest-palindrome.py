#
# @lc app=leetcode id=409 lang=python3
#
# [409] Longest Palindrome
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> int:
        hash = set()

        for char in s:
            if char not in hash:
                hash.add(char)
            else:
                hash.remove(char)

        # Hash will contain odd characters. 
        # Subtract from the length of s will be the length of longest palindrome

        if len(hash) == 0:
            return len(s)
        else:
            return len(s)-len(hash)+1
        
# @lc code=end

