#
# @lc app=leetcode id=1971 lang=python3
#
# [1971] Find if Path Exists in Graph
#

# @lc code=start
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        import collections
        graph = collections.defaultdict(list)
        visited = set()

        # Build graph
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)

        def dfs(node, dest, visited):
            if node == dest:
                return True
            if node in visited:
                return False
            visited.add(node)

            for n in graph[node]:
                if(dfs(n, dest, visited)):
                    return True
            return False

        return dfs(source, destination, visited)
# @lc code=end

