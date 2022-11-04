#
# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#

# @lc code=start
import collections 
class Solution:
    
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        ret = []
        hmap = collections.defaultdict(int)
        plen = len(p)
        slen = len(s)

        if plen > slen : return []

        for char in p:
            hmap[char] += 1

        for i in range(plen-1):
            if s[i] in hmap:
                hmap[s[i]] -= 1

        for i in range(-1,slen-plen+1):
            if i> -1 and s[i] in hmap:
                hmap[s[i]] += 1
            if i+plen < slen and s[i+plen] in hmap:
                hmap[s[i+plen]] -= 1

            flag = True
            for val in hmap.values():
                if val != 0:
                    flag = False
                    break
            if flag:
                ret.append(i+1)

        return ret

        
# @lc code=end

