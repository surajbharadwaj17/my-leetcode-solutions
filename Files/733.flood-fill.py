#
# @lc app=leetcode id=733 lang=python3
#
# [733] Flood Fill
#

# @lc code=start
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:


        m,n = len(image), len(image[0])

        cur_color = image[sr][sc]
        dirs = ((0,1),(0,-1),(-1,0),(1,0))

        # DFS 
        def dfs(sr, sc):
            # Base 
            if 0 <= sr < m and 0 <= sc < n and image[sr][sc] == cur_color and image[sr][sc] != color:
                image[sr][sc] = color 


                dfs(sr+1, sc)
                dfs(sr-1, sc)
                dfs(sr, sc+1)
                dfs(sr, sc-1)

        dfs(sr,sc)

        return image
        
# @lc code=end

