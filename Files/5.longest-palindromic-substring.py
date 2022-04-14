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
            temp = self.isPalindrome(s,i,i)

            if len(temp) > len(ret):
                ret = temp

            # even case
            temp = self.isPalindrome(s,i,i+1)
            if len(temp) > len(ret):
                ret = temp

        return ret
            
    
    def isPalindrome(self,s, left, right):

        while(left >=0 and right < len(s) and s[left] == s[right]):
            left -= 1
            right += 1

        return s[left+1:right] 
        
# @lc code=end

