#
# @lc app=leetcode id=623 lang=python3
#
# [623] Add One Row to Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        # BFS solution
        dummy, dummy.left = TreeNode(None), root
        level = [dummy]

        for _ in range(depth-1):
            level = [ child for node in level for child in (node.left, node.right) if child]

        for node in level:
            node.left, node.left.left = TreeNode(val), node.left
            node.right, node.right.right = TreeNode(val), node.right

        return dummy.left

        
# @lc code=end

