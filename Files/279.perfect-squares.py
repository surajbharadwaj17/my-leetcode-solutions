#
# @lc app=leetcode id=279 lang=python3
#
# [279] Perfect Squares
#

# @lc code=start
class Solution:
    def numSquares(self, n: int) -> int:
        import collections
        squares = []
        i = 1
        while i**2 <= n:
            squares.append(i**2)
            i += 1

        count = 0
        # BFS
        q = collections.deque([n])
        while q:
            count += 1
            temp = set() # Build the queue 
            for x in q:
                for sq in squares:
                    if x == sq:     # Success condition
                        return count
                    if x < sq:      # Backtrack case
                        break
                    temp.add(x-sq)
            q = temp

        return count

        
# @lc code=end

