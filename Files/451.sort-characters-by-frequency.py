#
# @lc app=leetcode id=451 lang=python3
#
# [451] Sort Characters By Frequency
#

# @lc code=start
class Solution:
    def frequencySort(self, s: str) -> str:
        import collections

        # Counting frequencies
        count = collections.Counter(s)

        ret = ""

        # Sorting hmap items in descending order based on values (frequencies in this case.)

        for key,val in sorted(count.items(), key=lambda x:x[1], reverse=True): 

            # Constructing the result string
            ret += key*val

        return ret
        
# @lc code=end

