#
# @lc app=leetcode id=733 lang=python3
#
# [733] Flood Fill
#

# @lc code=start
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        self.m, self.n = len(image), len(image[0])
        self.cur_color = image[sr][sc]
        self.color = color
        self.dfs(sr, sc, image)
        return image

    def dfs(self, i,j, image):
        # Base 
        if i < 0 or i >= self.m or j < 0 or j >= self.n or  image[i][j] == self.color or image[i][j] != self.cur_color:
            return

        image[i][j] = self.color

        self.dfs(i+1, j, image)
        self.dfs(i-1, j, image)
        self.dfs(i, j+1, image)
        self.dfs(i, j-1, image)
        
# @lc code=end

