#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.is_balanced = True
        self.dfs(root)
        return self.is_balanced
    
    def dfs(self, node):
        if not node: return 0
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        if abs(left-right) > 1:
            self.is_balanced = False
        return max(left, right) + 1

        
# @lc code=end

