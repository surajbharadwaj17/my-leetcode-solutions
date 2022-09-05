#
# @lc app=leetcode id=187 lang=python3
#
# [187] Repeated DNA Sequences
#

# @lc code=start
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        hmap = {}
        left, right = 0,  9
        while(right <= len(s)):
            if s[left:right+1] in hmap:
                hmap[s[left:right+1]] += 1
            else:
                hmap[s[left:right+1]] = 1
            left += 1
            right += 1

        
        return [key for key,val in hmap.items() if val>1]
        
# @lc code=end

