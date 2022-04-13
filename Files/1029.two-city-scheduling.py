#
# @lc app=leetcode id=1029 lang=python3
#
# [1029] Two City Scheduling
#
# https://leetcode.com/problems/two-city-scheduling/description/
#
# algorithms
# Medium (59.99%)
# Likes:    3186
# Dislikes: 255
# Total Accepted:    159.1K
# Total Submissions: 255.1K
# Testcase Example:  '[[10,20],[30,200],[400,50],[30,20]]'
#
# A company is planning to interview 2n people. Given the array costs where
# costs[i] = [aCosti, bCosti], the cost of flying the i^th person to city a is
# aCosti, and the cost of flying the i^th person to city b is bCosti.
# 
# Return the minimum cost to fly every person to a city such that exactly n
# people arrive in each city.
# 
# 
# Example 1:
# 
# 
# Input: costs = [[10,20],[30,200],[400,50],[30,20]]
# Output: 110
# Explanation: 
# The first person goes to city A for a cost of 10.
# The second person goes to city A for a cost of 30.
# The third person goes to city B for a cost of 50.
# The fourth person goes to city B for a cost of 20.
# 
# The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people
# interviewing in each city.
# 
# 
# Example 2:
# 
# 
# Input: costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
# Output: 1859
# 
# 
# Example 3:
# 
# 
# Input: costs =
# [[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]]
# Output: 3086
# 
# 
# 
# Constraints:
# 
# 
# 2 * n == costs.length
# 2 <= costs.length <= 100
# costs.length is even.
# 1 <= aCosti, bCosti <= 1000
# 
# 
#

# @lc code=start
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # import math
        # ret = 0
        # a_cnt, b_cnt,n = 0, 0, len(costs)

        # for cost in costs:
        #     if a_cnt < n//2 and b_cnt < n//2:
                
        #         if cost[0] < cost[1]:
        #             ret += cost[0]
        #             a_cnt += 1
        #         else:
        #             ret += cost[1]
        #             b_cnt += 1

        #     elif a_cnt >= n//2 :
        #         ret += cost[1]
        #         b_cnt += 1

        #     elif b_cnt >= n//2 :
        #         ret += cost[0]
        #         a_cnt += 1

        # return ret

        costs.sort(key= lambda x: x[0]-x[1] )

        ret, n = 0, len(costs)//2

        for i in range(n):
            ret += costs[i][0] + costs[i+n][1]

        return ret


# @lc code=end

