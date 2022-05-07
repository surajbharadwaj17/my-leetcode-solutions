#
# @lc app=leetcode id=647 lang=python3
#
# [647] Palindromic Substrings
#

# @lc code=start


from functools import lru_cache


class Solution:
    def countSubstrings(self, s: str) -> int:

        @lru_cache(None)
        def isPalindrome(left, right):
            if left > right:
                return True 
            
            if s[left] != s[right]:
                return False

            else:
                return isPalindrome(left+1, right-1)


        ret = 0
        n = len(s)

        for i in range(n):
            for j in range(i,n):
                if isPalindrome(i,j):
                    ret += 1

        return ret

    



# @lc code=end

