#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height)-1  # 2 pointers
        mx_area = 0     # result

        while left <= right:
            length = min(height[left], height[right]) # calculate the height of the container
            width = right-left      # calculate the width of the container
            area = length*width     # calculate the area
            mx_area = max(mx_area, area)        # update the result if found a bigger container

            if height[left] > height[right]:    # Move the pointer on the shorter height side of the two
                right -= 1
            else:
                left += 1

        return mx_area

        
# @lc code=end

