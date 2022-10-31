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
        hmap = {}

        def dfs(node):
            if not node:
                return 
            node_copy = Node(node.val)
            hmap[node] = node_copy

            for n in node.neighbors:
                if n in hmap:
                    node_copy.neighbors.append(hmap[n])
                else:
                    node_copy.neighbors.append(dfs(n))
            return node_copy

        return dfs(node)
# @lc code=end

