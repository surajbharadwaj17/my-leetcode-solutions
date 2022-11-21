#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#
# https://leetcode.com/problems/trapping-rain-water/description/
#
# algorithms
# Hard (55.94%)
# Likes:    17133
# Dislikes: 244
# Total Accepted:    1.1M
# Total Submissions: 1.9M
# Testcase Example:  '[0,1,0,2,1,0,1,3,2,1,2,1]'
#
# Given n non-negative integers representing an elevation map where the width
# of each bar is 1, compute how much water it can trap after raining.
# 
# 
# Example 1:
# 
# 
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array
# [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section)
# are being trapped.
# 
# 
# Example 2:
# 
# 
# Input: height = [4,2,0,3,2,5]
# Output: 9
# 
# 
# 
# Constraints:
# 
# 
# n == height.length
# 1 <= n <= 2 * 10^4
# 0 <= height[i] <= 10^5
# 
# 
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        max_l, max_r = 0,0
        count = 0
        while (left <= right):
            if height[left] <= height[right]:
                if height[left] >= max_l:
                    max_l = height[left]
                else:
                    count += max_l-height[left]
                left += 1   
            else:
                if height[right] >= max_r:
                    max_r = height[right]
                else:
                    count += max_r-height[right]
                right -= 1 
        return count
# @lc code=end

