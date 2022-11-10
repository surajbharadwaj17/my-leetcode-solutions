#
# @lc app=leetcode id=994 lang=python3
#
# [994] Rotting Oranges
#

# @lc code=start
import collections
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid: return 0

        self.m,self.n = len(grid), len(grid[0])
        n_fresh = 0
        rotten = collections.deque()
        self.dirs = [(0,1), (-1,0), (0, -1), (1,0)]

        # Identify rotten and fresh
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == 2:
                    rotten.append((i,j))
                elif grid[i][j] == 1:
                    n_fresh += 1

        return self.bfs(rotten, n_fresh, grid)

    def bfs(self, rotten, n_fresh, grid):
        mins = 0
        while(rotten and n_fresh > 0):  # Loop as long as there are rotten oranges and fresh count > 0
            mins += 1

            for _ in range(len(rotten)): # Search from all the rotten oranges
                x,y = rotten.popleft()

                for dir in self.dirs:   # Check in all directions
                    new_x, new_y = x+dir[0], y+dir[1]

                    # Base case. Ignore if the new cordinates are out of bound or if we encounter an already rotten orange or an empty cell.
                    if new_x < 0 or new_x >= self.m or new_y < 0 or new_y >= self.n \
                        or grid[new_x][new_y] == 2 or grid[new_x][new_y] == 0:
                        continue

                    # If fresh,
                    n_fresh -= 1    # Decrement the fresh count
                    grid[new_x][new_y] = 2  # Mark it as rotten
                    rotten.append((new_x, new_y)) # Add it to the rotten queue

        return mins if n_fresh == 0 else  -1




        
# @lc code=end

