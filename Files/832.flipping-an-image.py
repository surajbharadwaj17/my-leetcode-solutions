#
# @lc app=leetcode id=832 lang=python3
#
# [832] Flipping an Image
#

# @lc code=start
class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = len(image)
        for i in range(n):
            image[i] = image[i][::-1]

        for i in range(n):
            for j in range(n):
                image[i][j] = 1 - image[i][j]

        return image

        
# @lc code=end

