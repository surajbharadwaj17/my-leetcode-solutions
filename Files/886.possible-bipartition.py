#
# @lc app=leetcode id=886 lang=python3
#
# [886] Possible Bipartition
#

# @lc code=start
class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        import collections
        self.graph = collections.defaultdict(list)
        self.is_cycle = 0
        self.dist = [-1]*(n+1)

        # Build adjacency list
        for i,j in dislikes:
            self.graph[i].append(j)
            self.graph[j].append(i)

        for i in range(n):
            # stop if found a cycle
            if self.is_cycle: return False

            if self.dist[i] == -1:
                self.dist[i] = 0
                self.dfs(i)

        return True

    def dfs(self, start):
        if self.is_cycle == 1: return 
        
        for nei in self.graph[start]:
            if self.dist[nei] > 0 and (self.dist[nei] - self.dist[start])%2 == 0:
                self.is_cycle = 1
            elif self.dist[nei] < 0:
                self.dist[nei] = self.dist[start] + 1
                self.dfs(nei)
                
        
# @lc code=end

