#
# @lc app=leetcode id=133 lang=python3
#
# [133] Clone Graph
#

# @lc code=start

# Definition for a Node.

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        graph = {}

        def dfs(node):
            # base condition
            if not node: return

            # create a copy
            copy = Node(node.val)

            # update in graph
            graph[node] = copy

            # dfs for neighbors
            for nei in node.neighbors:
                if nei in graph:
                    copy.neighbors.append(graph[nei])
                else:
                    copy.neighbors.append(dfs(nei))
            
            return copy

        return dfs(node)


# @lc code=end

