#
# @lc app=leetcode id=692 lang=python3
#
# [692] Top K Frequent Words
#

# @lc code=start
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        import collections

        count = collections.Counter(words)
        ret = sorted(count, key=lambda x:(-count[x], x))
        return ret[:k]
# @lc code=end

