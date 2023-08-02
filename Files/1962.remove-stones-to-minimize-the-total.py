#
# @lc app=leetcode id=1962 lang=python3
#
# [1962] Remove Stones to Minimize the Total
#

# @lc code=start
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        import heapq
        piles = [-pile for pile in piles]
        heapq.heapify(piles)

        for _ in range(k):
            heapq.heapreplace(piles, piles[0]//2)

        return -sum(piles)


# @lc code=end

