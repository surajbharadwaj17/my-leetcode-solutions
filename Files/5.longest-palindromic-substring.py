#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:

        ret = ""
        for i in range(len(s)):

            #odd case
            temp = self._is_palindrome(s,i,i)

            if len(temp) > len(ret):
                ret = temp

            # even case
            temp = self._is_palindrome(s,i,i+1)
            if len(temp) > len(ret):
                ret = temp

        return ret
            

    def _is_palindrome(self, s, start, end):
        while(start>=0 and end < len(s) and s[start] == s[end]):
            start -= 1
            end +=1

        return s[start+1:end]
        
        
# @lc code=end

