#
# @lc app=leetcode id=429 lang=python3
#
# [429] N-ary Tree Level Order Traversal
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        #BFS
        if not root: return []
        level = [root]
        ret = []

        while level:
            ret.append([node.val for node in level])
            level = [ child for node in level for child in node.children if child]
        return ret
# @lc code=end

