#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
import collections
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = collections.defaultdict(list)

        for word in strs:
            arr = [0]*26
            for char in word:
                arr[ord(char) - ord('a')] += 1

            hmap[tuple(arr)].append(word)

        return hmap.values()        
# @lc code=end

