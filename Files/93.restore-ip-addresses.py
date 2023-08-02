#
# @lc app=leetcode id=93 lang=python3
#
# [93] Restore IP Addresses
#

# @lc code=start
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ret = []
        self.dfs(s, 0, "", ret)
        return ret
                
    def dfs(self, s, idx, path, ret):
        if idx > 4:
            return
        if idx == 4 and not s :
            ret.append(path[:-1])
            return
        for i in range(1, len(s)+1):
            if s[:i] == '0' or (s[0]!='0' and 0 < int(s[:i]) < 256):
                self.dfs(s[i:], idx+1, path+s[:i]+".", ret)

        
# @lc code=end

