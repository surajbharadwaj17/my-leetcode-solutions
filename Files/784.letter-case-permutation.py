#
# @lc app=leetcode id=784 lang=python3
#
# [784] Letter Case Permutation
#
# https://leetcode.com/problems/letter-case-permutation/description/
#
# algorithms
# Medium (71.91%)
# Likes:    3169
# Dislikes: 141
# Total Accepted:    204.8K
# Total Submissions: 284K
# Testcase Example:  '"a1b2"'
#
# Given a string s, you can transform every letter individually to be lowercase
# or uppercase to create another string.
# 
# Return a list of all possible strings we could create. Return the output in
# any order.
# 
# 
# Example 1:
# 
# 
# Input: s = "a1b2"
# Output: ["a1b2","a1B2","A1b2","A1B2"]
# 
# 
# Example 2:
# 
# 
# Input: s = "3z4"
# Output: ["3z4","3Z4"]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 12
# s consists of lowercase English letters, uppercase English letters, and
# digits.
# 
# 
#

# @lc code=start
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ret = []
        s = list(s)

        def dfs(ret, i, s):
            if i == len(s):
                ret.append(''.join(s))

            else:
                if s[i].isalpha():
                    s[i] = s[i].upper()

                    dfs(ret, i+1, s) # upper case branch

                    s[i] = s[i].lower()

                    dfs(ret, i+1, s) # lower case branch

                else:
                    dfs(ret, i+1, s)

        dfs(ret, 0, s)

        return ret
        
# @lc code=end

