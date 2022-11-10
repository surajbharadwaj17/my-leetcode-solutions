98#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        visited = [0 for _ in range(numCourses)]

        # create graph
        for x,y in prerequisites:
            graph[x].append(y)   # courses are the vertices and dependencies are the edges

        for i in range(numCourses):
            if not self.dfs(graph, visited, i):
                return False
        return True

    def dfs(self, graph, visited, i):
        # Base case 
        if visited[i] == -1: # Success case
            return False # Cycle is found
        
        if visited[i] == 1: # Failure base case
            return True 

        visited[i] = -1 # Mark as visited

        for j in graph[i]:  # Check all the neighbors
            if not self.dfs(graph, visited, j):
                return False

        visited[i] = 1
        return True

        
# @lc code=end

