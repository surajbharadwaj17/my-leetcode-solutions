#
# @lc app=leetcode id=417 lang=python3
#
# [417] Pacific Atlantic Water Flow
#

# @lc code=start


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights: return []

        rows, cols = len(heights), len(heights[0])
        pac_visited, atl_visited = set(), set()
        directions = ((0,1), (0,-1), (-1,0), (1,0))

        def dfs(i,j,visited):
            if (i,j) in visited: return
            visited.add((i,j))

            for dir in directions:
                next_i, next_j = i+dir[0], j+dir[1]

                if 0 <= next_i < rows and 0 <= next_j < cols:
                    if heights[next_i][next_j] >= heights[i][j]:
                        dfs(next_i, next_j, visited)

        for row in range(rows):
            dfs(row, 0, pac_visited)
            dfs(row, cols-1, atl_visited)

        for col in range(cols):
            dfs(0, col, pac_visited)
            dfs(rows-1, col, atl_visited)

        return [ele for ele in pac_visited if ele in atl_visited]
 
        
# @lc code=end

