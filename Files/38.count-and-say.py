#
# @lc app=leetcode id=38 lang=python3
#
# [38] Count and Say
#

# @lc code=start
class Solution:
    def countAndSay(self, n: int) -> str:
        #n = 233456
        if n==1: return "1"
        #n = str(n)
        s = self.countAndSay(n-1)
        ret = ""
        i = 0
        while i < len(s):
            count = 1
            while(i < len(s)-1 and s[i] == s[i+1]):
                count += 1
                i += 1
            ret += str(count) + s[i]
            i += 1
        return ret

            
            
        
# @lc code=end

