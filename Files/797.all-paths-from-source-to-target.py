#
# @lc app=leetcode id=797 lang=python3
#
# [797] All Paths From Source to Target
#

# @lc code=start
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        if not graph: return []
        ret = []
        stack = [(0, [0])] # Node and the path

        d = {}
        for i in range(len(graph)):
            d[i] = graph[i]
        n = len(graph)
        while stack:
            node, path = stack.pop()
            if node == n-1:
                ret.append(path)
            
            for nei in d[node]:
                stack.append((nei, path+[nei]))
        return ret

        
# @lc code=end

