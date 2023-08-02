#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#

# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if not s : return []

        ret = []
        self.dfs(s, [], ret)
        return ret
    
    def isPalindrome(self, s):
        return s == s[::-1]

    def dfs(self, s, path, ret):
        if not s:
            ret.append(path)
            return
        for i in range(1, len(s)+1):
            if self.isPalindrome(s[:i]):
                self.dfs(s[i:], path+[s[:i]], ret)

        
# @lc code=end

