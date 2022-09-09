#
# @lc app=leetcode id=606 lang=python3
#
# [606] Construct String from Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root: return ""
        left, right = "", ""
        if root.left or root.right:
            left = f"({self.tree2str(root.left)})"
        if root.right:
            right = f"({self.tree2str(root.right)})"

        return f"{root.val}{left}{right}"
        
# @lc code=end

