#
# @lc app=leetcode id=647 lang=python3
#
# [647] Palindromic Substrings
#

# @lc code=start


class Solution:
    def countSubstrings(self, s: str) -> int:
        ret_cnt = 0

        self.memo = [[0 for _ in range(len(s))] for x in range(len(s))]

        for i in range(len(s)):
            for j in range(i, len(s)):
                ret_cnt += self.isPalindrome(s,i, j)

        print(self.memo)

        return ret_cnt

    def isPalindrome(self, s, left, right):
        if left >= right:
            return 1
        
        if self.memo[left][right] >= 0:
            return self.memo[left][right] 

        if s[left] == s[right]:
            self.memo[left][right] = self.isPalindrome(s,left+1,right-1)
            return self.memo[left][right]

        else:
            return 0


# @lc code=end

