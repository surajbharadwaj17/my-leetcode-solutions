#
# @lc app=leetcode id=881 lang=python3
#
# [881] Boats to Save People
#
# https://leetcode.com/problems/boats-to-save-people/description/
#
# algorithms
# Medium (49.92%)
# Likes:    2217
# Dislikes: 60
# Total Accepted:    109.8K
# Total Submissions: 214.4K
# Testcase Example:  '[1,2]\n3'
#
# You are given an array people where people[i] is the weight of the i^th
# person, and an infinite number of boats where each boat can carry a maximum
# weight of limit. Each boat carries at most two people at the same time,
# provided the sum of the weight of those people is at most limit.
# 
# Return the minimum number of boats to carry every given person.
# 
# 
# Example 1:
# 
# 
# Input: people = [1,2], limit = 3
# Output: 1
# Explanation: 1 boat (1, 2)
# 
# 
# Example 2:
# 
# 
# Input: people = [3,2,2,1], limit = 3
# Output: 3
# Explanation: 3 boats (1, 2), (2) and (3)
# 
# 
# Example 3:
# 
# 
# Input: people = [3,5,3,4], limit = 5
# Output: 4
# Explanation: 4 boats (3), (3), (4), (5)
# 
# 
# 
# Constraints:
# 
# 
# 1 <= people.length <= 5 * 10^4
# 1 <= people[i] <= limit <= 3 * 10^4
# 
# 
#

# @lc code=start
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        # sort people. Pair the heaviest person with the lightest person.
        # If sum of the weights is more than the limit, let the heavier person go alone!

        people = sorted(people, reverse=True)
        n = len(people)
        left, right = 0, n-1
        while(left <= right):
            if people[left] + people[right] <= limit:
                right -= 1
            
            left += 1
            
        return left


# Note: Always sort the array before using 2 pointer technique


# @lc code=end

