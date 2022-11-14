#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True
        self.dfs(root)
        return self.balanced

    def dfs(self, node):
        # Base case
        if not node:
            return 0

        # left and right height
        left = self.dfs(node.left)
        right = self.dfs(node.right)

        # Check if the left and right height differ by more than 1
        if abs(left-right) > 1:
            self.balanced = False

        # Return the height
        return max(left, right) + 1

        
# @lc code=end

