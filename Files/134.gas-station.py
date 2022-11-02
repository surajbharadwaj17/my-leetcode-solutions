#
# @lc app=leetcode id=134 lang=python3
#
# [134] Gas Station
#

# @lc code=start
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start = 0
        cur = 0
        trip = 0

        for i in range(len(gas)):
            trip += gas[i] - cost[i]
            cur += gas[i] - cost[i]

            if cur < 0:         # If current tank capacity becomes negative, need a different start point
                start = i+1
                cur = 0

        if trip >= 0:       # If you have fuel left at the end of the trip, return the start point
            return start
        return -1
        
# @lc code=end

